# tests/test_task_generator.py
from ai.task_generator import generate_task


def main():
    topic = "list"
    difficulty = "beginner"

    context = """
    # List
    
    ## Definition
    
    List — изменяемая последовательность объектов в Python.
    Списки поддерживают индексацию, срезы, добавление и удаление элементов.
    
    ## Syntax
    
    ```python
    numbers = [1, 2, 3]
    numbers.append(4)
        Rules
    
        Список может содержать объекты разных типов.
        Списки являются изменяемыми.
    """

    task = generate_task(
        topic=topic,
        difficulty=difficulty,
        context=context,
    )

    print("\n=== GENERATED TASK ===\n")
    print(task)


if __name__ == "__main__":
    main()
