# Conditions

## Definition

Условные конструкции позволяют выполнять определённый участок программы в зависимости от результата проверки условия.

Основной условный оператор Python — `if`:

```python
age = 20

if age >= 18:
    print("Adult")
```

Если выражение после `if` имеет истинное значение, выполняется соответствующий блок кода.

Для нескольких альтернатив используются `elif` и `else`:

```python
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

Python определяет истинность выражения с помощью правил truth value testing. Условие не обязано непосредственно возвращать объект `bool`: любой объект может быть проверен на истинность.

---

## Purpose

Условные конструкции используются для:

* принятия решений во время выполнения программы;
* выполнения разных блоков кода в зависимости от данных;
* проверки ограничений и условий;
* обработки различных сценариев;
* управления поведением циклов и функций;
* создания логики программы.

Например:

```python
temperature = 30

if temperature > 25:
    print("Hot")
else:
    print("Cool")
```

Условие позволяет программе выбрать подходящее действие на основании значения `temperature`.

---

## Core Concepts

### `if` Statement

`if` выполняет блок кода, если условие имеет истинное значение:

```python
if condition:
    statement
```

Пример:

```python
age = 20

if age >= 18:
    print("Adult")
```

Если условие ложно, блок `if` пропускается.

---

### `elif`

`elif` позволяет проверить дополнительные условия после `if`.

```python
if condition1:
    statement1
elif condition2:
    statement2
```

Можно использовать несколько блоков `elif`:

```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
```

Проверка происходит сверху вниз. Выполняется блок первого условия, которое оказалось истинным.

---

### `else`

`else` выполняется, если ни одно из предыдущих условий не оказалось истинным:

```python
if condition:
    statement
else:
    statement
```

Пример:

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

`else` является необязательным.

---

### Conditional Chain

Конструкция `if` может содержать несколько альтернатив:

```python
if condition1:
    ...
elif condition2:
    ...
elif condition3:
    ...
else:
    ...
```

Проверки выполняются последовательно.

После того как найдено первое истинное условие, соответствующий блок выполняется, а остальные условия этой цепочки не проверяются.

Например:

```python
number = 10

if number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
else:
    print("Positive")
```

Будет выполнен только блок `else`.

---

### Nested Conditions

Условные конструкции можно помещать внутрь других условных конструкций.

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Allowed")
```

Вложенные условия позволяют создавать более сложную логику.

При большом количестве вложенных условий код может стать сложным для чтения. В таких случаях условия часто можно упростить с помощью логических операторов.

Например:

```python
if age >= 18 and has_ticket:
    print("Allowed")
```

---

### Comparison Operators

Python предоставляет операторы сравнения:

```text
<     less than
<=    less than or equal
>     greater than
>=    greater than or equal
==    equal
!=    not equal
```

Примеры:

```python
x = 10

x < 20
# True

x == 10
# True

x != 5
# True

x >= 10
# True
```

Результатом обычного сравнения является объект `bool`.

---

### Equality and Identity

Для сравнения значений используется `==`:

```python
a = [1, 2]
b = [1, 2]

print(a == b)
# True
```

Для проверки идентичности объектов используется `is`:

```python
a = [1, 2]
b = a

print(a is b)
# True
```

Эти операторы имеют разное назначение.

Особенно важно использовать `is` для проверки `None`:

```python
value = None

if value is None:
    print("No value")
```

---

### Chained Comparisons

Python поддерживает цепочки сравнений:

```python
x = 10

if 0 < x < 20:
    print("Between 0 and 20")
```

Это эквивалентно логической проверке:

```python
if 0 < x and x < 20:
    print("Between 0 and 20")
```

При этом выражение в середине цепочки вычисляется только один раз.

Можно использовать более длинные цепочки:

```python
if 0 < x <= 10 < y:
    ...
```

---

### Boolean Operators

Для объединения условий используются:

* `and`;
* `or`;
* `not`.

#### `and`

`and` требует, чтобы оба условия были истинными:

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Allowed")
```

#### `or`

`or` позволяет использовать альтернативные условия:

```python
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Access granted")
```

Условие истинно, если хотя бы один операнд имеет истинное значение.

#### `not`

`not` инвертирует truth value:

```python
is_active = False

if not is_active:
    print("Inactive")
```

---

### Short-Circuit Evaluation

`and` и `or` используют short-circuit evaluation.

Для `and`, если первый операнд имеет ложное значение, второй операнд не вычисляется.

```python
if user is not None and user.is_active:
    print("Active")
```

Если `user is not None` ложно, Python не вычисляет `user.is_active`.

Для `or`, если первый операнд имеет истинное значение, второй операнд не вычисляется.

```python
value = user_input or "default"
```

Если `user_input` имеет истинное значение, результатом становится `user_input`.

---

### Truth Value Testing

Условие в `if` преобразуется к truth value.

Ложными считаются, в частности:

* `None`;
* `False`;
* числовой ноль;
* пустая строка;
* пустой список;
* пустой кортеж;
* пустое множество;
* пустой словарь;
* пустой `range`.

Примеры:

```python
bool(0)
# False

bool("")
# False

bool([])
# False

bool("Python")
# True

bool([1, 2])
# True
```

Поэтому можно писать:

```python
items = []

if not items:
    print("Empty")
```

вместо явного сравнения:

```python
if len(items) == 0:
    print("Empty")
```

---

### Truth Value of Custom Objects

Пользовательские классы также могут определять своё поведение при проверке истинности.

Для этого используются методы:

```python
__bool__()
```

или, если `__bool__()` не определён:

```python
__len__()
```

Пример:

```python
class Collection:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return bool(self.items)
```

Теперь объект можно использовать непосредственно в условии:

```python
collection = Collection([])

if collection:
    print("Not empty")
else:
    print("Empty")
```

---

### Conditional Expression

Python поддерживает условное выражение:

```python
value_if_true if condition else value_if_false
```

Пример:

```python
age = 20

status = "Adult" if age >= 18 else "Minor"
```

Это выражение возвращает одно из двух значений.

Условные выражения особенно полезны для простого выбора значения.

Сложную логику лучше выражать обычными блоками `if` / `elif` / `else`.

---

### Boolean Values

Условие может непосредственно использовать `True` или `False`:

```python
is_active = True

if is_active:
    print("Active")
```

Однако в реальном коде условием часто является результат сравнения, вызова функции или проверки объекта:

```python
if age >= 18:
    ...

if user.is_active:
    ...

if items:
    ...
```

---

## Syntax

Базовый `if`:

```python
if condition:
    statement
```

`if` с `else`:

```python
if condition:
    statement1
else:
    statement2
```

`if` с `elif`:

```python
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
```

Несколько условий:

```python
if condition1 and condition2:
    statement
```

Альтернативные условия:

```python
if condition1 or condition2:
    statement
```

Инверсия условия:

```python
if not condition:
    statement
```

Цепочка сравнений:

```python
if 0 < x < 100:
    statement
```

Условное выражение:

```python
result = value1 if condition else value2
```

---

## Rules

### Indentation defines the block

В Python блок кода определяется отступом:

```python
if age >= 18:
    print("Adult")
    print("Allowed")
```

Обе инструкции находятся внутри блока `if`.

После блока выполняется код с соответствующим уровнем отступа:

```python
if age >= 18:
    print("Adult")

print("Finished")
```

---

### The condition is evaluated for truth

`if` не требует, чтобы условие имело тип `bool`.

Python определяет truth value объекта:

```python
items = [1, 2, 3]

if items:
    print("Not empty")
```

---

### Only the first matching branch is executed

В цепочке `if` / `elif` / `else` выполняется только первый подходящий блок:

```python
x = 10

if x > 0:
    print("Positive")
elif x > 5:
    print("Greater than 5")
```

Будет напечатано:

```text
Positive
```

После выполнения первого истинного условия дальнейшие `elif` не проверяются.

---

### `else` is executed only when all previous conditions are false

```python
x = -1

if x > 0:
    print("Positive")
else:
    print("Not positive")
```

`else` выполняется, когда условие `if` ложно.

В цепочке с `elif` `else` выполняется только тогда, когда все предыдущие условия ложны.

---

### `elif` can be repeated

Можно использовать несколько `elif`:

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

---

### `else` and `elif` are optional

Допустимо использовать только `if`:

```python
if condition:
    statement
```

Можно использовать `if` с `else`:

```python
if condition:
    statement1
else:
    statement2
```

Или `if` с несколькими `elif` и необязательным `else`.

---

### Comparisons can be chained

```python
if 18 <= age < 65:
    print("Working age")
```

Цепочка сравнений проверяет последовательность отношений между соседними выражениями.

---

### `and` and `or` use short-circuit evaluation

```python
if value is not None and value > 0:
    print("Positive")
```

Вторая часть не вычисляется, если первая часть уже определяет результат `and`.

---

### Boolean operators return operands

`and` и `or` являются выражениями и могут возвращать один из своих операндов:

```python
result = "" or "default"

print(result)
# default
```

Поэтому их поведение не следует воспринимать просто как операции, возвращающие `True` или `False`.

---

### `not` returns a boolean

`not` преобразует truth value операнда и возвращает `True` или `False`:

```python
print(not 0)
# True

print(not 10)
# False
```

---

### `is` and `is not` test identity

Для проверки того, являются ли два выражения одним объектом, используются `is` и `is not`:

```python
value = None

if value is None:
    print("None")
```

Для обычного сравнения значений следует использовать `==` и `!=`.

---

## Examples

### Example 1 — Simple condition

```python
age = 20

if age >= 18:
    print("Adult")
```

Условие истинно, поэтому выполняется блок `if`.

---

### Example 2 — `if` and `else`

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Результат:

```text
Minor
```

---

### Example 3 — Multiple branches

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
```

Результат:

```text
B
```

---

### Example 4 — Combining conditions

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
```

Оба условия должны иметь истинное значение.

---

### Example 5 — Alternative conditions

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

### Example 6 — Negation

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in")
```

---

### Example 7 — Truth value of a list

```python
items = [1, 2, 3]

if items:
    print("List is not empty")
```

---

### Example 8 — Empty collection

```python
items = []

if not items:
    print("List is empty")
```

Пустой список имеет ложное truth value.

---

### Example 9 — Chained comparison

```python
age = 25

if 18 <= age < 65:
    print("Adult")
```

---

### Example 10 — Conditional expression

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Результат:

```text
Adult
```

---

### Example 11 — Short-circuit evaluation

```python
user = None

if user is not None and user.is_active:
    print("Active")
```

Если `user is not None` имеет значение `False`, обращение к `user.is_active` не выполняется.

---

### Example 12 — Nested condition

```python
age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Entry allowed")
```

Ту же логику можно записать проще:

```python
if age >= 18 and has_ticket:
    print("Entry allowed")
```

---

## Edge Cases

### Comparing different types

Не все объекты можно сравнивать между собой:

```python
# 10 < "20"
```

Такое сравнение приводит к `TypeError`, потому что `int` и `str` не поддерживают такое упорядоченное сравнение.

При этом некоторые типы допускают сравнение значений разных типов:

```python
1 == 1.0
# True
```

Поведение сравнения определяется правилами соответствующих типов.

---

### `None` should normally be checked with `is`

Для проверки отсутствия значения рекомендуется:

```python
if value is None:
    ...
```

а не:

```python
if value == None:
    ...
```

`is` проверяет идентичность объекта `None`.

---

### Empty and non-empty objects

Объект может быть логически ложным, даже если он существует:

```python
items = []

if items:
    print("Has items")
else:
    print("Empty")
```

Сам объект `items` существует, но его truth value равно `False`.

---

### `and` and `or` return values

```python
username = ""
display_name = username or "Guest"
```

Результат:

```text
Guest
```

Но если значение непустое:

```python
username = "Roman"
display_name = username or "Guest"
```

результатом будет:

```text
Roman
```

---

### Short-circuit can prevent errors

```python
value = None

if value is not None and value > 10:
    print("Greater than 10")
```

Вторая часть не вычисляется, поэтому попытки сравнить `None` с `10` не происходит.

---

### Conditional expression with multiple conditions

Условное выражение может содержать сложное условие:

```python
age = 25
has_ticket = True

result = "Allowed" if age >= 18 and has_ticket else "Denied"
```

При усложнении такой конструкции обычный `if` может быть более читаемым.

---

### Floating-point comparisons

Прямое сравнение вычислений с `float` может дать неожиданный результат:

```python
value = 0.1 + 0.2

print(value == 0.3)
# False
```

Это связано с представлением чисел с плавающей точкой.

Для задач, требующих точного сравнения чисел с плавающей точкой, необходимо учитывать особенности `float` и использовать подходящий способ сравнения.

---

## Common Mistakes

### Mistake 1 — Using `=` instead of `==`

Неправильно:

```python
if age = 18:
    print("18")
```

`=` используется для присваивания.

Для сравнения используется:

```python
if age == 18:
    print("18")
```

---

### Mistake 2 — Using `is` for value comparison

Не следует использовать:

```python
if value is 10:
    ...
```

для обычного сравнения значения.

Используйте:

```python
if value == 10:
    ...
```

`is` предназначен для проверки идентичности объектов.

---

### Mistake 3 — Forgetting the colon

Неправильно:

```python
if age >= 18
    print("Adult")
```

Правильно:

```python
if age >= 18:
    print("Adult")
```

После условия требуется `:`.

---

### Mistake 4 — Incorrect indentation

Неправильно:

```python
if age >= 18:
print("Adult")
```

Правильно:

```python
if age >= 18:
    print("Adult")
```

Отступ определяет блок кода.

---

### Mistake 5 — Checking an empty collection incorrectly

Вместо:

```python
if len(items) > 0:
    print("Not empty")
```

часто можно использовать:

```python
if items:
    print("Not empty")
```

Для проверки пустоты коллекции Python предоставляет truth value semantics.

---

### Mistake 6 — Forgetting that `elif` stops after the first match

Например:

```python
x = 10

if x > 0:
    print("Positive")
elif x > 5:
    print("Greater than 5")
```

Вторая ветка не выполнится.

Если необходимо выполнить несколько независимых проверок, следует использовать несколько отдельных `if`:

```python
if x > 0:
    print("Positive")

if x > 5:
    print("Greater than 5")
```

---

### Mistake 7 — Incorrect use of `not`

Нужно учитывать приоритет операторов:

```python
if not age >= 18:
    ...
```

Это интерпретируется как:

```python
if not (age >= 18):
    ...
```

При сложных выражениях скобки могут сделать намерение более очевидным:

```python
if not (age >= 18 and has_ticket):
    ...
```

---

### Mistake 8 — Confusing `and` and `or`

Условие:

```python
if age >= 18 or has_ticket:
    ...
```

означает, что достаточно выполнения **одного** из условий.

Если обязательны оба условия:

```python
if age >= 18 and has_ticket:
    ...
```

---

## Related Concepts

* Boolean Type
* `bool`
* Truth Value Testing
* Comparison Operators
* `==`
* `!=`
* `is`
* `is not`
* `and`
* `or`
* `not`
* `if`
* `elif`
* `else`
* Conditional Expressions
* Expressions
* Operators
* Variables
* Data Types
* `None`
* Loops
* Functions
* Exception Handling

---

## Key Takeaways

* `if` используется для условного выполнения блока кода.
* `elif` позволяет проверять дополнительные условия.
* `else` выполняется, если предыдущие условия не были истинными.
* В цепочке `if` / `elif` / `else` выполняется только первый подходящий блок.
* Условия проверяются по правилам truth value testing.
* Для сравнения значений используются `==`, `!=`, `<`, `<=`, `>`, `>=`.
* `is` и `is not` проверяют идентичность объектов, а не равенство значений.
* `None` обычно проверяется через `is None`.
* `and`, `or` и `not` используются для логических операций.
* `and` и `or` используют short-circuit evaluation.
* `and` и `or` могут возвращать один из своих операндов, а не `True` или `False`.
* Python поддерживает цепочки сравнений, например `0 < x < 10`.
* Пустые коллекции и другие определённые объекты имеют ложное truth value.
* Условное выражение имеет форму `value_if_true if condition else value_if_false`.
* Отступы определяют блоки кода в условных конструкциях.
* Условия могут быть вложенными, но сложную вложенность часто можно заменить комбинацией логических операторов.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Compound statements — The `if` statement
* Python Language Reference — Expressions — Comparisons
* Python Language Reference — Boolean operations
* Python Standard Library — Truth Value Testing
* Python Standard Library — Boolean Operations
* Python Tutorial — More Control Flow Tools
* Official documentation: https://docs.python.org/3.14/reference/compound_stmts.html
* Official documentation: https://docs.python.org/3.14/reference/expressions.html
* Official documentation: https://docs.python.org/3.14/library/stdtypes.html#truth-value-testing
* Official documentation: https://docs.python.org/3.14/tutorial/controlflow.html
