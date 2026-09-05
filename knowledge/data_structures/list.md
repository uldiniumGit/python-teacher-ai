# List

## Definition

`list` — это встроенный изменяемый тип данных Python, предназначенный для хранения упорядоченной последовательности объектов.

Список может содержать любое количество элементов, в том числе элементы разных типов.

```python
numbers = [1, 2, 3]
mixed = [10, "Python", True, None]
```

Элементы списка имеют определенный порядок и доступны по индексам.

Списки являются изменяемыми (`mutable`), поэтому их содержимое можно изменять после создания.

---

## Purpose

Списки используются для:

* хранения нескольких объектов в одной структуре;
* хранения упорядоченных последовательностей данных;
* последовательного перебора элементов;
* добавления и удаления элементов;
* изменения существующих элементов;
* сортировки и обработки данных;
* хранения результатов вычислений;
* создания вложенных структур данных.

Список является одним из основных контейнеров Python и часто используется в качестве базовой структуры для работы с коллекциями данных.

---

## Core Concepts

### Creating a List

Список создается с помощью квадратных скобок `[]`.

```python
numbers = [1, 2, 3]
names = ["Alice", "Bob", "Charlie"]
```

Пустой список создается следующим образом:

```python
items = []
```

Также список можно создать с помощью конструктора `list()`:

```python
numbers = list()
```

---

### List Elements

Список может содержать элементы разных типов.

```python
items = [10, "Python", True, 3.14]
```

Элементы могут также быть другими коллекциями:

```python
data = [
    [1, 2],
    [3, 4],
]
```

Один список может содержать элементы разных типов, поскольку в Python список хранит ссылки на объекты.

---

### Indexing

Каждый элемент списка имеет индекс.

Индексация начинается с `0`.

```python
numbers = [10, 20, 30]

print(numbers[0])
print(numbers[1])
print(numbers[2])
```

Результат:

```text
10
20
30
```

Для доступа к элементам с конца списка используются отрицательные индексы.

```python
numbers = [10, 20, 30]

print(numbers[-1])
print(numbers[-2])
```

Результат:

```text
30
20
```

Индекс `-1` обозначает последний элемент.

---

### Slicing

Срез позволяет получить часть списка.

Основной синтаксис:

```python
list[start:stop:step]
```

`stop` не включается в результат.

```python
numbers = [0, 1, 2, 3, 4]

print(numbers[1:4])
```

Результат:

```text
[1, 2, 3]
```

Можно использовать отрицательный шаг:

```python
numbers = [0, 1, 2, 3, 4]

print(numbers[::-1])
```

Результат:

```text
[4, 3, 2, 1, 0]
```

Срез создает новый список.

---

### Mutability

Списки являются изменяемыми объектами.

Это означает, что существующий список можно изменить после создания.

```python
numbers = [1, 2, 3]

numbers[0] = 10

print(numbers)
```

Результат:

```text
[10, 2, 3]
```

Изменение элемента не создает новый список.

---

### Adding Elements

Для добавления элементов используются несколько методов.

#### `append()`

`append()` добавляет один объект в конец списка.

```python
numbers = [1, 2]

numbers.append(3)

print(numbers)
```

Результат:

```text
[1, 2, 3]
```

Если передать список в `append()`, сам список будет добавлен как один элемент:

```python
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)
```

Результат:

```text
[1, 2, [3, 4]]
```

#### `extend()`

`extend()` добавляет элементы из итерируемого объекта в конец списка.

```python
numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)
```

Результат:

```text
[1, 2, 3, 4]
```

В отличие от `append()`, `extend()` добавляет элементы переданного итерируемого объекта по отдельности.

#### `insert()`

`insert()` вставляет объект в указанную позицию.

```python
numbers = [1, 3]

numbers.insert(1, 2)

print(numbers)
```

Результат:

```text
[1, 2, 3]
```

---

### Removing Elements

Для удаления элементов используются разные методы.

#### `remove()`

`remove()` удаляет первое найденное в списке значение, равное переданному объекту.

```python
numbers = [1, 2, 2, 3]

numbers.remove(2)

print(numbers)
```

Результат:

```text
[1, 2, 3]
```

Если значение отсутствует, возникает `ValueError`.

#### `pop()`

`pop()` удаляет элемент по индексу и возвращает удаленный элемент.

```python
numbers = [10, 20, 30]

value = numbers.pop(1)

print(value)
print(numbers)
```

Результат:

```text
20
[10, 30]
```

Если индекс не указан, `pop()` удаляет и возвращает последний элемент.

```python
numbers = [10, 20, 30]

value = numbers.pop()

print(value)
```

Результат:

```text
30
```

#### `clear()`

`clear()` удаляет все элементы списка.

```python
numbers = [1, 2, 3]

numbers.clear()

print(numbers)
```

Результат:

```text
[]
```

---

### Finding Elements

Оператор `in` проверяет наличие элемента в списке.

```python
numbers = [1, 2, 3]

print(2 in numbers)
print(5 in numbers)
```

Результат:

```text
True
False
```

Оператор `not in` проверяет отсутствие элемента.

```python
print(5 not in numbers)
```

---

### `index()`

Метод `index()` возвращает индекс первого элемента, равного указанному значению.

```python
numbers = [10, 20, 30, 20]

print(numbers.index(20))
```

Результат:

```text
1
```

Если значение не найдено, возникает `ValueError`.

Можно ограничить область поиска:

```python
numbers = [10, 20, 30, 20]

print(numbers.index(20, 2))
```

Результат:

```text
3
```

---

### `count()`

Метод `count()` возвращает количество элементов, равных указанному значению.

```python
numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))
```

Результат:

```text
3
```

---

### List Length

Функция `len()` возвращает количество элементов списка.

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Результат:

```text
3
```

Для пустого списка:

```python
items = []

print(len(items))
```

Результат:

```text
0
```

---

### Iterating Over a List

Список можно перебирать с помощью `for`.

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Если одновременно нужен индекс, можно использовать `enumerate()`:

```python
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(index, name)
```

---

### List Concatenation

Списки можно объединять с помощью оператора `+`.

```python
first = [1, 2]
second = [3, 4]

result = first + second

print(result)
```

Результат:

```text
[1, 2, 3, 4]
```

Оператор `+` создает новый список.

---

### List Repetition

Список можно повторить с помощью оператора `*`.

```python
numbers = [1, 2]

result = numbers * 3

print(result)
```

Результат:

```text
[1, 2, 1, 2, 1, 2]
```

При повторении элементы не копируются глубоко. Для изменяемых вложенных объектов это может иметь важные последствия.

---

### Sorting

Список можно отсортировать с помощью метода `sort()`.

```python
numbers = [3, 1, 2]

numbers.sort()

print(numbers)
```

Результат:

```text
[1, 2, 3]
```

`sort()` изменяет существующий список.

Для сортировки в обратном порядке:

```python
numbers = [3, 1, 2]

numbers.sort(reverse=True)

print(numbers)
```

Функция `sorted()` отличается тем, что возвращает новый отсортированный список, не изменяя исходный.

```python
numbers = [3, 1, 2]

result = sorted(numbers)

print(numbers)
print(result)
```

---

### `reverse()`

Метод `reverse()` изменяет порядок элементов списка на обратный.

```python
numbers = [1, 2, 3]

numbers.reverse()

print(numbers)
```

Результат:

```text
[3, 2, 1]
```

`reverse()` изменяет существующий список и возвращает `None`.

---

### List Comprehensions

List comprehension позволяет создавать новый список на основе итерируемого объекта.

```python
numbers = [1, 2, 3, 4]

squares = [number * number for number in numbers]

print(squares)
```

Результат:

```text
[1, 4, 9, 16]
```

Можно добавить условие:

```python
numbers = [1, 2, 3, 4, 5]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

Результат:

```text
[2, 4]
```

List comprehension создает новый список.

---

### Nested Lists

Список может содержать другие списки.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
```

Доступ к вложенному элементу выполняется с использованием нескольких индексов:

```python
print(matrix[0][1])
```

Результат:

```text
2
```

---

### Copying Lists

Присваивание списка другой переменной не создает копию.

```python
first = [1, 2, 3]
second = first

second.append(4)

print(first)
print(second)
```

Результат:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Обе переменные ссылаются на один объект.

Для поверхностной копии можно использовать:

```python
second = first.copy()
```

или:

```python
second = first[:]
```

Также можно использовать `list(first)`.

---

### Shallow Copy

Методы `copy()`, `list()` и срез `[:]` создают поверхностную копию.

Вложенные изменяемые объекты при этом не копируются.

```python
first = [[1, 2], [3, 4]]
second = first.copy()

second[0].append(5)

print(first)
print(second)
```

Результат:

```text
[[1, 2, 5], [3, 4]]
[[1, 2, 5], [3, 4]]
```

Для независимого копирования вложенных объектов может использоваться `copy.deepcopy()`.

---

### List Comparison

Списки можно сравнивать с помощью операторов сравнения.

```python
first = [1, 2, 3]
second = [1, 2, 3]

print(first == second)
```

Результат:

```text
True
```

Списки сравниваются лексикографически, то есть элементы сравниваются последовательно.

```python
print([1, 2] < [1, 3])
```

Результат:

```text
True
```

---

## Syntax

### Creating a List

```python
items = []
items = [item1, item2, item3]
items = list(iterable)
```

### Indexing

```python
items[index]
items[-1]
```

### Slicing

```python
items[start:stop]
items[start:stop:step]
```

### Changing an Element

```python
items[index] = value
```

### Adding Elements

```python
items.append(value)
items.extend(iterable)
items.insert(index, value)
```

### Removing Elements

```python
items.remove(value)
items.pop()
items.pop(index)
items.clear()
```

### Searching

```python
value in items
value not in items

items.index(value)
items.count(value)
```

### Length

```python
len(items)
```

### Sorting

```python
items.sort()
items.sort(reverse=True)

sorted_items = sorted(items)
```

### Reversing

```python
items.reverse()
```

### Copying

```python
copy = items.copy()
copy = items[:]
copy = list(items)
```

### List Comprehension

```python
result = [expression for item in iterable]
```

С условием:

```python
result = [expression for item in iterable if condition]
```

---

## Rules

1. `list` является изменяемым типом данных.
2. Список сохраняет порядок элементов.
3. Индексация списка начинается с `0`.
4. Отрицательные индексы позволяют обращаться к элементам с конца.
5. Срез имеет форму `start:stop:step`.
6. Значение `stop` в срезе не включается.
7. Срез списка создает новый список.
8. `append()` добавляет один объект в конец списка.
9. `extend()` добавляет элементы из итерируемого объекта.
10. `append()` и `extend()` имеют разное поведение при передаче списка.
11. `insert()` вставляет объект в указанную позицию.
12. `remove()` удаляет первое совпадающее значение.
13. `remove()` вызывает `ValueError`, если значение не найдено.
14. `pop()` удаляет элемент и возвращает его.
15. `pop()` без индекса удаляет последний элемент.
16. `pop()` с недопустимым индексом вызывает `IndexError`.
17. `clear()` удаляет все элементы списка.
18. `len()` возвращает количество элементов.
19. `in` проверяет наличие элемента в списке.
20. `index()` возвращает индекс первого совпадения.
21. `count()` возвращает количество совпадающих элементов.
22. `sort()` изменяет исходный список.
23. `sorted()` возвращает новый отсортированный список.
24. `reverse()` изменяет порядок элементов исходного списка.
25. `reverse()` возвращает `None`.
26. `+` создает новый объединенный список.
27. `*` повторяет элементы списка.
28. Присваивание списка другой переменной не создает копию.
29. `copy()` создает поверхностную копию списка.
30. Срез `[:]` также создает поверхностную копию.
31. Вложенные изменяемые объекты не копируются при поверхностном копировании.
32. List comprehension создает новый список.
33. Списки могут содержать элементы разных типов.
34. Списки могут содержать другие списки.
35. При изменении списка во время итерации можно получить неожиданные результаты.
36. Для получения индекса и значения при итерации рекомендуется использовать `enumerate()`.

---

## Examples

### Example 1 — Creating and Accessing a List

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[-1])
```

Explanation:

Первый элемент имеет индекс `0`, последний можно получить с помощью `-1`.

---

### Example 2 — Changing an Element

```python
numbers = [1, 2, 3]

numbers[1] = 20

print(numbers)
```

Результат:

```text
[1, 20, 3]
```

Explanation:

Список изменяемый, поэтому существующий элемент можно заменить.

---

### Example 3 — Adding Elements

```python
numbers = [1, 2]

numbers.append(3)
numbers.extend([4, 5])
numbers.insert(0, 0)

print(numbers)
```

Результат:

```text
[0, 1, 2, 3, 4, 5]
```

Explanation:

Использованы три разных способа изменения списка.

---

### Example 4 — Removing Elements

```python
numbers = [10, 20, 30, 40]

numbers.remove(20)

last = numbers.pop()

print(numbers)
print(last)
```

Результат:

```text
[10, 30]
40
```

Explanation:

`remove()` удаляет значение, а `pop()` удаляет элемент и возвращает его.

---

### Example 5 — Slicing

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
print(numbers[::2])
print(numbers[::-1])
```

Результат:

```text
[1, 2, 3]
[0, 2, 4]
[5, 4, 3, 2, 1, 0]
```

Explanation:

Срезы позволяют получать части списка с заданным диапазоном и шагом.

---

### Example 6 — Searching

```python
numbers = [10, 20, 30, 20]

if 20 in numbers:
    print(numbers.index(20))

print(numbers.count(20))
```

Результат:

```text
1
2
```

Explanation:

`in` проверяет наличие значения, `index()` находит первое совпадение, а `count()` считает все совпадения.

---

### Example 7 — Iteration

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)
```

Explanation:

`for` последовательно перебирает элементы списка.

---

### Example 8 — `enumerate()`

```python
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names, start=1):
    print(index, name)
```

Результат:

```text
1 Alice
2 Bob
3 Charlie
```

Explanation:

`enumerate()` предоставляет индекс и значение элемента.

---

### Example 9 — Sorting

```python
numbers = [5, 2, 4, 1, 3]

numbers.sort()

print(numbers)
```

Результат:

```text
[1, 2, 3, 4, 5]
```

Explanation:

`sort()` изменяет исходный список.

---

### Example 10 — `sorted()`

```python
numbers = [5, 2, 4, 1, 3]

sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)
```

Результат:

```text
[5, 2, 4, 1, 3]
[1, 2, 3, 4, 5]
```

Explanation:

`sorted()` создает новый отсортированный список и оставляет исходный без изменений.

---

### Example 11 — List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

Результат:

```text
[1, 4, 9, 16, 25]
```

Explanation:

List comprehension создает новый список на основе существующего итерируемого объекта.

---

### Example 12 — List Comprehension with Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

Результат:

```text
[2, 4, 6]
```

Explanation:

В новый список попадают только элементы, удовлетворяющие условию.

---

### Example 13 — Nested Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

print(matrix[1][2])
```

Результат:

```text
6
```

Explanation:

Первый индекс выбирает вложенный список, второй — элемент внутри него.

---

### Example 14 — Copying a List

```python
original = [1, 2, 3]

copy = original.copy()

copy.append(4)

print(original)
print(copy)
```

Результат:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

Explanation:

`copy()` создает отдельный список верхнего уровня.

---

### Example 15 — Shallow Copy

```python
original = [[1, 2], [3, 4]]

copy = original.copy()

copy[0].append(5)

print(original)
print(copy)
```

Результат:

```text
[[1, 2, 5], [3, 4]]
[[1, 2, 5], [3, 4]]
```

Explanation:

Внутренний список не был скопирован. Обе структуры содержат ссылку на один вложенный список.

---

### Example 16 — List Concatenation

```python
first = [1, 2]
second = [3, 4]

result = first + second

print(result)
```

Результат:

```text
[1, 2, 3, 4]
```

Explanation:

Оператор `+` создает новый список.

---

## Edge Cases

### Empty List

Пустой список не содержит элементов.

```python
items = []

print(len(items))
print(items)
```

Результат:

```text
0
[]
```

При проверке в условии пустой список имеет ложное значение:

```python
if not items:
    print("List is empty")
```

---

### Index Out of Range

Попытка обратиться к несуществующему индексу вызывает `IndexError`.

```python
numbers = [1, 2, 3]

print(numbers[5])
```

Индекс `5` отсутствует.

---

### Negative Index Out of Range

Отрицательные индексы также имеют ограничения.

```python
numbers = [1, 2, 3]

print(numbers[-4])
```

Возникает `IndexError`, потому что допустимые отрицательные индексы — `-1`, `-2` и `-3`.

---

### Empty List and `pop()`

Вызов `pop()` для пустого списка вызывает `IndexError`.

```python
items = []

items.pop()
```

---

### Empty List and `remove()`

`remove()` для пустого списка вызывает `ValueError`.

```python
items = []

items.remove(1)
```

---

### Empty Slice

Срез может вернуть пустой список.

```python
numbers = [1, 2, 3]

result = numbers[5:10]

print(result)
```

Результат:

```text
[]
```

В отличие от прямого обращения по индексу, такой срез не вызывает `IndexError`.

---

### `append()` with a List

`append()` добавляет переданный список как один элемент.

```python
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)
```

Результат:

```text
[1, 2, [3, 4]]
```

Для добавления отдельных элементов используется `extend()`.

---

### `extend()` with a String

`extend()` принимает любой итерируемый объект.

Поэтому передача строки добавляет ее символы по отдельности:

```python
letters = ["a"]

letters.extend("bc")

print(letters)
```

Результат:

```text
["a", "b", "c"]
```

---

### List Repetition with Mutable Objects

Повторение списка не создает независимые копии вложенного изменяемого объекта.

Проблемный пример:

```python
rows = [[0] * 3] * 3

rows[0][0] = 1

print(rows)
```

Результат:

```text
[[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```

Все три элемента верхнего списка ссылаются на один и тот же внутренний список.

Для независимых вложенных списков можно использовать comprehension:

```python
rows = [[0] * 3 for _ in range(3)]

rows[0][0] = 1

print(rows)
```

Результат:

```text
[[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

### Aliasing

Две переменные могут ссылаться на один список.

```python
first = [1, 2, 3]
second = first

second.append(4)

print(first)
```

Результат:

```text
[1, 2, 3, 4]
```

Изменение через `second` изменяет тот же объект, на который ссылается `first`.

---

### Modifying a List During Iteration

Изменение списка непосредственно во время его обхода может привести к неожиданному поведению.

Проблемный пример:

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)
```

Удаление элементов изменяет структуру списка во время итерации.

Безопаснее создавать новый список:

```python
numbers = [1, 2, 3, 4, 5]

numbers = [
    number
    for number in numbers
    if number % 2 != 0
]
```

---

### Mixed Types

Список может содержать разные типы:

```python
items = [1, "Python", True, None]
```

Однако не все операции между такими элементами допустимы.

Например, сортировка списка с несовместимыми типами может вызвать `TypeError`:

```python
items = [1, "Python", 3]

items.sort()
```

---

### `sort()` and `None`

Методы, изменяющие список на месте, обычно возвращают `None`.

Например:

```python
numbers = [3, 1, 2]

result = numbers.sort()

print(result)
```

Результат:

```text
None
```

Нельзя использовать `result` как отсортированный список.

---

## Common Mistakes

### Mistake 1 — Confusing `append()` and `extend()`

Неправильно ожидать, что:

```python
numbers = [1, 2]

numbers.append([3, 4])
```

даст:

```text
[1, 2, 3, 4]
```

Фактически:

```text
[1, 2, [3, 4]]
```

Для добавления отдельных элементов используется:

```python
numbers.extend([3, 4])
```

---

### Mistake 2 — Assuming List Assignment Creates a Copy

Неправильно:

```python
first = [1, 2, 3]
second = first

second.append(4)
```

`first` и `second` ссылаются на один список.

Для поверхностной копии:

```python
second = first.copy()
```

---

### Mistake 3 — Confusing `sort()` and `sorted()`

`sort()` изменяет исходный список:

```python
numbers.sort()
```

`sorted()` возвращает новый список:

```python
result = sorted(numbers)
```

---

### Mistake 4 — Expecting `sort()` to Return the Sorted List

Неправильно:

```python
numbers = [3, 1, 2]

sorted_numbers = numbers.sort()
```

`sorted_numbers` будет равен `None`.

Правильно:

```python
sorted_numbers = sorted(numbers)
```

или:

```python
numbers.sort()
```

---

### Mistake 5 — Using an Invalid Index

```python
numbers = [1, 2, 3]

print(numbers[3])
```

Последний индекс равен `2`, поэтому возникает `IndexError`.

---

### Mistake 6 — Confusing `remove()` and `pop()`

`remove(value)` удаляет первое совпадение по значению.

```python
numbers.remove(20)
```

`pop(index)` удаляет элемент по индексу и возвращает его.

```python
value = numbers.pop(1)
```

---

### Mistake 7 — Modifying a List While Iterating

Удаление или добавление элементов во время обхода списка может привести к пропуску элементов или другим неожиданным результатам.

Часто лучше создать новый список с помощью list comprehension.

---

### Mistake 8 — Incorrect Nested List Creation

Неправильно:

```python
matrix = [[0] * 3] * 3
```

Внутренние списки являются одним и тем же объектом.

Для независимых строк:

```python
matrix = [[0] * 3 for _ in range(3)]
```

---

### Mistake 9 — Confusing `copy()` with Deep Copy

`copy()` создает поверхностную копию.

Если список содержит вложенные изменяемые объекты, они остаются общими.

Для полного независимого копирования вложенной структуры может использоваться `copy.deepcopy()`.

---

### Mistake 10 — Assuming Slicing Raises `IndexError`

Прямой доступ:

```python
numbers[100]
```

вызывает `IndexError`.

Но срез:

```python
numbers[100:200]
```

может просто вернуть:

```text
[]
```

---

## Related Concepts

* Variables
* Data Types
* Loops
* Tuples
* Sets
* Dictionaries
* Strings
* Iterables
* Iterators
* List Comprehensions
* Slicing
* `enumerate()`
* `sorted()`
* `copy`
* `copy.deepcopy()`

---

## Key Takeaways

* `list` — встроенный изменяемый упорядоченный контейнер Python.
* Списки создаются с помощью `[]` или `list()`.
* Индексация начинается с `0`.
* Отрицательные индексы позволяют обращаться к элементам с конца.
* Срезы позволяют получать части списка и создают новый список.
* Список можно изменять после создания.
* `append()` добавляет один объект.
* `extend()` добавляет элементы итерируемого объекта.
* `insert()` вставляет объект в указанную позицию.
* `remove()` удаляет первое совпадение по значению.
* `pop()` удаляет и возвращает элемент.
* `clear()` удаляет все элементы.
* `index()` находит первое совпадение.
* `count()` подсчитывает количество совпадений.
* `sort()` сортирует список на месте.
* `sorted()` возвращает новый отсортированный список.
* `reverse()` изменяет порядок элементов на месте.
* List comprehension создает новый список на основе итерируемого объекта.
* Присваивание списка другой переменной не создает копию.
* `copy()` создает поверхностную копию.
* Вложенные изменяемые объекты требуют осторожности при копировании.
* Списки могут содержать объекты разных типов и другие списки.
* Не следует без необходимости изменять список во время его итерации.
* `append()` и `extend()` особенно важно различать при работе с вложенными данными.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Data model — Objects, values and types
* Python Standard Library — Built-in Types — `list`
* Python Standard Library — Common Sequence Operations
* Python Standard Library — Mutable Sequence Types
* Python 3.14 Tutorial — Lists
* Python 3.14 Tutorial — Data Structures
* Python 3.14 Tutorial — List Comprehensions
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html
* Official documentation: https://docs.python.org/3.14/library/stdtypes.html#list
* Official documentation: https://docs.python.org/3.14/library/stdtypes.html#common-sequence-operations
* Official documentation: https://docs.python.org/3.14/library/stdtypes.html#mutable-sequence-types
* Official documentation: https://docs.python.org/3.14/tutorial/introduction.html#lists
* Official documentation: https://docs.python.org/3.14/tutorial/datastructures.html
* Official documentation: https://docs.python.org/3.14/tutorial/datastructures.html#list-comprehensions
