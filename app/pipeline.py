# app/pipeline.py
import time
import json
import re

from ai.task_checker import check_solution
from ai.task_generator import generate_task
from ai.tutor import chat_with_tutor

from database.crud import create, get, update
from database.models import Task

from knowledgebase_pipeline.retrieval import (
    retrieve_context_with_metadata,
)

TUTOR_HISTORY_LIMIT = 10


def _log_separator(title: str) -> None:
    print()
    print("=" * 70)
    print(f"[PIPELINE] {title}")
    print("=" * 70)


def _log_rag_metadata(metadata: list[dict]) -> None:
    print(f"[RAG] Retrieved chunks: {len(metadata)}")

    for item in metadata:
        score = item.get("score")

        if isinstance(score, (int, float)):
            score_text = f"{score:.6f}"
        else:
            score_text = str(score)

        print(
            f"[RAG] "
            f"rank={item.get('rank')} "
            f"id={item.get('id')} "
            f"score={score_text} "
            f"source={item.get('source')} "
            f"section={item.get('section')} "
            f"text_length={item.get('text_length')}"
        )


def _parse_solution_text(solution_text: str | None) -> dict:
    """
    Разбирает содержимое Task.solution_text.

    Формат:

    РЕШЕНИЕ:
    ...

    РЕЗУЛЬТАТ ПРОВЕРКИ:
    ...

    ДИАЛОГ:
    USER:
    ...

    TUTOR:
    ...
    """

    if not solution_text:
        return {
            "solution": "",
            "feedback": {},
            "history": [],
        }

    solution = ""
    feedback = {}
    dialogue = ""

    solution_marker = "РЕШЕНИЕ:"
    feedback_marker = "РЕЗУЛЬТАТ ПРОВЕРКИ:"
    dialogue_marker = "ДИАЛОГ:"

    if solution_marker in solution_text:
        after_solution = solution_text.split(
            solution_marker,
            1,
        )[1]

        if feedback_marker in after_solution:
            solution = after_solution.split(
                feedback_marker,
                1,
            )[0].strip()
        else:
            solution = after_solution.strip()

    if feedback_marker in solution_text:
        after_feedback = solution_text.split(
            feedback_marker,
            1,
        )[1]

        if dialogue_marker in after_feedback:
            feedback_text = after_feedback.split(
                dialogue_marker,
                1,
            )[0].strip()
        else:
            feedback_text = after_feedback.strip()

        if feedback_text:
            try:
                feedback = json.loads(feedback_text)
            except json.JSONDecodeError:
                feedback = {
                    "explanation": feedback_text,
                }

    if dialogue_marker in solution_text:
        dialogue = solution_text.split(
            dialogue_marker,
            1,
        )[1].strip()

    history = _parse_dialogue(dialogue)

    return {
        "solution": solution,
        "feedback": feedback,
        "history": history,
    }


def _parse_dialogue(dialogue: str) -> list[dict]:
    """
    Преобразует сохранённый диалог в формат,
    который принимает Tutor.
    """

    if not dialogue:
        return []

    pattern = re.compile(
        r"^(USER|TUTOR):\s*$",
        re.MULTILINE,
    )

    matches = list(pattern.finditer(dialogue))

    history = []

    for index, match in enumerate(matches):
        start = match.end()

        if index + 1 < len(matches):
            end = matches[index + 1].start()
        else:
            end = len(dialogue)

        content = dialogue[start:end].strip()

        if not content:
            continue

        role = (
            "user"
            if match.group(1) == "USER"
            else "assistant"
        )

        history.append(
            {
                "role": role,
                "content": content,
            }
        )

    return history


def _build_solution_text(
        solution: str,
        feedback: dict,
        history: list[dict],
) -> str:
    """
    Формирует единый текст для хранения
    в Task.solution_text.
    """

    parts = [
        "РЕШЕНИЕ:",
        solution.strip(),
        "",
        "РЕЗУЛЬТАТ ПРОВЕРКИ:",
        json.dumps(
            feedback,
            ensure_ascii=False,
            indent=2,
        ),
        "",
        "ДИАЛОГ:",
    ]

    for message in history:
        if message["role"] == "user":
            parts.append("USER:")
        else:
            parts.append("TUTOR:")

        parts.append(message["content"])
        parts.append("")

    return "\n".join(parts).strip()


def generate_task_pipeline(
        user_id: int,
        topic: str,
        difficulty: str,
) -> int:
    if not topic.strip():
        raise ValueError("Topic cannot be empty.")

    if not difficulty.strip():
        raise ValueError("Difficulty cannot be empty.")

    total_start = time.perf_counter()

    _log_separator("TASK GENERATION")

    print(f"[PIPELINE] user_id={user_id}")
    print(f"[PIPELINE] topic={topic}")
    print(f"[PIPELINE] difficulty={difficulty}")

    # ========================================
    # RAG
    # ========================================

    rag_start = time.perf_counter()

    rag_query = f"Python {topic}"

    context, rag_metadata = retrieve_context_with_metadata(
        query=rag_query,
    )

    rag_elapsed = time.perf_counter() - rag_start

    print()
    print("[RAG] Query:")
    print(f"[RAG] {rag_query}")

    _log_rag_metadata(rag_metadata)

    print(
        f"[RAG] Context length: "
        f"{len(context)} characters"
    )

    print(
        f"[RAG] Retrieval time: "
        f"{rag_elapsed:.2f} seconds"
    )

    # ========================================
    # TASK GENERATOR
    # ========================================

    generator_start = time.perf_counter()

    task_text = generate_task(
        topic=topic,
        difficulty=difficulty,
        context=context,
    )

    generator_elapsed = (
            time.perf_counter() - generator_start
    )

    if not task_text or not task_text.strip():
        raise RuntimeError(
            "Task Generator returned an empty task."
        )

    print()
    print("[GENERATOR] Task generated")

    print(
        f"[GENERATOR] Output length: "
        f"{len(task_text)} characters"
    )

    print(
        f"[GENERATOR] Generation time: "
        f"{generator_elapsed:.2f} seconds"
    )

    print("[GENERATOR] Generated task:")
    print("-" * 70)
    print(task_text)
    print("-" * 70)

    # ========================================
    # POSTGRESQL
    # ========================================

    db_start = time.perf_counter()

    task = create(
        Task,
        user_id=user_id,
        topic=topic,
        difficulty=difficulty,
        task_text=task_text,
    )

    db_elapsed = time.perf_counter() - db_start

    print()
    print("[DATABASE] Task created")
    print(f"[DATABASE] task_id={task.id}")

    print(
        f"[DATABASE] PostgreSQL time: "
        f"{db_elapsed:.2f} seconds"
    )

    # ========================================
    # TOTAL
    # ========================================

    total_elapsed = time.perf_counter() - total_start

    print()
    print("[PIPELINE] Task generation completed")
    print(f"[PIPELINE] task_id={task.id}")

    print(
        f"[PIPELINE] Total time: "
        f"{total_elapsed:.2f} seconds"
    )

    return task.id


def check_task_pipeline(
        task_id: int,
        solution: str,
) -> dict:
    """
    Проверяет решение задачи через RAG + Task Checker
    и сохраняет результат в PostgreSQL.

    Возвращает результат проверки.
    """

    if not solution.strip():
        raise ValueError("Solution cannot be empty.")

    total_start = time.perf_counter()

    _log_separator("TASK CHECK")

    print(f"[PIPELINE] task_id={task_id}")

    print(
        f"[PIPELINE] Solution length: "
        f"{len(solution)} characters"
    )

    # ========================================
    # LOAD TASK
    # ========================================

    db_start = time.perf_counter()

    task = get(Task, task_id)

    db_load_elapsed = time.perf_counter() - db_start

    if task is None:
        raise ValueError(
            f"Task with id={task_id} not found."
        )

    if task.score is not None:
        raise ValueError(
            "Task has already been checked."
        )

    print(
        f"[DATABASE] Task loaded in "
        f"{db_load_elapsed:.2f} seconds"
    )

    print(f"[DATABASE] user_id={task.user_id}")
    print(f"[DATABASE] topic={task.topic}")
    print(f"[DATABASE] difficulty={task.difficulty}")

    print(
        f"[DATABASE] Task text length: "
        f"{len(task.task_text)} characters"
    )

    # ========================================
    # RAG
    # ========================================

    rag_start = time.perf_counter()

    rag_query = (
        f"Python {task.topic}\n"
        f"{task.task_text}"
    )

    context, rag_metadata = retrieve_context_with_metadata(
        query=rag_query,
    )

    rag_elapsed = time.perf_counter() - rag_start

    print()
    print("[RAG] Query length:")
    print(f"[RAG] {len(rag_query)} characters")

    _log_rag_metadata(rag_metadata)

    print(
        f"[RAG] Context length: "
        f"{len(context)} characters"
    )

    print(
        f"[RAG] Retrieval time: "
        f"{rag_elapsed:.2f} seconds"
    )

    # ========================================
    # TASK CHECKER
    # ========================================

    checker_start = time.perf_counter()

    result = check_solution(
        task=task.task_text,
        solution=solution,
        context=context,
    )

    checker_elapsed = (
            time.perf_counter() - checker_start
    )

    if not isinstance(result, dict):
        raise RuntimeError(
            "Task Checker returned invalid result."
        )

    if "score" not in result:
        raise RuntimeError(
            "Task Checker result does not contain score."
        )

    score = result["score"]

    if not isinstance(score, int) or not 0 <= score <= 10:
        raise RuntimeError(
            "Task Checker returned invalid score."
        )

    errors = result.get("errors", [])
    recommendations = result.get(
        "recommendations",
        [],
    )

    print()
    print("[CHECKER] Result:")

    print(
        f"[CHECKER] is_correct="
        f"{result.get('is_correct')}"
    )

    print(f"[CHECKER] score={score}")

    print(
        f"[CHECKER] errors_count="
        f"{len(errors) if isinstance(errors, list) else 'N/A'}"
    )

    print(
        f"[CHECKER] recommendations_count="
        f"{len(recommendations) if isinstance(recommendations, list) else 'N/A'}"
    )

    print(
        f"[CHECKER] Explanation length: "
        f"{len(str(result.get('explanation', '')))} characters"
    )

    print(
        f"[CHECKER] Processing time: "
        f"{checker_elapsed:.2f} seconds"
    )

    print("[CHECKER] Full result:")
    print("-" * 70)
    print(
        json.dumps(
            result,
            ensure_ascii=False,
            indent=2,
        )
    )
    print("-" * 70)

    # ========================================
    # SAVE RESULT
    # ========================================

    existing = _parse_solution_text(
        task.solution_text,
    )

    solution_text = _build_solution_text(
        solution=solution,
        feedback=result,
        history=existing["history"],
    )

    db_start = time.perf_counter()

    update(
        Task,
        task_id,
        solution_text=solution_text,
        score=score,
    )

    db_elapsed = time.perf_counter() - db_start

    print()
    print(
        f"[DATABASE] Checker result saved in "
        f"{db_elapsed:.2f} seconds"
    )

    # ========================================
    # TOTAL
    # ========================================

    total_elapsed = time.perf_counter() - total_start

    print()
    print("[PIPELINE] Task check completed")

    print(
        f"[PIPELINE] Total time: "
        f"{total_elapsed:.2f} seconds"
    )

    return result


def tutor_pipeline(
        task_id: int,
        question: str,
) -> str:
    """
    Отправляет вопрос текущей задачи Tutor Agent,
    получает ответ и сохраняет диалог
    в Task.solution_text.

    Возвращает ответ Tutor.
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    total_start = time.perf_counter()

    _log_separator("TUTOR")

    print(f"[PIPELINE] task_id={task_id}")

    print(
        f"[PIPELINE] Question length: "
        f"{len(question)} characters"
    )

    # ========================================
    # LOAD TASK
    # ========================================

    db_start = time.perf_counter()

    task = get(Task, task_id)

    db_load_elapsed = time.perf_counter() - db_start

    if task is None:
        raise ValueError(
            f"Task with id={task_id} not found."
        )

    print(
        f"[DATABASE] Task loaded in "
        f"{db_load_elapsed:.2f} seconds"
    )

    print(f"[DATABASE] user_id={task.user_id}")
    print(f"[DATABASE] topic={task.topic}")
    print(f"[DATABASE] difficulty={task.difficulty}")

    print(
        f"[DATABASE] Task text length: "
        f"{len(task.task_text)} characters"
    )

    # ========================================
    # PARSE STORED DATA
    # ========================================

    parsed = _parse_solution_text(
        task.solution_text,
    )

    solution = parsed["solution"]
    feedback = parsed["feedback"]
    history = parsed["history"]

    print()
    print("[TUTOR] Stored data:")

    print(
        f"[TUTOR] Solution length: "
        f"{len(solution)} characters"
    )

    print(
        f"[TUTOR] History messages: "
        f"{len(history)}"
    )

    print(
        f"[TUTOR] Feedback fields: "
        f"{list(feedback.keys())}"
    )

    # ========================================
    # RAG
    # ========================================

    rag_start = time.perf_counter()

    rag_query = (
        f"Python {task.topic}\n"
        f"{task.task_text}"
    )

    context, rag_metadata = retrieve_context_with_metadata(
        query=rag_query,
    )

    rag_elapsed = time.perf_counter() - rag_start

    print()
    print("[RAG] Query length:")
    print(f"[RAG] {len(rag_query)} characters")

    _log_rag_metadata(rag_metadata)

    print(
        f"[RAG] Context length: "
        f"{len(context)} characters"
    )

    print(
        f"[RAG] Retrieval time: "
        f"{rag_elapsed:.2f} seconds"
    )

    # ========================================
    # PREPARE TUTOR CONTEXT
    # ========================================

    feedback_text = json.dumps(
        feedback,
        ensure_ascii=False,
        indent=2,
    )

    recent_history = history[-TUTOR_HISTORY_LIMIT:]

    print()
    print("[TUTOR] Context:")

    print(
        f"[TUTOR] Full history messages: "
        f"{len(history)}"
    )

    print(
        f"[TUTOR] History limit: "
        f"{TUTOR_HISTORY_LIMIT}"
    )

    print(
        f"[TUTOR] Messages sent to model: "
        f"{len(recent_history)}"
    )

    print(
        f"[TUTOR] Feedback length: "
        f"{len(feedback_text)} characters"
    )

    # ========================================
    # TUTOR
    # ========================================

    tutor_start = time.perf_counter()

    answer = chat_with_tutor(
        task=task.task_text,
        solution=solution,
        feedback=feedback_text,
        context=context,
        history=recent_history,
        question=question,
    )

    tutor_elapsed = time.perf_counter() - tutor_start

    if not answer or not answer.strip():
        raise RuntimeError(
            "Tutor returned an empty answer."
        )

    print()
    print("[TUTOR] Answer generated")

    print(
        f"[TUTOR] Answer length: "
        f"{len(answer)} characters"
    )

    print(
        f"[TUTOR] Processing time: "
        f"{tutor_elapsed:.2f} seconds"
    )

    # ========================================
    # SAVE DIALOGUE
    # ========================================

    history.append(
        {
            "role": "user",
            "content": question.strip(),
        }
    )

    history.append(
        {
            "role": "assistant",
            "content": answer.strip(),
        }
    )

    solution_text = _build_solution_text(
        solution=solution,
        feedback=feedback,
        history=history,
    )

    db_start = time.perf_counter()

    update(
        Task,
        task_id,
        solution_text=solution_text,
    )

    db_elapsed = time.perf_counter() - db_start

    print()
    print(
        f"[DATABASE] Dialogue saved in "
        f"{db_elapsed:.2f} seconds"
    )

    # ========================================
    # TOTAL
    # ========================================

    total_elapsed = time.perf_counter() - total_start

    print()
    print("[PIPELINE] Tutor request completed")

    print(
        f"[PIPELINE] Total time: "
        f"{total_elapsed:.2f} seconds"
    )

    return answer
