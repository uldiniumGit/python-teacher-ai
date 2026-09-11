# tests/test_task_checker.py
from pprint import pprint

from ai.task_checker import check_solution


def main():
    task = """
    Создай список numbers со значениями 1, 2 и 3.
    Добавь в конец списка число 4.
    Выведи получившийся список.
    """

    solution = """
    numbers = [1, 2, 3]
    numbers.append(4)
    print(numbers)
    """

    context = """
    # List
    
    ## Definition
    
    List — изменяемая последовательность объектов в Python.
    
    ## Syntax
    
    ```python
    numbers = [1, 2, 3]
    numbers.append(4)
    Rules

    Метод append() добавляет один объект в конец списка.
    """

    result = check_solution(
        task=task,
        solution=solution,
        context=context,
    )

    print("\n=== CHECK RESULT ===\n")
    pprint(result)


if __name__ == "__main__":
    main()
