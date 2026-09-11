# app/routes.py
import time
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app.pipeline import (
    _parse_solution_text,
    check_task_pipeline,
    generate_task_pipeline,
    tutor_pipeline,
)
from database.crud import create, get, get_all
from database.models import Task, User

main = Blueprint("main", __name__)


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        users = get_all(
            User,
            username=username,
        )

        if not users:
            return render_template(
                "login.html",
                error="Неверное имя пользователя или пароль.",
            )

        user = users[0]

        if user.password != password:
            return render_template(
                "login.html",
                error="Неверное имя пользователя или пароль.",
            )

        session["user_id"] = user.id

        return redirect(
            url_for("main.profile")
        )

    return render_template("login.html")


@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get(
            "username",
            "",
        ).strip()

        password = request.form.get(
            "password",
            "",
        )

        password_confirm = request.form.get(
            "password_confirm",
            "",
        )

        if not username or not password:
            return render_template(
                "register.html",
                error="Заполните все поля.",
            )

        if password != password_confirm:
            return render_template(
                "register.html",
                error="Пароли не совпадают.",
            )

        existing_users = get_all(
            User,
            username=username,
        )

        if existing_users:
            return render_template(
                "register.html",
                error="Пользователь с таким именем уже существует.",
            )

        create(
            User,
            username=username,
            password=password,
        )

        return redirect(
            url_for("main.login")
        )

    return render_template("register.html")


@main.route("/")
@main.route("/profile")
def profile():
    user_id = session.get("user_id")

    if user_id is None:
        return redirect(
            url_for("main.login")
        )

    user = get(
        User,
        user_id,
    )

    if user is None:
        session.clear()

        return redirect(
            url_for("main.login")
        )

    # Получаем только задачи текущего пользователя.
    all_tasks = get_all(
        Task,
        user_id=user.id,
    )

    # На профиле показываем только решённые задачи.
    # Решённой считается задача, для которой уже есть score.
    solved_tasks = [
        task
        for task in all_tasks
        if task.score is not None
    ]

    # Новые задачи сверху.
    solved_tasks.sort(
        key=lambda task: task.created_at,
        reverse=True,
    )

    return render_template(
        "profile.html",
        user=user,
        tasks=solved_tasks,
    )


@main.route("/logout")
def logout():
    session.clear()

    return redirect(
        url_for("main.login")
    )


@main.route(
    "/generate",
    methods=["GET", "POST"],
)
def generate():
    user_id = session.get("user_id")

    if user_id is None:
        return redirect(
            url_for("main.login")
        )

    if request.method == "POST":
        topic = request.form.get(
            "topic",
            "",
        ).strip()

        difficulty = request.form.get(
            "difficulty",
            "",
        ).strip()

        if not topic or not difficulty:
            return render_template(
                "generate.html",
                error="Выберите тему и сложность.",
                selected_topic=topic,
                selected_difficulty=difficulty,
            )

        start_time = time.perf_counter()

        try:
            task_id = generate_task_pipeline(
                user_id=user_id,
                topic=topic,
                difficulty=difficulty,
            )

            elapsed = time.perf_counter() - start_time

            print(
                f"[GENERATE] Task created successfully "
                f"in {elapsed:.2f} seconds"
            )

        except Exception as exc:
            elapsed = time.perf_counter() - start_time

            print(
                f"[GENERATE] Failed after "
                f"{elapsed:.2f} seconds: {exc}"
            )

            return render_template(
                "generate.html",
                error=f"Не удалось создать задачу: {exc}",
                selected_topic=topic,
                selected_difficulty=difficulty,
            )

        return redirect(
            url_for(
                "main.task",
                task_id=task_id,
            )
        )

    return render_template(
        "generate.html",
    )


@main.route(
    "/task/<int:task_id>",
    methods=["GET", "POST"],
)
def task(task_id):
    user_id = session.get("user_id")

    if user_id is None:
        return redirect(
            url_for("main.login")
        )

    task_obj = get(
        Task,
        task_id,
    )

    if task_obj is None:
        return redirect(
            url_for("main.profile")
        )

    # Пользователь может работать только со своими задачами.
    if task_obj.user_id != user_id:
        return redirect(
            url_for("main.profile")
        )

    if request.method == "POST":
        action = request.form.get(
            "action",
            "",
        )

        # ============================================================
        # CHECK SOLUTION
        # ============================================================

        if action == "check":
            # Проверку можно выполнить только один раз.
            if task_obj.score is not None:
                return redirect(
                    url_for(
                        "main.task",
                        task_id=task_id,
                    )
                )

            solution = request.form.get(
                "solution",
                "",
            ).strip()

            if not solution:
                parsed = _parse_solution_text(
                    task_obj.solution_text,
                )

                return render_template(
                    "task.html",
                    task=task_obj,
                    parsed=parsed,
                    error="Введите решение.",
                )

            try:
                check_task_pipeline(
                    task_id=task_id,
                    solution=solution,
                )
            except Exception as exc:
                parsed = _parse_solution_text(
                    task_obj.solution_text,
                )

                return render_template(
                    "task.html",
                    task=task_obj,
                    parsed=parsed,
                    error=f"Не удалось проверить решение: {exc}",
                )

            return redirect(
                url_for(
                    "main.task",
                    task_id=task_id,
                )
            )

        # ============================================================
        # TUTOR QUESTION
        # ============================================================

        if action == "tutor":
            # Вопросы доступны только после проверки решения.
            if task_obj.score is None:
                return redirect(
                    url_for(
                        "main.task",
                        task_id=task_id,
                    )
                )

            question = request.form.get(
                "question",
                "",
            ).strip()

            if not question:
                parsed = _parse_solution_text(
                    task_obj.solution_text,
                )

                return render_template(
                    "task.html",
                    task=task_obj,
                    parsed=parsed,
                    error="Введите вопрос.",
                )

            try:
                tutor_pipeline(
                    task_id=task_id,
                    question=question,
                )
            except Exception as exc:
                parsed = _parse_solution_text(
                    task_obj.solution_text,
                )

                return render_template(
                    "task.html",
                    task=task_obj,
                    parsed=parsed,
                    error=f"Не удалось получить ответ: {exc}",
                )

            return redirect(
                url_for(
                    "main.task",
                    task_id=task_id,
                )
            )

    parsed = _parse_solution_text(
        task_obj.solution_text,
    )

    return render_template(
        "task.html",
        task=task_obj,
        parsed=parsed,
    )
