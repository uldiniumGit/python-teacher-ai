# Set

## Definition

Множество (`set`) — это встроенный изменяемый тип данных Python, предназначенный для хранения уникальных элементов.

Множество не хранит дубликаты элементов и не поддерживает доступ к элементам по числовому индексу.

```python
numbers = {1, 2, 3, 4}
```

Если при создании множества указать одинаковые элементы несколько раз, дубликаты будут удалены:

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
```

Результат:

```python
{1, 2, 3}
```

Элементы множества должны быть хешируемыми.

---

## Purpose

Множества используются для хранения уникальных элементов и выполнения операций над коллекциями.

Они особенно полезны, когда необходимо:

* удалить дубликаты;
* быстро проверить наличие элемента;
* найти общие элементы двух коллекций;
* найти элементы, присутствующие только в одной коллекции;
* определить, является ли одна коллекция подмножеством другой;
* выполнить операции объединения, пересечения и разности.

Например, из списка можно быстро получить уникальные значения:

```python
numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)
```

Результат:

```python
{1, 2, 3, 4}
```

---

## Core Concepts

### Unique Elements

Основное свойство множества — каждый элемент хранится только один раз.

```python
numbers = {1, 2, 2, 3, 3}

print(numbers)
```

Результат:

```python
{1, 2, 3}
```

Множество автоматически устраняет повторяющиеся элементы.

Это делает `set` удобным для удаления дубликатов из последовательности:

```python
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]

unique_names = set(names)

print(unique_names)
```

---

### Creating Sets

Множество можно создать с помощью фигурных скобок:

```python
numbers = {1, 2, 3}
```

Однако пустые фигурные скобки создают словарь, а не множество:

```python
empty = {}

print(type(empty))
```

Результат:

```text
<class 'dict'>
```

Для создания пустого множества используется `set()`:

```python
empty = set()
```

Множество также можно создать из любого итерируемого объекта:

```python
numbers = set([1, 2, 2, 3])
```

Результат:

```python
{1, 2, 3}
```

---

### Hashable Elements

Элементы множества должны быть хешируемыми.

Например, числа и строки можно использовать как элементы множества:

```python
data = {1, 2, 3, "Python"}
```

Кортеж также может быть элементом множества, если все его элементы хешируемы:

```python
data = {
    (1, 2),
    (3, 4)
}
```

Изменяемые объекты, такие как списки и словари, нельзя добавлять в множество:

```python
# TypeError
data = {
    [1, 2]
}
```

---

### Adding Elements

Метод `add()` добавляет один элемент в множество:

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

Если элемент уже существует, множество не изменяется:

```python
numbers.add(4)
```

После повторного добавления второго `4` не появится.

---

### Removing Elements

Метод `remove()` удаляет указанный элемент:

```python
numbers = {1, 2, 3}

numbers.remove(2)

print(numbers)
```

Если элемента нет, `remove()` вызывает `KeyError`.

Метод `discard()` также удаляет элемент, но не вызывает ошибку, если элемента нет:

```python
numbers.discard(5)
```

Метод `pop()` удаляет и возвращает некоторый элемент множества:

```python
numbers = {1, 2, 3}

value = numbers.pop()

print(value)
print(numbers)
```

Поскольку множество не предоставляет индексов, нельзя указать, какой именно элемент должен быть удалён с помощью `pop()`.

---

### `clear()`

Метод `clear()` удаляет все элементы множества:

```python
numbers = {1, 2, 3}

numbers.clear()

print(numbers)
```

Результат:

```python
set()
```

---

### Membership Testing

Оператор `in` позволяет проверить наличие элемента в множестве:

```python
numbers = {1, 2, 3}

print(2 in numbers)
print(5 in numbers)
```

Результат:

```text
True
False
```

Проверка принадлежности является одной из основных причин использовать множество.

---

### Union

Объединение (`union`) возвращает множество, содержащее элементы обоих множеств.

Можно использовать оператор `|`:

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a | b

print(result)
```

Результат:

```python
{1, 2, 3, 4, 5}
```

Также используется метод `union()`:

```python
result = a.union(b)
```

Повторяющиеся элементы автоматически объединяются в один элемент.

---

### Intersection

Пересечение (`intersection`) возвращает элементы, которые присутствуют в обоих множествах.

Используется оператор `&`:

```python
a = {1, 2, 3}
b = {2, 3, 4}

result = a & b

print(result)
```

Результат:

```python
{2, 3}
```

Также существует метод `intersection()`:

```python
result = a.intersection(b)
```

---

### Difference

Разность (`difference`) возвращает элементы, которые находятся в первом множестве, но отсутствуют во втором.

Используется оператор `-`:

```python
a = {1, 2, 3}
b = {2, 3, 4}

result = a - b

print(result)
```

Результат:

```python
{1}
```

Обратная операция:

```python
result = b - a
```

даст:

```python
{4}
```

---

### Symmetric Difference

Симметричная разность (`symmetric difference`) возвращает элементы, которые находятся только в одном из двух множеств.

Используется оператор `^`:

```python
a = {1, 2, 3}
b = {2, 3, 4}

result = a ^ b

print(result)
```

Результат:

```python
{1, 4}
```

Также можно использовать метод `symmetric_difference()`.

---

### Subset

Множество `A` является подмножеством (`subset`) множества `B`, если каждый элемент `A` также присутствует в `B`.

Используется оператор `<=`:

```python
a = {1, 2}
b = {1, 2, 3}

print(a <= b)
```

Результат:

```text
True
```

Метод `issubset()` выполняет ту же проверку:

```python
print(a.issubset(b))
```

---

### Proper Subset

Оператор `<` проверяет, является ли множество строгим подмножеством другого множества.

```python
a = {1, 2}
b = {1, 2, 3}

print(a < b)
```

Результат:

```text
True
```

Если множества равны, `<` возвращает `False`.

---

### Superset

Множество `A` является надмножеством (`superset`) множества `B`, если оно содержит все элементы `B`.

Используется оператор `>=`:

```python
a = {1, 2, 3}
b = {1, 2}

print(a >= b)
```

Результат:

```text
True
```

Также используется метод `issuperset()`:

```python
print(a.issuperset(b))
```

---

### Disjoint Sets

Два множества являются непересекающимися (`disjoint`), если у них нет общих элементов.

Для проверки используется `isdisjoint()`:

```python
a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))
```

Результат:

```text
True
```

Если хотя бы один элемент является общим, результат будет `False`.

---

### Iteration

Множество можно перебирать с помощью цикла `for`:

```python
numbers = {1, 2, 3}

for number in numbers:
    print(number)
```

При этом порядок элементов не следует воспринимать как фиксированный порядок последовательности.

Множества не поддерживают индексирование:

```python
numbers = {1, 2, 3}

# TypeError
print(numbers[0])
```

---

### `frozenset`

`frozenset` — это неизменяемый вариант множества.

```python
numbers = frozenset([1, 2, 3])
```

В отличие от обычного `set`, `frozenset` нельзя изменять после создания.

Например, у него нет операции `add()`:

```python
numbers.add(4)
```

Это вызывает `AttributeError`.

Поскольку `frozenset` является неизменяемым и хешируемым объектом, его можно использовать в качестве элемента другого множества или ключа словаря.

---

## Syntax

Создание множества:

```python
numbers = {1, 2, 3}
```

Создание пустого множества:

```python
numbers = set()
```

Создание из итерируемого объекта:

```python
numbers = set(iterable)
```

Добавление элемента:

```python
numbers.add(value)
```

Удаление элемента:

```python
numbers.remove(value)
```

Безопасное удаление:

```python
numbers.discard(value)
```

Удаление и получение элемента:

```python
value = numbers.pop()
```

Удаление всех элементов:

```python
numbers.clear()
```

Проверка наличия элемента:

```python
if value in numbers:
    ...
```

Объединение:

```python
result = a | b
result = a.union(b)
```

Пересечение:

```python
result = a & b
result = a.intersection(b)
```

Разность:

```python
result = a - b
result = a.difference(b)
```

Симметричная разность:

```python
result = a ^ b
result = a.symmetric_difference(b)
```

Проверка подмножества:

```python
result = a <= b
result = a.issubset(b)
```

Проверка строгого подмножества:

```python
result = a < b
```

Проверка надмножества:

```python
result = a >= b
result = a.issuperset(b)
```

Проверка отсутствия общих элементов:

```python
result = a.isdisjoint(b)
```

---

## Rules

1. `set` хранит уникальные элементы.
2. Дубликаты автоматически удаляются.
3. Множество является изменяемым типом данных.
4. Элементы множества должны быть хешируемыми.
5. Списки и словари нельзя использовать как элементы множества.
6. Множество не поддерживает индексирование.
7. Пустое множество создаётся с помощью `set()`, а не `{}`.
8. Оператор `in` используется для проверки наличия элемента.
9. `add()` добавляет один элемент.
10. `remove()` удаляет элемент и вызывает `KeyError`, если его нет.
11. `discard()` удаляет элемент без ошибки, если его нет.
12. `pop()` удаляет и возвращает некоторый элемент множества.
13. `clear()` удаляет все элементы.
14. `|` выполняет объединение множеств.
15. `&` выполняет пересечение множеств.
16. `-` выполняет разность множеств.
17. `^` выполняет симметричную разность множеств.
18. `<=` проверяет отношение подмножества.
19. `>=` проверяет отношение надмножества.
20. `isdisjoint()` проверяет отсутствие общих элементов.
21. Множество не следует использовать там, где требуется сохранение порядка элементов.
22. `frozenset` является неизменяемым вариантом множества.

---

## Examples

### Example 1 — Removing Duplicates

```python
numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)
```

Explanation:

Преобразование списка в множество удаляет повторяющиеся элементы.

---

### Example 2 — Membership Testing

```python
languages = {"Python", "Java", "Go"}

if "Python" in languages:
    print("Python is available")
```

Explanation:

Оператор `in` проверяет наличие элемента в множестве.

---

### Example 3 — Adding and Removing Elements

```python
numbers = {1, 2, 3}

numbers.add(4)
numbers.remove(2)

print(numbers)
```

Explanation:

`add()` добавляет новый элемент, а `remove()` удаляет существующий.

---

### Example 4 — Union

```python
frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "Java", "JavaScript"}

all_languages = frontend | backend

print(all_languages)
```

Explanation:

Объединение содержит элементы обоих множеств. Общий элемент `"JavaScript"` появляется только один раз.

---

### Example 5 — Intersection

```python
python_students = {"Alice", "Bob", "Charlie"}
sql_students = {"Bob", "Charlie", "David"}

both = python_students & sql_students

print(both)
```

Explanation:

Пересечение содержит пользователей, которые находятся в обоих множествах.

---

### Example 6 — Difference

```python
python_students = {"Alice", "Bob", "Charlie"}
sql_students = {"Bob", "Charlie", "David"}

only_python = python_students - sql_students

print(only_python)
```

Explanation:

Результат содержит элементы, которые есть в первом множестве, но отсутствуют во втором.

---

### Example 7 — Symmetric Difference

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a ^ b

print(result)
```

Explanation:

Результат содержит элементы, которые принадлежат только одному из множеств.

---

### Example 8 — Subset

```python
required = {"Python", "SQL"}
skills = {"Python", "SQL", "Docker", "Git"}

print(required <= skills)
```

Explanation:

`required` является подмножеством `skills`, потому что все необходимые навыки присутствуют в `skills`.

---

### Example 9 — Checking Disjoint Sets

```python
a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))
```

Explanation:

Множества не имеют общих элементов, поэтому результатом является `True`.

---

### Example 10 — `frozenset`

```python
numbers = frozenset([1, 2, 3])

print(numbers)
```

Explanation:

`frozenset` хранит уникальные элементы, но не позволяет изменять множество после создания.

---

## Edge Cases

### Empty Set

Пустой набор нельзя создать с помощью `{}`:

```python
empty = {}

print(type(empty))
```

Результат:

```text
<class 'dict'>
```

Для создания пустого множества необходимо использовать:

```python
empty = set()
```

---

### Duplicate Elements

Дубликаты автоматически удаляются:

```python
numbers = {1, 1, 2, 2, 3}

print(numbers)
```

Результат:

```python
{1, 2, 3}
```

---

### Unhashable Elements

Список нельзя использовать как элемент множества:

```python
numbers = {
    [1, 2]
}
```

Это вызывает `TypeError`.

Кортеж может быть элементом множества, если все его элементы хешируемы:

```python
numbers = {
    (1, 2)
}
```

---

### Nested Mutable Objects

Нельзя создать множество, содержащее изменяемый список:

```python
data = {
    [1, 2],
    [3, 4]
}
```

Для составных неизменяемых данных можно использовать кортежи:

```python
data = {
    (1, 2),
    (3, 4)
}
```

---

### Removing a Missing Element

`remove()` вызывает `KeyError`, если элемента нет:

```python
numbers = {1, 2, 3}

numbers.remove(10)
```

Если отсутствие элемента является допустимой ситуацией, используйте `discard()`:

```python
numbers.discard(10)
```

---

### Popping from a Set

`pop()` удаляет некоторый элемент множества:

```python
numbers = {1, 2, 3}

value = numbers.pop()
```

Не следует полагаться на то, какой именно элемент будет выбран.

---

### No Indexing

Множества не поддерживают обращение по индексу:

```python
numbers = {1, 2, 3}

print(numbers[0])
```

Это вызывает `TypeError`.

Если нужен конкретный элемент по позиции, следует использовать подходящую последовательность, например список.

---

### Empty Set and `pop()`

Вызов `pop()` для пустого множества вызывает `KeyError`:

```python
numbers = set()

numbers.pop()
```

---

### Set Operations with Different Types

Некоторые операции множеств могут выполняться с другими множественно-подобными итерируемыми объектами через методы.

Например:

```python
numbers = {1, 2, 3}

result = numbers.intersection([2, 3, 4])

print(result)
```

Результат:

```python
{2, 3}
```

При этом операторы `|`, `&`, `-` и `^` имеют более строгие требования к типам операндов.

---

## Common Mistakes

### Mistake 1 — Using `{}` for an Empty Set

Неправильно:

```python
numbers = {}
```

Это создаёт словарь.

Правильно:

```python
numbers = set()
```

---

### Mistake 2 — Trying to Access an Element by Index

Неправильно:

```python
numbers = {10, 20, 30}

print(numbers[0])
```

Множества не поддерживают индексирование.

Если нужен доступ по индексу, используйте список:

```python
numbers = [10, 20, 30]

print(numbers[0])
```

---

### Mistake 3 — Adding a List to a Set

Неправильно:

```python
numbers = set()

numbers.add([1, 2])
```

Список является нехешируемым объектом.

Если нужен неизменяемый составной элемент, можно использовать кортеж:

```python
numbers.add((1, 2))
```

---

### Mistake 4 — Using `remove()` When the Element May Be Missing

Неправильно:

```python
numbers = {1, 2, 3}

numbers.remove(10)
```

Это вызывает `KeyError`.

Если элемент может отсутствовать:

```python
numbers.discard(10)
```

---

### Mistake 5 — Expecting a Fixed Order

Не следует использовать множество, если логика программы зависит от позиции элементов.

Неправильно:

```python
numbers = {1, 2, 3}

# Не следует полагаться на конкретный порядок элементов
for number in numbers:
    print(number)
```

Если важен порядок, используйте последовательность, например список.

---

### Mistake 6 — Expecting `pop()` to Remove a Specific Element

Неправильно предполагать, что:

```python
numbers.pop()
```

удалит конкретное значение.

`pop()` не принимает индекс или значение элемента. Если необходимо удалить конкретный элемент, используйте `remove()` или `discard()`.

---

## Related Concepts

* `list` — упорядоченная изменяемая последовательность.
* `tuple` — упорядоченная неизменяемая последовательность.
* `dict` — изменяемое отображение «ключ — значение».
* `frozenset` — неизменяемое множество.
* Hashability — свойство объекта, необходимое для использования его в множестве.
* Membership testing — проверка наличия элемента с помощью `in`.
* Set operations — объединение, пересечение, разность и симметричная разность.
* Set comprehension — компактный способ создания множеств.
* `collections` — модуль со специализированными структурами данных.

---

## Key Takeaways

* `set` — встроенный тип Python для хранения уникальных элементов.
* Дубликаты автоматически удаляются.
* Элементы множества должны быть хешируемыми.
* Множество является изменяемым.
* Множества не поддерживают индексирование.
* Пустое множество создаётся через `set()`.
* `in` используется для проверки наличия элемента.
* `add()` добавляет элемент.
* `remove()` удаляет элемент и вызывает `KeyError`, если его нет.
* `discard()` удаляет элемент без ошибки, если его нет.
* `pop()` удаляет и возвращает некоторый элемент.
* `|` выполняет объединение.
* `&` выполняет пересечение.
* `-` выполняет разность.
* `^` выполняет симметричную разность.
* `<=` и `issubset()` проверяют подмножество.
* `>=` и `issuperset()` проверяют надмножество.
* `isdisjoint()` проверяет отсутствие общих элементов.
* `frozenset` является неизменяемой версией множества.
* Множества особенно полезны для удаления дубликатов и быстрых проверок принадлежности.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Data model — Sets
* Python Standard Library — Built-in Types — `set`
* Python Standard Library — Set Types — `set`, `frozenset`
* Python 3.14 Tutorial — Data Structures
* Python 3.14 Tutorial — Sets
* Official documentation: https://docs.python.org/3.14/library/stdtypes.html#set-types-set-frozenset
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html#sets
* Official documentation: https://docs.python.org/3.14/tutorial/datastructures.html#sets
