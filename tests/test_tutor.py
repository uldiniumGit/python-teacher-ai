# tests/test_tutor.py
from ai.tutor import chat_with_tutor


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

    feedback = """
    {
        "is_correct": true,
        "score": 10,
        "errors": [],
        "explanation": "Решение полностью соответствует условию.",
        "recommendations": []
    }
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

    history = [
        {
            "role": "user",
            "content": "Я использовал append().",
        },
        {
            "role": "assistant",
            "content": "Да, append() добавляет элемент в конец списка.",
        },
    ]

    question = "Почему после append() число 4 оказалось последним элементом?"

    answer = chat_with_tutor(
        task=task,
        solution=solution,
        feedback=feedback,
        context=context,
        history=history,
        question=question,
    )

    print("\n=== TUTOR ANSWER ===\n")
    print(answer)


if __name__ == "__main__":
    main()
