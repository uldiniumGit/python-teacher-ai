# Functions

## Definition

Функция — это именованный объект Python, содержащий блок кода, который выполняется при вызове функции.

Функция определяется с помощью ключевого слова `def`. При определении создается объект функции, но тело функции не выполняется. Тело выполняется только при вызове функции.

Функция может принимать аргументы и возвращать результат с помощью `return`. Если функция не выполняет `return` со значением, она возвращает `None`.

---

## Purpose

Функции используются для:

* повторного использования кода;
* разделения программы на логические части;
* уменьшения дублирования;
* создания понятной структуры программы;
* обработки входных данных;
* возврата результатов вычислений;
* создания повторно используемого API;
* абстрагирования сложной логики за простым интерфейсом.

Функции особенно полезны, когда один и тот же алгоритм необходимо использовать в нескольких местах программы.

---

## Core Concepts

### Function Definition

Функция определяется с помощью `def`.

```python
def greet():
    print("Hello")
```

Определение функции связывает имя `greet` с объектом функции.

Само определение функции не выполняет ее тело.

Чтобы выполнить функцию, ее необходимо вызвать:

```python
greet()
```

---

### Function Call

Вызов функции выполняется с помощью круглых скобок:

```python
function_name()
```

Если функция принимает параметры, значения передаются во время вызова:

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
```

При вызове `"Alice"` передается функции в качестве аргумента.

---

### Parameters and Arguments

Параметр — это имя, указанное в определении функции.

Аргумент — это конкретное значение, переданное функции при вызове.

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
```

Здесь:

* `name` — параметр;
* `"Alice"` — аргумент.

---

### Positional Arguments

При позиционной передаче аргументы сопоставляются с параметрами по их позиции.

```python
def add(a, b):
    return a + b

result = add(2, 3)
```

`2` передается параметру `a`, а `3` — параметру `b`.

---

### Keyword Arguments

Аргументы можно передавать по имени параметра.

```python
def introduce(name, age):
    print(name, age)

introduce(name="Alice", age=25)
```

Порядок keyword arguments может отличаться:

```python
introduce(age=25, name="Alice")
```

Keyword arguments позволяют явно указать, какому параметру передается значение.

---

### Default Parameter Values

Параметр может иметь значение по умолчанию.

```python
def greet(name, message="Hello"):
    print(message, name)
```

Теперь параметр `message` можно не передавать:

```python
greet("Alice")
```

Или передать другое значение:

```python
greet("Alice", "Welcome")
```

Значения параметров по умолчанию вычисляются при выполнении определения функции и используются при последующих вызовах, если соответствующий аргумент не был передан.

---

### Mutable Default Arguments

Особенно важно учитывать поведение изменяемых объектов в качестве значений по умолчанию.

Нежелательный вариант:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Список создается один раз при определении функции и затем используется повторно.

Поэтому вызовы:

```python
print(add_item("a"))
print(add_item("b"))
```

могут дать:

```text
['a']
['a', 'b']
```

Если нужен новый список при каждом вызове, обычно используется `None`:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

---

### Return Statement

`return` завершает выполнение функции и возвращает значение вызывающему коду.

```python
def add(a, b):
    return a + b

result = add(2, 3)
```

`result` получает значение `5`.

`return` может возвращать любое значение Python:

```python
def get_name():
    return "Alice"
```

---

### Return Without a Value

`return` без выражения возвращает `None`.

```python
def stop():
    return
```

То же относится к функции, которая заканчивается без `return`:

```python
def greet():
    print("Hello")

result = greet()

print(result)
```

Результат:

```text
Hello
None
```

---

### Multiple Return Values

Функция может возвращать несколько значений.

```python
def get_user():
    return "Alice", 25
```

Фактически функция возвращает один объект-кортеж, содержащий два значения.

Его можно распаковать:

```python
name, age = get_user()
```

---

### `*args`

Параметр `*args` позволяет функции принимать произвольное количество позиционных аргументов.

```python
def add_all(*args):
    return sum(args)
```

Пример:

```python
result = add_all(1, 2, 3, 4)
```

Внутри функции `args` является кортежем.

```python
def show_args(*args):
    print(args)

show_args(1, 2, 3)
```

Результат:

```text
(1, 2, 3)
```

Имя `args` не является обязательным. Важен символ `*`.

---

### `**kwargs`

Параметр `**kwargs` позволяет принимать произвольное количество keyword arguments.

```python
def show_user(**kwargs):
    print(kwargs)
```

Вызов:

```python
show_user(name="Alice", age=25)
```

Внутри функции `kwargs` является словарем:

```text
{'name': 'Alice', 'age': 25}
```

Имя `kwargs` также не является обязательным. Важны две звездочки `**`.

---

### Combining Parameters

Разные виды параметров можно комбинировать.

```python
def example(name, age=18, *args, **kwargs):
    ...
```

При этом порядок параметров имеет значение.

Также Python позволяет явно разделять positional-only и keyword-only параметры с помощью `/` и `*`.

---

### Positional-Only Parameters

Параметры перед `/` являются positional-only.

```python
def greet(name, /):
    print(name)
```

Такой параметр можно передать только позиционно:

```python
greet("Alice")
```

Но нельзя:

```python
greet(name="Alice")
```

---

### Keyword-Only Parameters

Параметры после `*` являются keyword-only.

```python
def create_user(name, *, age):
    print(name, age)
```

Правильно:

```python
create_user("Alice", age=25)
```

Неправильно:

```python
create_user("Alice", 25)
```

---

### Positional-or-Keyword Parameters

Обычные параметры могут передаваться как позиционно, так и по имени.

```python
def greet(name):
    print(name)
```

Оба вызова допустимы:

```python
greet("Alice")
greet(name="Alice")
```

---

### Function Scope

Переменные, созданные внутри функции, обычно являются локальными для этой функции.

```python
def calculate():
    value = 10
    print(value)

calculate()
```

Переменная `value` существует в локальной области видимости функции.

Попытка обратиться к ней за пределами функции:

```python
print(value)
```

приведет к ошибке, если переменная не определена в другой области видимости.

---

### Local and Global Variables

Переменная, определенная внутри функции, является локальной, если она не объявлена иначе.

```python
value = 10

def example():
    value = 20
    print(value)

example()

print(value)
```

Результат:

```text
20
10
```

Локальная переменная не изменяет глобальную переменную с тем же именем.

---

### `global`

`global` используется внутри функции, чтобы объявить, что имя относится к глобальной переменной.

```python
counter = 0

def increment():
    global counter
    counter += 1
```

Использовать `global` следует осторожно, поскольку большое количество глобального изменяемого состояния усложняет программу.

---

### `nonlocal`

`nonlocal` используется во вложенной функции для изменения переменной из ближайшей внешней функции.

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

`nonlocal` не относится к глобальной области видимости. Он используется для работы с переменными внешней функции.

---

### Functions Are First-Class Objects

Функции являются объектами и могут:

* присваиваться переменным;
* передаваться в другие функции;
* возвращаться из функций;
* храниться в коллекциях.

```python
def greet():
    return "Hello"

message = greet

print(message())
```

Здесь `message` ссылается на тот же объект функции.

---

### Functions as Arguments

Функцию можно передать другой функции как аргумент.

```python
def apply(func, value):
    return func(value)

def square(x):
    return x * x

result = apply(square, 5)
```

`apply()` получает функцию `square` и вызывает ее внутри себя.

---

### Nested Functions

Функцию можно определить внутри другой функции.

```python
def outer():
    def inner():
        print("Hello")

    inner()
```

Вложенная функция может обращаться к переменным внешней функции.

```python
def multiplier(n):
    def multiply(value):
        return value * n

    return multiply
```

---

### Recursion

Рекурсия — это ситуация, когда функция вызывает саму себя.

```python
def countdown(n):
    if n <= 0:
        return

    print(n)
    countdown(n - 1)
```

Рекурсивная функция должна иметь условие завершения. Без него вызовы будут продолжаться до возникновения ошибки переполнения глубины рекурсии.

---

### Lambda Functions

`lambda` создает небольшую анонимную функцию.

```python
square = lambda x: x * x
```

Это эквивалентно простой функции:

```python
def square(x):
    return x * x
```

Lambda ограничена одним выражением.

Она часто используется как короткая функция, передаваемая в другую функцию:

```python
numbers = [3, 1, 2]

numbers.sort(key=lambda x: x)

print(numbers)
```

---

### Docstrings

Первый строковый литерал в теле функции может использоваться как ее документация.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

Такой текст называется docstring и сохраняется в `__doc__`.

Docstrings используются для описания назначения функции, ее параметров и возвращаемого значения.

---

### Function Annotations

Параметры и возвращаемое значение функции могут иметь annotations.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Annotations являются метаданными. Сам Python не использует их автоматически для проверки типов.

Они могут использоваться статическими анализаторами, IDE и другими инструментами.

В Python 3.14 annotations по умолчанию вычисляются лениво.

---

## Syntax

### Basic Function

```python
def function_name():
    statements
```

### Function with Parameters

```python
def function_name(parameter1, parameter2):
    statements
```

### Function with Return Value

```python
def function_name(parameter):
    return value
```

### Default Parameter

```python
def function_name(parameter=default_value):
    statements
```

### Positional-Only Parameter

```python
def function_name(parameter, /):
    statements
```

### Keyword-Only Parameter

```python
def function_name(*, parameter):
    statements
```

### Arbitrary Positional Arguments

```python
def function_name(*args):
    statements
```

### Arbitrary Keyword Arguments

```python
def function_name(**kwargs):
    statements
```

### Combined Parameters

```python
def function_name(pos_only, /, standard, *args, keyword_only, **kwargs):
    statements
```

### Function Annotation

```python
def function_name(parameter: type) -> type:
    return value
```

### Lambda

```python
lambda parameter: expression
```

### Function Call

```python
function_name(argument)
```

### Keyword Argument Call

```python
function_name(parameter=value)
```

---

## Rules

1. Функция определяется с помощью `def`.
2. Определение функции создает объект функции, но не выполняет ее тело.
3. Тело функции выполняется только при вызове функции.
4. Блок тела функции должен быть выделен отступом.
5. Параметры указываются при определении функции.
6. Аргументы передаются при вызове функции.
7. Аргументы можно передавать позиционно или по имени.
8. Параметры со значениями по умолчанию могут не получать аргумент при вызове.
9. Значения параметров по умолчанию вычисляются при выполнении определения функции.
10. Изменяемые объекты в качестве значений по умолчанию могут сохранять состояние между вызовами.
11. `return` завершает выполнение функции.
12. `return` может возвращать значение вызывающему коду.
13. `return` без значения возвращает `None`.
14. Если функция заканчивается без `return`, она возвращает `None`.
15. `*args` собирает дополнительные позиционные аргументы в кортеж.
16. `**kwargs` собирает дополнительные keyword arguments в словарь.
17. Параметры перед `/` являются positional-only.
18. Параметры после `*` являются keyword-only.
19. Обычные параметры могут быть positional-or-keyword.
20. Локальные переменные функции доступны внутри соответствующей области видимости.
21. Для изменения глобальной переменной внутри функции используется `global`.
22. Для изменения переменной внешней функции во вложенной функции используется `nonlocal`.
23. Функции являются объектами и могут передаваться как значения.
24. Lambda является сокращенной формой небольшой функции с одним выражением.
25. Рекурсивная функция должна иметь условие завершения.
26. Первый строковый литерал в теле функции может быть docstring.
27. Function annotations не выполняют автоматическую проверку типов.
28. Функция может возвращать несколько значений; фактически они объединяются в кортеж.
29. Порядок параметров в определении функции имеет значение.
30. Позиционные аргументы нельзя указывать после keyword arguments.
31. Один параметр не может получить несколько значений одновременно.

---

## Examples

### Example 1 — Basic Function

```python
def greet():
    print("Hello")


greet()
```

Explanation:

Функция `greet` определяется с помощью `def`. Ее тело выполняется при вызове `greet()`.

---

### Example 2 — Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}")


greet("Alice")
```

Explanation:

`name` является параметром функции, а `"Alice"` — аргументом при вызове.

---

### Example 3 — Returning a Value

```python
def add(a, b):
    return a + b


result = add(2, 3)

print(result)
```

Explanation:

Функция возвращает результат вычисления через `return`.

---

### Example 4 — Default Parameter

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}")


greet("Alice")
greet("Bob", "Welcome")
```

Explanation:

Если `message` не передан, используется значение `"Hello"`.

---

### Example 5 — Keyword Arguments

```python
def create_user(name, age):
    print(name, age)


create_user(age=25, name="Alice")
```

Explanation:

Аргументы передаются по имени, поэтому их порядок при вызове может отличаться от порядка параметров.

---

### Example 6 — Positional-Only Parameter

```python
def greet(name, /):
    print(name)


greet("Alice")
```

Explanation:

`name` находится перед `/`, поэтому его можно передать только позиционно.

---

### Example 7 — Keyword-Only Parameter

```python
def create_user(name, *, age):
    print(name, age)


create_user("Alice", age=25)
```

Explanation:

`age` находится после `*`, поэтому он должен быть передан как keyword argument.

---

### Example 8 — `*args`

```python
def calculate_sum(*numbers):
    return sum(numbers)


result = calculate_sum(1, 2, 3, 4)

print(result)
```

Explanation:

Все позиционные аргументы собираются в кортеж `numbers`.

---

### Example 9 — `**kwargs`

```python
def show_user(**user):
    for key, value in user.items():
        print(key, value)


show_user(name="Alice", age=25)
```

Explanation:

Все дополнительные keyword arguments собираются в словарь `user`.

---

### Example 10 — Returning Multiple Values

```python
def get_user():
    return "Alice", 25


name, age = get_user()

print(name)
print(age)
```

Explanation:

Функция возвращает кортеж из двух элементов, который затем распаковывается в `name` и `age`.

---

### Example 11 — Function as an Argument

```python
def apply(function, value):
    return function(value)


def square(number):
    return number * number


result = apply(square, 5)

print(result)
```

Explanation:

Функция `square` передается другой функции как аргумент.

---

### Example 12 — Nested Function

```python
def create_multiplier(multiplier):
    def multiply(value):
        return value * multiplier

    return multiply


double = create_multiplier(2)

print(double(5))
```

Explanation:

`multiply` является вложенной функцией и использует переменную `multiplier` из внешней функции.

---

### Example 13 — Recursion

```python
def countdown(number):
    if number <= 0:
        return

    print(number)
    countdown(number - 1)


countdown(3)
```

Explanation:

Функция вызывает саму себя с уменьшенным значением. Условие `number <= 0` останавливает рекурсию.

---

### Example 14 — Lambda

```python
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x * x, numbers))

print(squared)
```

Explanation:

Lambda создает небольшую функцию, которая возводит число в квадрат.

---

### Example 15 — Docstring

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print(add.__doc__)
```

Explanation:

Первый строковый литерал функции становится ее docstring и доступен через `__doc__`.

---

### Example 16 — Function Annotations

```python
def add(a: int, b: int) -> int:
    return a + b
```

Explanation:

`int` используется как annotation для параметров и возвращаемого значения. Annotation не выполняет автоматическую проверку типов.

---

## Edge Cases

### Mutable Default Argument

Проблемный вариант:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Список создается один раз при определении функции.

```python
print(add_item("a"))
print(add_item("b"))
```

Результат:

```text
['a']
['a', 'b']
```

Если состояние между вызовами не требуется, используется `None`:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

---

### Function Without `return`

```python
def greet():
    print("Hello")


result = greet()

print(result)
```

Результат:

```text
Hello
None
```

Функция без возвращаемого значения возвращает `None`.

---

### Empty `return`

```python
def stop():
    return
```

Такой `return` возвращает `None`.

---

### Early `return`

`return` немедленно прекращает выполнение функции.

```python
def check_age(age):
    if age < 18:
        return "Too young"

    return "Allowed"
```

После выполнения первого `return` оставшийся код функции не выполняется.

---

### Multiple Return Values

```python
def get_coordinates():
    return 10, 20
```

Это возвращает один кортеж:

```python
coordinates = get_coordinates()

print(coordinates)
```

Результат:

```text
(10, 20)
```

---

### Too Few Arguments

Если обязательный параметр не получил значение:

```python
def greet(name):
    print(name)


greet()
```

возникает `TypeError`.

---

### Too Many Arguments

Если функции передать больше позиционных аргументов, чем она принимает:

```python
def greet(name):
    print(name)


greet("Alice", "Bob")
```

возникает `TypeError`.

---

### Multiple Values for One Parameter

Нельзя передать одному параметру значение одновременно позиционно и по имени.

```python
def greet(name):
    print(name)


greet("Alice", name="Bob")
```

Возникает `TypeError`.

---

### Positional Argument After Keyword Argument

Нельзя передавать обычный позиционный аргумент после keyword argument.

```python
def greet(name, message):
    print(name, message)


greet(name="Alice", "Hello")
```

Такой вызов является синтаксически некорректным.

---

### Recursive Function Without a Base Case

Проблемный вариант:

```python
def countdown(number):
    print(number)
    countdown(number - 1)
```

Функция не имеет условия завершения и продолжает вызывать саму себя.

Рекурсия должна иметь базовый случай.

---

### `*args` Is a Tuple

```python
def show_args(*args):
    print(type(args))


show_args(1, 2, 3)
```

Результат:

```text
<class 'tuple'>
```

---

### `**kwargs` Is a Dictionary

```python
def show_kwargs(**kwargs):
    print(type(kwargs))


show_kwargs(name="Alice")
```

Результат:

```text
<class 'dict'>
```

---

### Local Variable Shadowing

```python
value = 10

def example():
    value = 20
    print(value)


example()

print(value)
```

Результат:

```text
20
10
```

Локальная переменная с таким же именем не изменяет глобальную переменную.

---

### Annotations Do Not Automatically Validate Types

```python
def add(a: int, b: int) -> int:
    return a + b
```

Annotation указывает предполагаемый тип, но сама функция не обязана принимать только `int`.

Автоматическая проверка типов требует дополнительных инструментов.

---

## Common Mistakes

### Mistake 1 — Confusing Definition and Call

Определение:

```python
def greet():
    print("Hello")
```

Вызов:

```python
greet()
```

Определение функции само по себе не запускает ее тело.

---

### Mistake 2 — Forgetting `return`

Неправильно:

```python
def add(a, b):
    a + b


result = add(2, 3)

print(result)
```

`result` будет равен `None`.

Правильно:

```python
def add(a, b):
    return a + b
```

---

### Mistake 3 — Using `print()` Instead of `return`

`print()` выводит значение, но не передает его вызывающему коду.

```python
def add(a, b):
    print(a + b)
```

Если результат необходимо использовать дальше, следует использовать `return`:

```python
def add(a, b):
    return a + b
```

---

### Mistake 4 — Mutable Default Argument

Нежелательно:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Обычно безопаснее:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

---

### Mistake 5 — Wrong Argument Order

Неправильно:

```python
def greet(name, message):
    print(message, name)


greet(name="Alice", "Hello")
```

Позиционный аргумент нельзя размещать после keyword argument.

---

### Mistake 6 — Confusing Parameters and Arguments

```python
def greet(name):
    print(name)


greet("Alice")
```

`name` — параметр.

`"Alice"` — аргумент.

---

### Mistake 7 — Forgetting the Base Case in Recursion

Без условия завершения рекурсивная функция может продолжать вызывать себя до возникновения `RecursionError`.

---

### Mistake 8 — Assuming Annotations Enforce Types

```python
def square(number: int) -> int:
    return number * number
```

Annotation не является автоматическим runtime-проверяющим механизмом типов.

---

### Mistake 9 — Overusing Global Variables

Использование большого количества глобального изменяемого состояния усложняет понимание поведения функций.

Предпочтительно передавать необходимые данные через параметры и возвращать результаты через `return`.

---

### Mistake 10 — Using Lambda for Complex Logic

Lambda предназначена для простых выражений.

Если функция требует несколько инструкций, сложную логику или подробную документацию, обычно лучше использовать обычный `def`.

---

## Related Concepts

* Variables
* Data Types
* Conditions
* Loops
* Lists
* Tuples
* Dictionaries
* Scope
* Iterables
* Iterators
* Classes
* Methods
* Lambda expressions
* Decorators
* Function annotations
* Recursion
* `return`
* `global`
* `nonlocal`
* `*args`
* `**kwargs`

---

## Key Takeaways

* Функция — это именованный объект, содержащий повторно используемый код.
* Функция создается с помощью `def`.
* Определение функции не выполняет ее тело.
* Функция выполняется при вызове.
* Параметры задаются при определении функции.
* Аргументы передаются при вызове.
* Аргументы могут быть позиционными или keyword arguments.
* Значения параметров по умолчанию позволяют делать аргументы необязательными.
* Изменяемые значения по умолчанию требуют особой осторожности.
* `return` возвращает результат и завершает выполнение функции.
* Функция без `return` возвращает `None`.
* `*args` собирает дополнительные позиционные аргументы в кортеж.
* `**kwargs` собирает дополнительные keyword arguments в словарь.
* `/` используется для positional-only параметров.
* `*` используется для keyword-only параметров.
* Локальные переменные принадлежат области видимости функции.
* `global` позволяет работать с глобальным именем.
* `nonlocal` позволяет изменять переменную внешней функции.
* Функции являются объектами и могут передаваться как аргументы и возвращаться из других функций.
* Lambda — сокращенный синтаксис для небольшой функции, содержащей одно выражение.
* Рекурсивные функции должны иметь условие завершения.
* Docstrings используются для документирования функций.
* Function annotations являются метаданными и не выполняют автоматическую проверку типов.
* Хорошая функция обычно имеет четкую ответственность, понятные параметры и предсказуемый результат.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Compound statements — Function definitions
* Python Language Reference — Expressions — Calls
* Python Language Reference — Expressions — Lambdas
* Python Language Reference — Simple statements — The `return` statement
* Python Language Reference — Simple statements — The `global` statement
* Python Language Reference — Simple statements — The `nonlocal` statement
* Python 3.14 Tutorial — Defining Functions
* Python 3.14 Tutorial — More on Defining Functions
* Python 3.14 Tutorial — Documentation Strings
* Python 3.14 Tutorial — Function Annotations
* Official documentation: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
* Official documentation: https://docs.python.org/3.14/reference/expressions.html#calls
* Official documentation: https://docs.python.org/3.14/reference/expressions.html#lambda
* Official documentation: https://docs.python.org/3.14/reference/simple_stmts.html#the-return-statement
* Official documentation: https://docs.python.org/3.14/reference/simple_stmts.html#the-global-statement
* Official documentation: https://docs.python.org/3.14/reference/simple_stmts.html#the-nonlocal-statement
* Official documentation: https://docs.python.org/3.14/tutorial/controlflow.html#defining-functions
* Official documentation: https://docs.python.org/3.14/tutorial/controlflow.html#more-on-defining-functions
* Official documentation: https://docs.python.org/3.14/tutorial/controlflow.html#documentation-strings
* Official documentation: https://docs.python.org/3.14/tutorial/controlflow.html#function-annotations
