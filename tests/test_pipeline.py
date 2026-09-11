# tests/test_pipeline.py
from pprint import pprint

from app.pipeline import (
    generate_task_pipeline,
    check_task_pipeline,
    tutor_pipeline,
)

from database.crud import get
from database.models import Task

# Используй ID существующего пользователя в PostgreSQL.
USER_ID = 1


def main():
    # ================================================================
    # 1. GENERATE TASK
    # ================================================================

    print("=" * 70)
    print("1. TEST: GENERATE TASK PIPELINE")
    print("=" * 70)

    task_id = generate_task_pipeline(
        user_id=USER_ID,
        topic="list",
        difficulty="beginner",
    )

    print()
    print(f"Task created successfully.")
    print(f"Task ID: {task_id}")

    task = get(Task, task_id)

    if task is None:
        raise RuntimeError(
            "Generated task was not found in PostgreSQL."
        )

    print()
    print("Saved task:")
    print(task.task_text)

    # ================================================================
    # 2. CHECK SOLUTION
    # ================================================================

    print()
    print("=" * 70)
    print("2. TEST: CHECK TASK PIPELINE")
    print("=" * 70)

    solution = """
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
"""

    result = check_task_pipeline(
        task_id=task_id,
        solution=solution,
    )

    print()
    print("Checker result:")
    pprint(result)

    task = get(Task, task_id)

    if task is None:
        raise RuntimeError(
            "Task was not found after checking."
        )

    print()
    print(f"Saved score: {task.score}")

    print()
    print("Saved solution_text:")
    print(task.solution_text)

    # ================================================================
    # 3. TUTOR
    # ================================================================

    print()
    print("=" * 70)
    print("3. TEST: TUTOR PIPELINE")
    print("=" * 70)

    question = (
        "Почему после append() число 4 оказалось "
        "последним элементом списка?"
    )

    answer = tutor_pipeline(
        task_id=task_id,
        question=question,
    )

    print()
    print("Tutor answer:")
    print(answer)

    # ================================================================
    # 4. VERIFY DATABASE
    # ================================================================

    print()
    print("=" * 70)
    print("4. VERIFY DATABASE")
    print("=" * 70)

    task = get(Task, task_id)

    if task is None:
        raise RuntimeError(
            "Task was not found after tutor."
        )

    print()
    print(f"Task ID:       {task.id}")
    print(f"User ID:       {task.user_id}")
    print(f"Topic:         {task.topic}")
    print(f"Difficulty:    {task.difficulty}")
    print(f"Score:         {task.score}")

    print()
    print("Full solution_text:")
    print("-" * 70)
    print(task.solution_text)
    print("-" * 70)

    # ================================================================
    # 5. FINAL CHECKS
    # ================================================================

    if task.score is None:
        raise RuntimeError(
            "Score was not saved to PostgreSQL."
        )

    if not task.solution_text:
        raise RuntimeError(
            "solution_text was not saved to PostgreSQL."
        )

    if "РЕШЕНИЕ:" not in task.solution_text:
        raise RuntimeError(
            "solution_text does not contain solution section."
        )

    if "РЕЗУЛЬТАТ ПРОВЕРКИ:" not in task.solution_text:
        raise RuntimeError(
            "solution_text does not contain checker feedback."
        )

    if "ДИАЛОГ:" not in task.solution_text:
        raise RuntimeError(
            "solution_text does not contain dialogue section."
        )

    if "USER:" not in task.solution_text:
        raise RuntimeError(
            "User question was not saved."
        )

    if "TUTOR:" not in task.solution_text:
        raise RuntimeError(
            "Tutor answer was not saved."
        )

    print()
    print("=" * 70)
    print("ALL PIPELINE TESTS PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()
