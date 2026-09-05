# Tuple

## Definition

Кортеж (`tuple`) — это упорядоченная неизменяемая последовательность объектов в Python.

Кортеж может содержать элементы разных типов, включая числа, строки, списки, словари, другие кортежи и объекты пользовательских классов.

В отличие от списка (`list`), после создания кортежа нельзя изменить, добавить или удалить его элементы.

---

## Purpose

Кортеж используется для хранения фиксированного набора значений, который не должен изменяться после создания.

Основные случаи применения:

* хранение связанных значений;
* возврат нескольких значений из функции;
* распаковка нескольких значений;
* использование последовательности в качестве ключа словаря, если все её элементы хешируемы;
* представление неизменяемых данных;
* передача нескольких значений как одной структуры данных.

Кортеж особенно полезен, когда структура данных должна оставаться неизменной.

---

## Core Concepts

Основные понятия, которые необходимо знать для работы с кортежами.

### Ordered Sequence

Кортеж является упорядоченной последовательностью. Каждый элемент имеет определённую позицию, которая определяется индексом.

Индексация начинается с `0`:

```python
numbers = (10, 20, 30)

print(numbers[0])  # 10
print(numbers[1])  # 20
print(numbers[2])  # 30
```

Порядок элементов сохраняется.

---

### Immutability

Кортеж является неизменяемым объектом.

После создания нельзя изменить отдельный элемент:

```python
numbers = (10, 20, 30)

numbers[0] = 100  # TypeError
```

Также нельзя добавить или удалить элемент из существующего кортежа.

Однако если кортеж содержит изменяемый объект, сам этот объект может быть изменён:

```python
data = ([1, 2], 10)

data[0].append(3)

print(data)
# ([1, 2, 3], 10)
```

Неизменяемость относится к структуре самого кортежа, а не обязательно к объектам, на которые он ссылается.

---

### Creating Tuples

Кортеж обычно создаётся с помощью круглых скобок:

```python
numbers = (1, 2, 3)
names = ("Alice", "Bob", "Charlie")
mixed = (10, "Python", True)
```

В Python круглые скобки не всегда обязательны. Кортеж определяется в первую очередь наличием запятых:

```python
numbers = 1, 2, 3

print(numbers)
# (1, 2, 3)
```

---

### Single-Element Tuple

Для создания кортежа с одним элементом обязательно нужна запятая.

Правильный вариант:

```python
number = (10,)
```

Без запятой это будет обычное значение в круглых скобках:

```python
number = (10)

print(type(number))
# <class 'int'>
```

С запятой:

```python
number = (10,)

print(type(number))
# <class 'tuple'>
```

---

### Empty Tuple

Пустой кортеж создаётся с помощью пустых круглых скобок:

```python
empty = ()

print(type(empty))
# <class 'tuple'>
```

Также можно использовать конструктор `tuple()`:

```python
empty = tuple()
```

---

### Indexing

Для получения элемента используется индекс:

```python
colors = ("red", "green", "blue")

print(colors[0])  # red
print(colors[1])  # green
print(colors[2])  # blue
```

Можно использовать отрицательные индексы:

```python
colors = ("red", "green", "blue")

print(colors[-1])  # blue
print(colors[-2])  # green
```

Если индекс выходит за пределы кортежа, возникает `IndexError`.

---

### Slicing

Срез позволяет получить часть кортежа.

Общий синтаксис:

```python
tuple[start:stop:step]
```

Пример:

```python
numbers = (0, 1, 2, 3, 4, 5)

print(numbers[1:4])
# (1, 2, 3)

print(numbers[:3])
# (0, 1, 2)

print(numbers[::2])
# (0, 2, 4)
```

Срез возвращает новый кортеж.

---

### Tuple Length

Количество элементов можно получить с помощью `len()`:

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
# 4
```

Для пустого кортежа:

```python
print(len(()))
# 0
```

---

### Tuple Methods

У кортежей есть два основных метода:

* `count()` — количество вхождений элемента;
* `index()` — индекс первого вхождения элемента.

Пример:

```python
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
# 3

print(numbers.index(2))
# 1
```

Если `index()` не находит указанный элемент, возникает `ValueError`.

---

### Membership Testing

Оператор `in` проверяет наличие элемента в кортеже:

```python
numbers = (10, 20, 30)

print(20 in numbers)
# True

print(50 in numbers)
# False
```

Оператор `not in` проверяет отсутствие элемента:

```python
print(50 not in numbers)
# True
```

---

### Iteration

Кортеж можно перебирать с помощью цикла `for`:

```python
numbers = (10, 20, 30)

for number in numbers:
    print(number)
```

Для получения индексов можно использовать `enumerate()`:

```python
colors = ("red", "green", "blue")

for index, color in enumerate(colors):
    print(index, color)
```

---

### Tuple Unpacking

Распаковка позволяет присвоить элементы кортежа отдельным переменным:

```python
person = ("Roman", 27)

name, age = person

print(name)
# Roman

print(age)
# 27
```

Количество переменных должно соответствовать количеству элементов, если не используется расширенная распаковка.

---

### Extended Unpacking

Оператор `*` позволяет собрать несколько элементов в одну переменную:

```python
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print(first)
# 1

print(middle)
# [2, 3, 4]

print(last)
# 5
```

Переменная с `*` получает список, а не кортеж.

---

### Nested Tuples

Кортеж может содержать другие кортежи:

```python
points = (
    (10, 20),
    (30, 40),
    (50, 60)
)

print(points[0])
# (10, 20)

print(points[0][1])
# 20
```

Это позволяет создавать многоуровневые структуры данных.

---

### Tuple and Mutable Objects

Кортеж может содержать изменяемые объекты:

```python
data = ([1, 2], [3, 4])

data[0].append(5)

print(data)
# ([1, 2, 5], [3, 4])
```

При этом нельзя заменить сам элемент:

```python
data[0] = [10, 20]  # TypeError
```

Кортеж остаётся неизменяемым, но его элементы могут ссылаться на изменяемые объекты.

---

### Hashability

Кортеж может быть хешируемым, если все его элементы также являются хешируемыми.

Например:

```python
point = (10, 20)

data = {
    point: "coordinate"
}

print(data[point])
# coordinate
```

Но кортеж, содержащий изменяемый объект, например список, не может использоваться как ключ словаря:

```python
key = ([1, 2], 3)

data = {
    key: "value"
}
# TypeError: unhashable type: 'list'
```

---

### Tuple vs List

Кортеж и список являются последовательностями, но имеют важное различие.

`list` является изменяемым:

```python
numbers = [1, 2, 3]
numbers.append(4)
```

`tuple` является неизменяемым:

```python
numbers = (1, 2, 3)

# numbers.append(4)  # AttributeError
```

Кортеж следует использовать, когда набор значений не должен изменяться.

---

## Syntax

Основной синтаксис Python.

```python
# Empty tuple
empty = ()

# Tuple with multiple elements
numbers = (1, 2, 3)

# Tuple without parentheses
numbers = 1, 2, 3

# Single-element tuple
single = (10,)

# Tuple with different types
data = (10, "Python", True)

# Nested tuple
nested = ((1, 2), (3, 4))

# Tuple constructor
numbers = tuple([1, 2, 3])

# Indexing
value = numbers[0]

# Slicing
part = numbers[1:3]

# Unpacking
a, b, c = numbers

# Extended unpacking
first, *middle, last = numbers
```

---

## Rules

1. Кортеж является упорядоченной последовательностью.
2. Индексация начинается с `0`.
3. Для доступа к элементам используются индексы.
4. Поддерживаются отрицательные индексы.
5. Кортеж поддерживает срезы.
6. Кортеж является неизменяемым.
7. Нельзя изменить, добавить или удалить элемент существующего кортежа.
8. Кортеж может содержать объекты разных типов.
9. Пустой кортеж создаётся как `()`.
10. Для кортежа из одного элемента обязательна запятая: `(value,)`.
11. Кортеж можно создать без круглых скобок, используя запятые.
12. Кортеж поддерживает `len()`, `in`, `not in`, `count()` и `index()`.
13. Кортеж можно использовать в цикле `for`.
14. Кортеж поддерживает распаковку.
15. При расширенной распаковке переменная с `*` получает список.
16. Кортеж может содержать изменяемые объекты.
17. Кортеж может быть ключом словаря только тогда, когда все его элементы хешируемы.
18. `tuple()` может использоваться для создания кортежа из итерируемого объекта.

---

## Examples

### Example 1 — Creating a Tuple

```python
person = ("Roman", 27, "Python")

print(person)
# ('Roman', 27, 'Python')
```

Explanation:

Кортеж может хранить значения разных типов. В данном примере он содержит строку, число и ещё одну строку.

---

### Example 2 — Indexing and Slicing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[0])
# 10

print(numbers[-1])
# 50

print(numbers[1:4])
# (20, 30, 40)
```

Explanation:

Индексы позволяют получать отдельные элементы, а срезы — получать части кортежа.

---

### Example 3 — Single-Element Tuple

```python
value = (42,)

print(type(value))
# <class 'tuple'>
```

Explanation:

Запятая является обязательной для создания кортежа из одного элемента.

---

### Example 4 — Tuple Unpacking

```python
user = ("Roman", 27, "Python")

name, age, language = user

print(name)
# Roman

print(age)
# 27

print(language)
# Python
```

Explanation:

Элементы кортежа автоматически распределяются между переменными.

---

### Example 5 — Extended Unpacking

```python
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print(first)
# 1

print(middle)
# [2, 3, 4]

print(last)
# 5
```

Explanation:

Оператор `*` собирает все оставшиеся элементы в список.

---

### Example 6 — Returning Multiple Values

```python
def get_user():
    return "Roman", 27


name, age = get_user()

print(name)
# Roman

print(age)
# 27
```

Explanation:

Функция фактически возвращает кортеж из двух значений. Распаковка позволяет сразу присвоить эти значения отдельным переменным.

---

### Example 7 — Tuple as Dictionary Key

```python
point = (10, 20)

locations = {
    point: "office"
}

print(locations[point])
# office
```

Explanation:

Кортеж из чисел является хешируемым и поэтому может использоваться как ключ словаря.

---

### Example 8 — Tuple with Mutable Object

```python
data = ([1, 2], 10)

data[0].append(3)

print(data)
# ([1, 2, 3], 10)
```

Explanation:

Сам кортеж не изменяется: ссылка на список остаётся на том же месте. Изменяется объект списка, находящийся внутри кортежа.

---

## Edge Cases

### Empty Tuple

Пустой кортеж не содержит элементов:

```python
value = ()

print(len(value))
# 0
```

---

### Missing Comma in Single-Element Tuple

```python
value = (10)

print(type(value))
# <class 'int'>
```

Для создания кортежа нужна запятая:

```python
value = (10,)

print(type(value))
# <class 'tuple'>
```

---

### Index Out of Range

Попытка обратиться к несуществующему индексу вызывает `IndexError`:

```python
numbers = (1, 2, 3)

print(numbers[10])
# IndexError
```

---

### Empty Tuple Unpacking

Нельзя распаковать пустой кортеж в обязательные переменные:

```python
value = ()

a, b = value
# ValueError
```

Количество элементов должно соответствовать количеству переменных либо должна использоваться расширенная распаковка.

---

### Unpacking Mismatch

Если элементов больше, чем переменных:

```python
numbers = (1, 2, 3)

a, b = numbers
# ValueError
```

Можно использовать `*`:

```python
a, *rest = numbers

print(a)
# 1

print(rest)
# [2, 3]
```

---

### Mutable Elements

Не следует считать кортеж полностью «глубоко неизменяемым».

```python
data = ([1, 2],)

data[0].append(3)

print(data)
# ([1, 2, 3],)
```

Изменяемые объекты внутри кортежа всё ещё могут изменяться.

---

### Unhashable Tuple

Кортеж со списком нельзя использовать как ключ словаря:

```python
value = ([1, 2], 3)

hash(value)
# TypeError
```

Причина — список является нехешируемым объектом.

---

## Common Mistakes

### Mistake 1 — Forgetting the Comma

Неправильно:

```python
value = (10)

print(type(value))
# int
```

Правильно:

```python
value = (10,)

print(type(value))
# tuple
```

---

### Mistake 2 — Trying to Modify a Tuple

Неправильно:

```python
numbers = (1, 2, 3)

numbers[0] = 10
# TypeError
```

Если данные должны изменяться, следует использовать `list`.

---

### Mistake 3 — Confusing Tuple Immutability with Deep Immutability

Нельзя изменить ссылку на элемент:

```python
data = ([1, 2], 3)

# data[0] = [10, 20]  # TypeError
```

Но можно изменить сам список:

```python
data[0].append(3)
```

---

### Mistake 4 — Incorrect Unpacking

Неправильно:

```python
numbers = (1, 2, 3)

a, b = numbers
# ValueError
```

Правильно:

```python
a, b, c = numbers
```

или:

```python
a, *rest = numbers
```

---

### Mistake 5 — Expecting List Methods

У кортежа нет методов `append()`, `remove()`, `sort()` и других методов изменения списка.

```python
numbers = (3, 1, 2)

numbers.append(4)
# AttributeError
```

Если необходимо изменять последовательность, используйте `list`.

---

## Related Concepts

* `list` — изменяемая упорядоченная последовательность.
* `set` — коллекция уникальных элементов без индексированного доступа.
* `dict` — структура данных для хранения пар ключ-значение.
* `frozenset` — неизменяемое множество.
* `tuple()` — встроенный конструктор кортежей.
* `len()` — получение количества элементов.
* `enumerate()` — получение индексов и значений при итерации.
* Unpacking — распаковка элементов последовательности.
* Hashability — возможность объекта использоваться в хеш-таблицах.
* Sequence operations — общие операции над последовательностями.

---

## Key Takeaways

* `tuple` — упорядоченная неизменяемая последовательность.
* Индексация начинается с `0`.
* Кортеж поддерживает индексацию, срезы, итерацию и проверку принадлежности.
* Кортеж нельзя изменить после создания.
* Для кортежа из одного элемента нужна запятая: `(value,)`.
* Кортежи удобно использовать для фиксированных наборов значений.
* Кортежи поддерживают обычную и расширенную распаковку.
* Кортеж может содержать изменяемые объекты, которые сами могут изменяться.
* Кортеж может использоваться как ключ словаря, если все его элементы хешируемы.
* Основные методы кортежа — `count()` и `index()`.
* Если структура данных должна изменяться, обычно следует использовать `list`.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Data model — Tuples
* Python Standard Library — Built-in Types — `tuple`
* Python Standard Library — Common Sequence Operations
* Python 3.14 Tutorial — Data Structures
* Official documentation: https://docs.python.org/3.14/library/stdtypes.html#tuple
* Official documentation: https://docs.python.org/3.14/library/stdtypes.html#common-sequence-operations
* Official documentation: https://docs.python.org/3.14/tutorial/datastructures.html#tuples
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html
