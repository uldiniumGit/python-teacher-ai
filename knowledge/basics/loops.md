# Loops

## Definition

Циклы — это конструкции Python, которые позволяют многократно выполнять блок кода.

В Python используются два основных типа циклов:

* `for` — последовательно перебирает элементы итерируемого объекта;
* `while` — выполняет блок кода, пока условие остается истинным.

Для управления выполнением цикла используются `break` и `continue`. Циклы `for` и `while` также могут иметь блок `else`, который выполняется, если цикл завершился без `break`.

---

## Purpose

Циклы используются для:

* обработки элементов списков, кортежей, строк, множеств и других итерируемых объектов;
* повторения операции несколько раз;
* выполнения кода до выполнения определенного условия;
* перебора числовых последовательностей;
* поиска элементов;
* обработки данных;
* построения алгоритмов, требующих повторяющихся действий.

---

## Core Concepts

### `for` Loop

Цикл `for` используется для перебора элементов итерируемого объекта.

В отличие от циклов в некоторых других языках программирования, `for` в Python не требует заранее задавать счетчик, условие завершения и шаг. Он получает элементы итерируемого объекта последовательно.

```python
for item in iterable:
    statements
```

Пример:

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)
```

Цикл последовательно получает `"Alice"`, `"Bob"` и `"Charlie"`.

Итерируемыми объектами могут быть:

* `list`;
* `tuple`;
* `str`;
* `set`;
* `dict`;
* `range`;
* другие объекты, поддерживающие итерацию.

---

### `while` Loop

Цикл `while` выполняет блок кода, пока его условие имеет истинное значение.

```python
while condition:
    statements
```

Пример:

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

Результат:

```text
0
1
2
```

После изменения `count` условие в конечном итоге становится ложным, и цикл завершается.

---

### `range()`

`range()` используется для создания последовательности целых чисел.

Основные формы:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Значение `stop` не включается в последовательность.

```python
for number in range(5):
    print(number)
```

Результат:

```text
0
1
2
3
4
```

Можно задать начальное значение:

```python
for number in range(2, 5):
    print(number)
```

Результат:

```text
2
3
4
```

Можно задать шаг:

```python
for number in range(0, 10, 2):
    print(number)
```

Результат:

```text
0
2
4
6
8
```

Шаг может быть отрицательным:

```python
for number in range(5, 0, -1):
    print(number)
```

Результат:

```text
5
4
3
2
1
```

`range()` возвращает объект `range`, а не готовый список.

```python
numbers = range(5)

print(numbers)
```

Результат имеет вид:

```text
range(0, 5)
```

При необходимости его можно преобразовать в список:

```python
numbers = list(range(5))

print(numbers)
```

---

### `break`

`break` немедленно завершает ближайший окружающий цикл `for` или `while`.

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

Результат:

```text
0
1
2
3
4
```

После выполнения `break` управление передается инструкции после цикла.

---

### `continue`

`continue` завершает текущую итерацию и переходит к следующей итерации цикла.

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

Результат:

```text
0
1
3
4
```

В отличие от `break`, `continue` не завершает весь цикл.

---

### Loop `else`

Циклы `for` и `while` могут иметь блок `else`.

Для цикла `for` `else` выполняется после завершения всех итераций, если `break` не был выполнен.

```python
for number in range(3):
    print(number)
else:
    print("Loop finished")
```

Результат:

```text
0
1
2
Loop finished
```

Если цикл завершается через `break`, блок `else` не выполняется.

```python
for number in range(5):
    if number == 2:
        break
else:
    print("Loop finished")
```

В этом случае `else` не выполняется.

`else` относится к циклу, а не к находящемуся внутри цикла `if`.

---

### Nested Loops

Цикл может находиться внутри другого цикла.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Внутренний цикл выполняется полностью для каждой итерации внешнего цикла.

Вложенные циклы часто используются для обработки двумерных структур данных, таблиц и комбинаций элементов.

---

### `pass`

`pass` — это инструкция, которая ничего не делает.

Она используется, когда синтаксис Python требует наличия инструкции, но выполнять действие пока не требуется.

```python
for number in range(5):
    if number == 2:
        pass
```

`pass` не пропускает текущую итерацию.

Для пропуска текущей итерации используется `continue`.

---

### `enumerate()`

`enumerate()` позволяет одновременно получать индекс и значение элемента при итерации.

```python
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(index, name)
```

Результат:

```text
0 Alice
1 Bob
2 Charlie
```

Начальный индекс можно изменить:

```python
for index, name in enumerate(names, start=1):
    print(index, name)
```

Результат:

```text
1 Alice
2 Bob
3 Charlie
```

`enumerate()` часто удобнее, чем использование `range(len(...))`.

---

### `zip()`

`zip()` позволяет одновременно перебирать несколько итерируемых объектов.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]

for name, score in zip(names, scores):
    print(name, score)
```

Результат:

```text
Alice 90
Bob 85
Charlie 95
```

При обычном использовании `zip()` итерация заканчивается, когда заканчивается самый короткий переданный итерируемый объект.

---

### Iterating Over a Dictionary

При непосредственной итерации по словарю цикл `for` перебирает его ключи.

```python
user = {
    "name": "Alice",
    "age": 25,
}

for key in user:
    print(key)
```

Для получения ключей и значений можно использовать `items()`:

```python
for key, value in user.items():
    print(key, value)
```

Для получения только значений:

```python
for value in user.values():
    print(value)
```

---

### Modifying a Collection During Iteration

Изменение коллекции во время итерации по этой же коллекции может привести к ошибкам или неожиданному поведению.

Например, не рекомендуется удалять элементы из словаря непосредственно во время его обхода.

Вместо этого можно итерироваться по копии:

```python
users = {
    "Alice": "active",
    "Bob": "inactive",
    "Charlie": "active",
}

for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
```

Другой подход — создать новую коллекцию:

```python
active_users = {}

for user, status in users.items():
    if status == "active":
        active_users[user] = status
```

---

## Syntax

### `for`

```python
for variable in iterable:
    statements
```

### `while`

```python
while condition:
    statements
```

### `for` with `else`

```python
for variable in iterable:
    statements
else:
    statements
```

### `while` with `else`

```python
while condition:
    statements
else:
    statements
```

### `break`

```python
for item in iterable:
    if condition:
        break
```

### `continue`

```python
for item in iterable:
    if condition:
        continue
```

### `range()`

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

### `enumerate()`

```python
enumerate(iterable)
enumerate(iterable, start=0)
```

### `zip()`

```python
zip(iterable1, iterable2)
```

---

## Rules

1. `for` используется для итерации по итерируемому объекту.
2. `while` выполняется до тех пор, пока его условие является истинным.
3. В `range(start, stop)` значение `stop` не включается.
4. `range()` поддерживает начальное значение, конечное значение и шаг.
5. `range()` может использовать отрицательный шаг.
6. `range()` возвращает объект `range`, а не список.
7. `break` завершает ближайший окружающий цикл.
8. `continue` пропускает оставшуюся часть текущей итерации.
9. `else` у цикла выполняется, если цикл завершился без `break`.
10. `return` или исключение также не позволяют loop `else` выполниться.
11. `break` во внутреннем цикле вложенной конструкции завершает только этот внутренний цикл.
12. `pass` ничего не делает.
13. `pass` не заменяет `continue`.
14. При непосредственной итерации по словарю перебираются его ключи.
15. Для одновременного получения индекса и значения рекомендуется использовать `enumerate()`.
16. Для одновременной итерации по нескольким последовательностям можно использовать `zip()`.
17. Не следует без необходимости изменять коллекцию во время итерации по ней.
18. В `while` необходимо следить за изменением состояния, влияющего на условие.
19. Неправильное условие `while` может привести к бесконечному циклу.
20. Циклы могут быть вложенными друг в друга.

---

## Examples

### Example 1 — Iterating Over a List

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Explanation:

`for` последовательно получает каждый элемент списка.

---

### Example 2 — Iterating Over a String

```python
word = "Python"

for character in word:
    print(character)
```

Explanation:

Строка является итерируемым объектом, поэтому `for` последовательно получает каждый символ.

---

### Example 3 — Counting with `range()`

```python
for number in range(1, 6):
    print(number)
```

Explanation:

Цикл выводит числа от `1` до `5`. Значение `6` не входит в диапазон.

---

### Example 4 — Using a Negative Step

```python
for number in range(10, 0, -2):
    print(number)
```

Explanation:

Цикл начинает с `10` и уменьшает значение на `2` на каждой итерации.

Результат:

```text
10
8
6
4
2
```

---

### Example 5 — Using `while`

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Explanation:

Цикл продолжается, пока `number <= 5`.

---

### Example 6 — Finding an Element with `break`

```python
numbers = [4, 7, 12, 15, 20]

for number in numbers:
    if number % 2 == 0:
        print(f"Found: {number}")
        break
```

Explanation:

Цикл останавливается после нахождения первого четного числа.

---

### Example 7 — Skipping Values with `continue`

```python
for number in range(1, 6):
    if number % 2 == 0:
        continue

    print(number)
```

Explanation:

Четные числа пропускаются.

Результат:

```text
1
3
5
```

---

### Example 8 — Searching with Loop `else`

```python
numbers = [1, 3, 5, 7]
target = 4

for number in numbers:
    if number == target:
        print("Found")
        break
else:
    print("Not found")
```

Explanation:

`target` не найден, поэтому `break` не выполняется и запускается блок `else`.

---

### Example 9 — Nested Loops

```python
for row in range(2):
    for column in range(3):
        print(row, column)
```

Explanation:

Внешний цикл выполняется два раза. Для каждой его итерации внутренний цикл выполняется три раза.

---

### Example 10 — Using `enumerate()`

```python
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names, start=1):
    print(f"{index}: {name}")
```

Explanation:

`enumerate()` возвращает пары из индекса и значения.

---

### Example 11 — Using `zip()`

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]

for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

Explanation:

На каждой итерации получаются соответствующие элементы двух последовательностей.

---

### Example 12 — Iterating Over a Dictionary

```python
user = {
    "name": "Alice",
    "age": 25,
}

for key, value in user.items():
    print(f"{key}: {value}")
```

Explanation:

`items()` предоставляет пары `key` и `value`.

---

## Edge Cases

### Empty Iterable

Если `for` получает пустой итерируемый объект, тело цикла не выполняется.

```python
for item in []:
    print(item)

print("Done")
```

Результат:

```text
Done
```

Если у цикла есть `else`, он выполнится:

```python
for item in []:
    print(item)
else:
    print("No items")
```

---

### `while` with a False Condition

Если условие `while` изначально ложно, тело цикла не выполняется.

```python
while False:
    print("Never executed")
```

При наличии `else` он выполнится:

```python
while False:
    print("Never executed")
else:
    print("Finished")
```

---

### Infinite `while` Loop

Если состояние, влияющее на условие, никогда не изменяется, цикл может стать бесконечным.

```python
count = 0

while count < 5:
    print(count)
```

`count` остается равным `0`, поэтому условие всегда остается истинным.

Исправленный вариант:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

### Empty `range()`

`range()` может создать пустую последовательность.

```python
for number in range(5, 1):
    print(number)
```

Ничего не выводится, потому что по умолчанию `step` равен `1`, а последовательность не может двигаться от `5` к `1` с положительным шагом.

Для обратного направления используется отрицательный шаг:

```python
for number in range(5, 1, -1):
    print(number)
```

Результат:

```text
5
4
3
2
```

---

### `break` in Nested Loops

`break` завершает только ближайший цикл.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break

        print(i, j)
```

Внешний цикл продолжает выполнение.

---

### `continue` in `while`

При использовании `continue` в `while` необходимо убедиться, что состояние цикла изменяется до следующей итерации.

Проблемный код:

```python
count = 0

while count < 5:
    if count == 2:
        continue

    count += 1
```

Когда `count` становится равным `2`, выполняется `continue`, поэтому `count` больше не увеличивается. Цикл становится бесконечным.

---

### `range()` Does Not Include `stop`

```python
numbers = list(range(1, 5))

print(numbers)
```

Результат:

```text
[1, 2, 3, 4]
```

`5` не входит в диапазон.

---

### Different Lengths with `zip()`

Если переданные в `zip()` итерируемые объекты имеют разную длину, обычный `zip()` заканчивает итерацию после самого короткого объекта.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)
```

Результат:

```text
Alice 90
Bob 85
```

---

## Common Mistakes

### Mistake 1 — Forgetting to Update a `while` Loop

Неправильно:

```python
count = 0

while count < 10:
    print(count)
```

Условие никогда не становится ложным.

Правильно:

```python
count = 0

while count < 10:
    print(count)
    count += 1
```

---

### Mistake 2 — Expecting `range()` to Include `stop`

Неправильно ожидать:

```python
range(1, 5)
```

как последовательность:

```text
1 2 3 4 5
```

Фактически:

```text
1 2 3 4
```

---

### Mistake 3 — Confusing `break` and `continue`

`break` полностью завершает ближайший цикл:

```python
break
```

`continue` пропускает только текущую итерацию:

```python
continue
```

---

### Mistake 4 — Confusing `pass` and `continue`

`pass` ничего не делает:

```python
if condition:
    pass
```

`continue` переходит к следующей итерации:

```python
if condition:
    continue
```

---

### Mistake 5 — Misunderstanding Loop `else`

`else` у цикла не означает обычное "иначе".

Он выполняется, когда цикл завершился без `break`.

```python
for number in numbers:
    if number == target:
        break
else:
    print("Not found")
```

---

### Mistake 6 — Using `range(len(...))` Unnecessarily

Вместо:

```python
names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):
    print(i, names[i])
```

часто лучше использовать:

```python
for i, name in enumerate(names):
    print(i, name)
```

---

### Mistake 7 — Modifying a Collection During Iteration

Изменение коллекции непосредственно во время ее обхода может привести к неожиданным результатам или ошибкам.

Безопаснее использовать копию или создавать новую коллекцию.

---

### Mistake 8 — Assuming `zip()` Pads Missing Values

`zip()` не добавляет автоматически отсутствующие значения.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)
```

`Charlie` не будет обработан, потому что второй итерируемый объект закончился.

---

## Related Concepts

* Variables
* Data Types
* Conditions
* Lists
* Tuples
* Sets
* Dictionaries
* Functions
* Iterables
* Iterators
* List Comprehensions
* `range()`
* `enumerate()`
* `zip()`
* `break`
* `continue`

---

## Key Takeaways

* `for` используется для перебора элементов итерируемого объекта.
* `while` выполняется, пока его условие истинно.
* `range()` используется для числовых последовательностей.
* Правая граница `range()` не включается.
* `break` завершает ближайший цикл.
* `continue` пропускает текущую итерацию.
* `else` у цикла выполняется, если `break` не произошел.
* `pass` ничего не делает.
* `enumerate()` позволяет одновременно получать индекс и значение.
* `zip()` позволяет одновременно перебирать несколько итерируемых объектов.
* Вложенные циклы позволяют выполнять циклы внутри других циклов.
* При `while` необходимо контролировать изменение условия.
* Изменение коллекции во время ее итерации требует особой осторожности.
* Хороший цикл должен иметь понятное условие завершения.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Compound statements — The `for` statement
* Python Language Reference — Compound statements — The `while` statement
* Python Language Reference — The `break` statement
* Python Language Reference — The `continue` statement
* Python Language Reference — The `pass` statement
* Python 3.14 Standard Library — Built-in Functions — `range()`
* Python 3.14 Standard Library — Built-in Functions — `enumerate()`
* Python 3.14 Standard Library — Built-in Functions — `zip()`
* Python 3.14 Tutorial — More Control Flow Tools
* Official documentation: https://docs.python.org/3.14/reference/compound_stmts.html
* Official documentation: https://docs.python.org/3.14/reference/simple_stmts.html
* Official documentation: https://docs.python.org/3.14/library/functions.html#range
* Official documentation: https://docs.python.org/3.14/library/functions.html#enumerate
* Official documentation: https://docs.python.org/3.14/library/functions.html#zip
* Official documentation: https://docs.python.org/3.14/tutorial/controlflow.html
