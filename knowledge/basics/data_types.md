# Data Types

## Definition

Тип данных в Python определяет, какие значения может представлять объект и какие операции поддерживает этот объект.

В Python все данные представлены объектами. Каждый объект имеет идентичность, тип и значение. Тип объекта можно получить с помощью встроенной функции `type()`:

```python
value = 42

print(type(value))
# <class 'int'>
```

Тип объекта определяется при его создании и не изменяется в течение существования объекта.

Python имеет множество встроенных типов. К основным типам относятся числовые типы, последовательности, отображения, множества, логический тип и специальные типы.

Основные встроенные типы, рассматриваемые в этой теме:

* `int` — целые числа;
* `float` — числа с плавающей точкой;
* `complex` — комплексные числа;
* `bool` — логические значения;
* `str` — строки;
* `list` — изменяемые последовательности;
* `tuple` — неизменяемые последовательности;
* `set` — множества уникальных элементов;
* `dict` — отображения ключей на значения;
* `None` — специальный объект, обозначающий отсутствие значения.

---

## Purpose

Типы данных определяют поведение объектов в программе.

Они позволяют Python понимать:

* какие операции можно выполнять над объектом;
* как интерпретировать его значение;
* какие методы и операции доступны;
* является ли объект изменяемым или неизменяемым;
* можно ли использовать объект, например, в качестве ключа словаря или элемента множества.

Например:

```python
a = 10
b = 20

print(a + b)
# 30
```

Для числовых объектов оператор `+` выполняет сложение.

Для строк тот же оператор выполняет конкатенацию:

```python
first = "Hello"
second = "Python"

print(first + " " + second)
# Hello Python
```

Таким образом, поведение операции зависит от типов участвующих в ней объектов.

Типы также используются для организации данных:

```python
name = "Roman"
age = 27
is_student = False
scores = [90, 85, 95]
```

Здесь разные значения представлены разными типами, каждый из которых предназначен для определённого вида данных.

---

## Core Concepts

### Objects, Values and Types

В Python объект является абстракцией данных.

Каждый объект имеет:

* identity — идентичность;
* type — тип;
* value — значение.

Тип можно получить с помощью `type()`:

```python
value = 10

print(type(value))
# <class 'int'>
```

Идентичность объекта можно проверить с помощью `id()`:

```python
value = 10

print(id(value))
```

Оператор `is` используется для сравнения идентичности двух объектов:

```python
a = []
b = a

print(a is b)
# True
```

Оператор `==`, напротив, сравнивает значения объектов:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
# True

print(a is b)
# False
```

`==` и `is` выполняют разные задачи и не должны рассматриваться как взаимозаменяемые операторы.

---

### Numeric Types

Python предоставляет три основных встроенных числовых типа:

* `int`;
* `float`;
* `complex`.

#### `int`

`int` представляет целые числа.

```python
age = 27
temperature = -10
large_number = 100000000000000000000
```

Целые числа в Python имеют неограниченную точность.

```python
number = 10 ** 100
print(number)
```

Целые числа могут записываться также в двоичной, восьмеричной и шестнадцатеричной системах:

```python
binary = 0b1010
octal = 0o12
hexadecimal = 0xA
```

Все три значения равны `10`.

---

### `float`

`float` представляет числа с плавающей точкой.

```python
price = 19.99
temperature = -3.5
```

Также используются числовые литералы с экспоненциальной записью:

```python
value = 1.5e3
```

Значение `value` равно `1500.0`.

Точность и внутреннее представление `float` зависят от реализации и платформы. В CPython обычно используется представление double precision.

Из-за особенностей представления чисел с плавающей точкой некоторые десятичные значения нельзя представить точно:

```python
result = 0.1 + 0.2

print(result)
# 0.30000000000000004
```

Поэтому сравнение результатов вычислений с `float` требует осторожности.

---

### `complex`

`complex` представляет комплексные числа.

Комплексное число имеет действительную и мнимую части:

```python
number = 3 + 4j
```

Доступ к частям осуществляется через `real` и `imag`:

```python
number = 3 + 4j

print(number.real)
# 3.0

print(number.imag)
# 4.0
```

Комплексные числа можно создавать с помощью `complex()`:

```python
number = complex(3, 4)
```

---

### Boolean Type

`bool` представляет логические значения.

В Python существуют два объекта типа `bool`:

```python
True
False
```

Пример:

```python
is_active = True
is_deleted = False
```

`bool` является подклассом `int`.

Поэтому в числовом контексте:

```python
print(True + True)
# 2

print(False + 10)
# 10
```

`True` ведёт себя как `1`, а `False` — как `0`.

Несмотря на это, для явного преобразования логического значения в число рекомендуется использовать `int()`.

---

### String Type

`str` используется для представления текстовых данных.

Строки можно создавать с помощью одинарных или двойных кавычек:

```python
name = 'Python'
language = "Python"
```

Также поддерживаются многострочные строки:

```python
text = """This is
a multiline
string."""
```

Строки являются последовательностями Unicode-символов.

К отдельным символам можно обращаться по индексу:

```python
word = "Python"

print(word[0])
# P
```

Можно получать срезы:

```python
word = "Python"

print(word[0:3])
# Pyt
```

Строки являются неизменяемыми объектами.

Следующий код не изменяет существующую строку:

```python
word = "Python"

# word[0] = "J"
```

Такая операция приводит к `TypeError`.

Для получения новой строки используется создание нового объекта:

```python
word = "Python"
word = "J" + word[1:]

print(word)
# Jython
```

---

### Sequence Types

Основными встроенными типами последовательностей являются:

* `list`;
* `tuple`;
* `range`.

Последовательность предоставляет упорядоченный набор элементов и обычно поддерживает операции индексирования, срезов, определения длины и проверки принадлежности.

Например:

```python
numbers = [10, 20, 30]

print(numbers[0])
# 10

print(len(numbers))
# 3

print(20 in numbers)
# True
```

---

### Mutable and Immutable Types

Объекты Python могут быть изменяемыми или неизменяемыми.

**Mutable** — изменяемые объекты. Их значение может изменяться после создания.

Примеры:

```python
numbers = [1, 2, 3]
numbers.append(4)
```

Список изменился, но объект списка остался тем же.

Основные изменяемые встроенные типы:

* `list`;
* `dict`;
* `set`;
* `bytearray`.

**Immutable** — неизменяемые объекты. Их значение нельзя изменить после создания.

К неизменяемым относятся, например:

* `int`;
* `float`;
* `complex`;
* `bool`;
* `str`;
* `tuple`;
* `frozenset`.

Например:

```python
x = 10
```

Нельзя изменить объект `10`. Операция:

```python
x += 1
```

приводит к связыванию имени `x` с другим объектом, представляющим `11`.

---

### List

`list` — изменяемая последовательность.

```python
numbers = [1, 2, 3]
```

Элементы списка можно изменять:

```python
numbers[0] = 100

print(numbers)
# [100, 2, 3]
```

Список может содержать объекты разных типов:

```python
values = [10, "Python", True, 3.14]
```

---

### Tuple

`tuple` — неизменяемая последовательность.

```python
coordinates = (10, 20)
```

После создания элементы кортежа нельзя заменить:

```python
coordinates = (10, 20)

# coordinates[0] = 100
```

Это приводит к `TypeError`.

Кортеж может содержать объекты разных типов:

```python
user = ("Roman", 27, True)
```

---

### Set

`set` — изменяемое множество уникальных хешируемых объектов.

```python
numbers = {1, 2, 3}
```

Дубликаты не сохраняются:

```python
numbers = {1, 2, 2, 3}

print(numbers)
# {1, 2, 3}
```

Множества поддерживают операции объединения, пересечения, разности и проверки принадлежности.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
# {1, 2, 3, 4, 5}

print(a & b)
# {3}
```

Множества не поддерживают индексирование и срезы.

---

### Dictionary

`dict` представляет отображение ключей на значения.

```python
user = {
    "name": "Roman",
    "age": 27
}
```

Получение значения:

```python
print(user["name"])
# Roman
```

Словари являются изменяемыми.

```python
user["age"] = 28
```

Ключи словаря должны быть хешируемыми объектами.

Например, строка, число или кортеж из хешируемых объектов могут использоваться в качестве ключа:

```python
data = {
    "name": "Roman",
    1: "one",
    (1, 2): "coordinates"
}
```

Список не может использоваться как ключ словаря:

```python
# data = {[1, 2]: "value"}
```

---

### None

`None` — специальный объект, обозначающий отсутствие значения.

```python
result = None
```

Тип объекта `None`:

```python
print(type(None))
# <class 'NoneType'>
```

`None` часто используется:

* когда функция не возвращает полезное значение;
* для обозначения отсутствующего значения;
* как значение по умолчанию;
* для обозначения состояния, в котором значение ещё не задано.

Для проверки используется `is`:

```python
value = None

if value is None:
    print("No value")
```

---

### Truth Value

Практически любой объект в Python может быть проверен на истинность.

Объекты считаются истинными, если для них не определено обратное поведение.

Основные значения, считающиеся ложными:

* `None`;
* `False`;
* ноль числового типа;
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

bool([1, 2, 3])
# True
```

Истинность объекта используется, например, в `if` и `while`:

```python
items = []

if items:
    print("Items exist")
else:
    print("Items are empty")
```

Для пользовательских классов truth value может определяться методами `__bool__()` или `__len__()`.

---

### Type Conversion

Python предоставляет встроенные функции для преобразования значений между типами.

Основные функции:

* `int()`;
* `float()`;
* `complex()`;
* `bool()`;
* `str()`;
* `list()`;
* `tuple()`;
* `set()`;
* `dict()`.

Примеры:

```python
number = int("42")
price = float("19.99")
text = str(42)
flag = bool(1)
```

Некоторые преобразования могут завершиться ошибкой:

```python
number = int("hello")
```

Результат:

```text
ValueError
```

Преобразование не обязательно сохраняет всю информацию исходного объекта:

```python
value = int(3.9)

print(value)
# 3
```

---

### Numeric Type Conversion

При арифметических операциях над разными числовыми типами Python выполняет соответствующее расширение типа.

Например:

```python
result = 10 + 2.5

print(type(result))
# <class 'float'>
```

Целое число преобразуется к `float`.

При участии `complex` результат становится комплексным:

```python
result = 10 + 2j

print(type(result))
# <class 'complex'>
```

`complex` нельзя напрямую преобразовать в `float` или `int` без предварительного извлечения нужной части.

---

## Syntax

Создание объектов различных типов:

```python
integer = 42
floating_point = 3.14
complex_number = 2 + 3j

boolean = True

string = "Python"

list_value = [1, 2, 3]
tuple_value = (1, 2, 3)
set_value = {1, 2, 3}
dict_value = {"name": "Roman"}

none_value = None
```

Получение типа:

```python
value = 42

type(value)
```

Проверка типа:

```python
value = 42

isinstance(value, int)
```

Преобразование:

```python
int("42")
float("3.14")
str(42)
bool(1)
list("abc")
tuple([1, 2, 3])
set([1, 2, 2, 3])
```

Проверка идентичности:

```python
a = None
b = None

a is b
```

Сравнение значений:

```python
a = [1, 2]
b = [1, 2]

a == b
```

---

## Rules

### Every value is an object

Все данные Python представлены объектами или отношениями между объектами.

Объекты имеют тип, значение и идентичность.

---

### Object type does not change

После создания объекта его тип не изменяется.

```python
value = 10
```

Объект `10` имеет тип `int`.

Если написать:

```python
value = "10"
```

изменяется не тип существующего объекта, а объект, с которым связано имя `value`.

---

### Variables do not have fixed types

Тип относится к объекту, а не к имени.

```python
value = 10
value = "Python"
value = [1, 2, 3]
```

Имя `value` может последовательно связываться с объектами разных типов.

---

### Mutable objects can change their value

Изменяемый объект можно изменить после создания:

```python
numbers = [1, 2, 3]

numbers.append(4)
```

---

### Immutable objects cannot be changed

Неизменяемый объект нельзя изменить после создания:

```python
text = "Python"

# text[0] = "J"
```

Вместо изменения создаётся новый объект:

```python
text = "J" + text[1:]
```

---

### `bool` has two values

Тип `bool` имеет два значения:

```python
True
False
```

`bool` является подклассом `int`, поэтому `True` и `False` могут участвовать в некоторых числовых операциях как `1` и `0`.

---

### Dictionary keys must be hashable

Ключи словаря должны быть хешируемыми.

Допустимо:

```python
data = {
    "name": "Roman",
    1: "one",
    (1, 2): "tuple"
}
```

Недопустимо использовать изменяемый список в качестве ключа:

```python
# data = {
#     [1, 2]: "value"
# }
```

---

### Set elements must be hashable

Элементы множества также должны быть хешируемыми.

Допустимо:

```python
values = {1, "Python", (1, 2)}
```

Недопустимо:

```python
# values = {[1, 2], [3, 4]}
```

---

### Boolean operations use truth values

`if` и `while` могут работать с объектами напрямую:

```python
items = []

if items:
    print("Not empty")
```

Python проверяет truth value объекта, а не требует, чтобы результат был именно `True` или `False`.

---

### `and` and `or` return operands

Логические операторы `and` и `or` имеют особое поведение.

Они возвращают один из своих операндов, а не обязательно значение типа `bool`.

```python
result = "Python" and 42

print(result)
# 42
```

```python
result = "" or "default"

print(result)
# default
```

Это поведение часто используется для выбора значения по умолчанию.

---

## Examples

### Example 1 — Basic data types

```python
age = 27
price = 19.99
name = "Roman"
is_active = True

print(type(age))
print(type(price))
print(type(name))
print(type(is_active))
```

Каждое значение имеет свой тип.

---

### Example 2 — Mutable list

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
# [1, 2, 3, 4]
```

Список изменяется после создания.

---

### Example 3 — Immutable string

```python
text = "Python"

new_text = "J" + text[1:]

print(text)
# Python

print(new_text)
# Jython
```

Исходная строка остаётся неизменной.

---

### Example 4 — Type conversion

```python
age_text = "27"

age = int(age_text)

print(age)
print(type(age))
```

Строка преобразуется в целое число.

---

### Example 5 — Truth value

```python
values = []

if values:
    print("Not empty")
else:
    print("Empty")
```

Пустой список имеет ложное truth value.

---

### Example 6 — Different numeric types

```python
a = 10
b = 2.5

result = a + b

print(result)
# 12.5

print(type(result))
# <class 'float'>
```

При смешанной арифметике `int` и `float` результат имеет тип `float`.

---

### Example 7 — Dictionary

```python
user = {
    "name": "Roman",
    "age": 27
}

user["age"] = 28

print(user)
```

Словарь является изменяемым объектом.

---

### Example 8 — Set removes duplicates

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
# {1, 2, 3}
```

Множество хранит только уникальные элементы.

---

### Example 9 — `is` versus `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
# True

print(a is b)
# False

print(a is c)
# True
```

`==` сравнивает значения, а `is` проверяет идентичность объектов.

---

### Example 10 — `None`

```python
result = None

if result is None:
    print("No result")
```

`None` используется для представления отсутствующего значения.

---

## Edge Cases

### Floating-point precision

Десятичные дроби не всегда могут быть представлены точно в двоичной системе:

```python
result = 0.1 + 0.2

print(result)
# 0.30000000000000004
```

Поэтому результат арифметики с `float` не всегда следует сравнивать с десятичным литералом через `==`.

---

### Boolean values are integers

`bool` является подклассом `int`:

```python
print(isinstance(True, int))
# True
```

Поэтому:

```python
print(True + 2)
# 3
```

Несмотря на это, логические значения следует использовать прежде всего для представления истины и лжи, а не как замену обычным числам.

---

### Empty objects are often false

Разные типы имеют ложное значение для пустых объектов:

```python
bool("")
# False

bool([])
# False

bool(())
# False

bool({})
# False

bool(set())
# False
```

Это позволяет писать:

```python
items = []

if not items:
    print("No items")
```

---

### Immutable container can contain mutable objects

Неизменяемость контейнера не означает, что все объекты внутри него неизменяемы.

Например:

```python
data = ([1, 2], "Python")

data[0].append(3)

print(data)
# ([1, 2, 3], 'Python')
```

Сам кортеж не позволяет заменить свой первый элемент:

```python
# data[0] = [10, 20]
```

Но объект списка, на который он ссылается, остаётся изменяемым.

---

### `and` and `or` do not always return bool

```python
value = "Python" or ""

print(value)
# Python
```

Результатом является один из операндов.

Поэтому:

```python
result = 0 or 100
```

даёт:

```text
100
```

а не `True`.

---

### Numeric equality across types

Числовые объекты разных встроенных числовых типов могут сравниваться по значению:

```python
print(1 == 1.0)
# True

print(True == 1)
# True
```

Это не означает, что объекты имеют одинаковый тип:

```python
print(type(1))
# <class 'int'>

print(type(1.0))
# <class 'float'>
```

---

## Common Mistakes

### Mistake 1 — Confusing `is` and `==`

Неправильно использовать `is` для обычного сравнения значений:

```python
a = [1, 2]
b = [1, 2]

a is b
# False
```

Для сравнения значений используется:

```python
a == b
# True
```

`is` следует использовать для проверки идентичности, например:

```python
value is None
```

---

### Mistake 2 — Assuming variables have fixed types

Python не закрепляет тип за именем:

```python
value = 10
value = "10"
```

Это не изменение типа переменной, а повторное связывание имени с другим объектом.

---

### Mistake 3 — Trying to modify an immutable object

Нельзя изменить отдельный символ строки:

```python
text = "Python"

# text[0] = "J"
```

Строки неизменяемы.

Нужно создать новую строку:

```python
text = "J" + text[1:]
```

---

### Mistake 4 — Expecting `int()` to preserve a fractional part

```python
value = int(3.9)

print(value)
# 3
```

Преобразование `float` в `int` не сохраняет дробную часть.

---

### Mistake 5 — Using mutable objects as dictionary keys

Неправильно:

```python
# data = {
#     [1, 2]: "value"
# }
```

Список является изменяемым и не может использоваться как ключ словаря.

Можно использовать кортеж из хешируемых объектов:

```python
data = {
    (1, 2): "value"
}
```

---

### Mistake 6 — Expecting `bool()` to return only `True` for non-zero numbers

`bool()` преобразует значение согласно правилам truth value:

```python
bool(0)
# False

bool(1)
# True

bool(-10)
# True
```

Для чисел ноль является ложным, а ненулевые значения — истинными.

---

### Mistake 7 — Assuming `and` and `or` return booleans

```python
result = "hello" and 10

print(result)
# 10
```

`and` и `or` возвращают один из операндов.

Если нужен именно `bool`, можно использовать:

```python
result = bool("hello" and 10)
```

---

## Related Concepts

* Objects
* Values
* Types
* `type()`
* `isinstance()`
* `id()`
* `is`
* `==`
* Variables
* Assignment
* `int`
* `float`
* `complex`
* `bool`
* `str`
* `list`
* `tuple`
* `set`
* `dict`
* `None`
* Mutable Objects
* Immutable Objects
* Truth Value Testing
* Type Conversion
* Numeric Operations
* Sequences
* Mappings
* Hashability

---

## Key Takeaways

* В Python все данные представлены объектами.
* Каждый объект имеет идентичность, тип и значение.
* Тип объекта определяет доступные операции и возможные значения.
* Тип объекта можно получить с помощью `type()`.
* `is` проверяет идентичность объектов, а `==` сравнивает их значения.
* Python использует динамическую типизацию: имя может быть связано с объектами разных типов.
* Основные числовые типы — `int`, `float` и `complex`.
* `bool` имеет два значения: `True` и `False`, и является подклассом `int`.
* `str` представляет текст и является неизменяемым типом.
* `list` — изменяемая последовательность.
* `tuple` — неизменяемая последовательность.
* `set` хранит уникальные хешируемые элементы.
* `dict` хранит соответствия между хешируемыми ключами и произвольными значениями.
* `None` представляет отсутствие значения.
* Изменяемые объекты могут изменять своё содержимое после создания.
* Неизменяемые объекты нельзя изменить после создания.
* Truth value позволяет использовать объекты непосредственно в `if` и `while`.
* `int()`, `float()`, `str()`, `bool()` и другие конструкторы используются для преобразования объектов.
* При смешанной арифметике числовых типов Python выполняет соответствующее преобразование типов.
* Ключи словаря и элементы множества должны быть хешируемыми.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Data Model — Objects, values and types
* Python Standard Types — Built-in Types
* Python Standard Types — Truth Value Testing
* Python Standard Types — Numeric Types
* Python Standard Types — Boolean Type
* Python Standard Types — Sequence Types
* Python Standard Types — Text Sequence Type
* Python Standard Types — Set Types
* Python Standard Types — Mapping Types
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html
* Official documentation: https://docs.python.org/3.14/library/stdtypes.html
