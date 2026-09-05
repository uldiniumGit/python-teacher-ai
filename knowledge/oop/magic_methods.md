# Magic Methods

## Definition

Magic methods, также называемые **special methods**, — это методы Python с именами специального вида, обычно начинающимися и заканчивающимися двумя символами подчёркивания, например `__init__`, `__str__`, `__len__`, `__getitem__` и `__add__`.

Они позволяют пользовательским классам определять поведение стандартных операций Python. Интерпретатор вызывает такие методы автоматически при использовании специального синтаксиса или встроенных функций.

Например, выражение `x + y` может вызывать `x.__add__(y)`, `len(x)` — `x.__len__()`, а `x[key]` — `x.__getitem__(key)`.

В официальной документации Python эта группа методов рассматривается в разделе **Special method names** модели данных.

---

## Purpose

Magic methods используются для интеграции пользовательских объектов с синтаксисом и протоколами Python.

Они позволяют:

* задавать поведение объектов при создании;
* определять строковое представление объектов;
* поддерживать арифметические операции;
* реализовывать сравнение объектов;
* делать объекты итерируемыми;
* поддерживать операции `len()`, `in`, `[]` и `del`;
* определять логическое значение объекта;
* реализовывать работу с контекстным менеджером `with`;
* управлять доступом к атрибутам;
* определять поведение объектов как вызываемых объектов;
* реализовывать асинхронные протоколы;
* настраивать работу объектов с `async for`, `async with` и другими конструкциями Python.

Magic methods особенно полезны при создании собственных классов, которые должны вести себя подобно встроенным типам Python.

---

## Core Concepts

### Special Method Invocation

Специальные методы обычно вызываются не напрямую, а автоматически интерпретатором.

Например:

```python
class UserList:
    def __len__(self):
        return 3


users = UserList()

print(len(users))
```

При вызове `len(users)` Python использует специальный метод `__len__()` класса.

Аналогично:

```python
class Number:
    def __add__(self, other):
        return 10


x = Number()

print(x + 5)
```

Операция `x + 5` использует `__add__()`.

Специальные методы обеспечивают механизм, который Python использует для поддержки операторов и различных протоколов объектов.

### Special Method Lookup

Неявный поиск специальных методов отличается от обычного поиска атрибутов экземпляра.

Специальные методы для неявных операций должны определяться на уровне класса, а не только у конкретного экземпляра.

Например:

```python
class Example:
    pass


obj = Example()
obj.__len__ = lambda: 5

len(obj)
```

Такой код не заставит `len(obj)` использовать `obj.__len__`. Python выполняет специальный поиск метода через тип объекта.

Правильный вариант:

```python
class Example:
    def __len__(self):
        return 5


obj = Example()

print(len(obj))
```

Это важно учитывать при реализации magic methods: присваивание специального метода отдельному экземпляру не является надёжным способом изменить поведение соответствующей встроенной операции.

### Object Construction

`__new__()` отвечает за создание нового экземпляра, а `__init__()` — за его инициализацию после создания.

```python
class User:
    def __new__(cls, name):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self, name):
        print("Initializing object")
        self.name = name


user = User("Roman")
```

Сначала вызывается `__new__()`. Если он возвращает экземпляр `cls`, Python затем вызывает `__init__()` для этого экземпляра.

`__new__()` особенно важен при наследовании от неизменяемых типов, таких как `int`, `str` или `tuple`.

### Object Representation

Для строкового представления объекта используются несколько специальных методов.

`__repr__()` предназначен для официального, информативного представления объекта:

```python
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User(name={self.name!r})"
```

`repr()`:

```python
user = User("Roman")

print(repr(user))
```

может вернуть:

```text
User(name='Roman')
```

`__str__()` предназначен для более удобного представления объекта:

```python
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


user = User("Roman")

print(user)
```

`__repr__()` обычно ориентирован на отладку и однозначное представление объекта, а `__str__()` — на удобное отображение пользователю.

Если класс определяет `__repr__()`, но не определяет `__str__()`, то `__repr__()` также используется для неформального строкового представления.

### Comparison Methods

Magic methods позволяют определять поведение операторов сравнения:

| Operator | Method     |
| -------- | ---------- |
| `<`      | `__lt__()` |
| `<=`     | `__le__()` |
| `==`     | `__eq__()` |
| `!=`     | `__ne__()` |
| `>`      | `__gt__()` |
| `>=`     | `__ge__()` |

Пример:

```python
class User:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


user1 = User(27)
user2 = User(27)

print(user1 == user2)
```

Результат:

```text
True
```

Эти методы называются **rich comparison methods**.

### Arithmetic Methods

Magic methods позволяют переопределять арифметические операторы.

Основные методы:

```text
__add__       +
__sub__       -
__mul__       *
__matmul__    @
__truediv__   /
__floordiv__  //
__mod__       %
__pow__       **
```

Также существуют отражённые операции:

```text
__radd__
__rsub__
__rmul__
__rmatmul__
__rtruediv__
__rfloordiv__
__rmod__
__rpow__
```

И in-place операции:

```text
__iadd__
__isub__
__imul__
__imatmul__
__itruediv__
__ifloordiv__
__imod__
__ipow__
```

Пример:

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


a = Number(10)
b = Number(5)

result = a + b

print(result.value)
```

### Container Methods

Magic methods позволяют создавать собственные контейнеры.

Основные методы:

```text
__len__()
__getitem__()
__setitem__()
__delitem__()
__contains__()
__iter__()
__reversed__()
```

Например:

```python
class Numbers:
    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]


numbers = Numbers([10, 20, 30])

print(len(numbers))
print(numbers[1])
```

Метод `__getitem__()` используется для доступа через `obj[key]`.

Метод `__contains__()` используется для операций `in` и `not in`.

Если `__contains__()` отсутствует, Python сначала пытается использовать `__iter__()`, а затем старый протокол последовательности через `__getitem__()`.

### Iteration

`__iter__()` определяет получение итератора объекта.

```python
class Numbers:
    def __init__(self, values):
        self.values = values

    def __iter__(self):
        return iter(self.values)


numbers = Numbers([1, 2, 3])

for number in numbers:
    print(number)
```

`__reversed__()` используется встроенной функцией `reversed()` для обратной итерации.

Если `__reversed__()` не определён, `reversed()` может использовать последовательностный протокол через `__len__()` и `__getitem__()`.

### Truth Value Testing

`__bool__()` определяет логическое значение объекта:

```python
class User:
    def __init__(self, active):
        self.active = active

    def __bool__(self):
        return self.active


user = User(True)

if user:
    print("Active")
```

Если `__bool__()` не определён, Python пытается использовать `__len__()`.

Объект считается ложным, если `__bool__()` возвращает `False` или если отсутствует `__bool__()`, а `__len__()` возвращает `0`.

Если оба метода отсутствуют, экземпляры объекта считаются истинными.

### Hashing

`__hash__()` определяет хеш объекта и используется встроенной функцией `hash()`.

Хешируемые объекты могут использоваться, например, в качестве ключей словаря или элементов `set`.

```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __hash__(self):
        return hash(self.user_id)

    def __eq__(self, other):
        return self.user_id == other.user_id
```

При реализации `__hash__()` необходимо учитывать согласованность с `__eq__()`: объекты, которые считаются равными, должны иметь одинаковый хеш.

### Attribute Access

Python предоставляет специальные методы для управления доступом к атрибутам:

```text
__getattribute__()
__getattr__()
__setattr__()
__delattr__()
```

Например, `__getattr__()` вызывается, когда обычный поиск атрибута не смог его найти:

```python
class User:
    def __getattr__(self, name):
        return f"Unknown attribute: {name}"


user = User()

print(user.email)
```

Методы управления атрибутами позволяют создавать прокси-объекты, lazy attributes, динамические атрибуты и другие механизмы.

### Callable Objects

Метод `__call__()` позволяет сделать экземпляр класса вызываемым как функцию.

```python
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f"Hello, {self.name}"


greeter = Greeter("Roman")

print(greeter())
```

После определения `__call__()` объект можно использовать с синтаксисом вызова:

```python
greeter()
```

### Context Managers

Для поддержки конструкции `with` используются:

```text
__enter__()
__exit__()
```

Пример:

```python
class Manager:
    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit")


with Manager():
    print("Inside")
```

`__enter__()` вызывается при входе в контекст, а `__exit__()` — при выходе из него.

### Async Protocols

Python также предоставляет специальные методы для асинхронных протоколов:

```text
__aenter__()
__aexit__()
__aiter__()
__anext__()
```

Они используются конструкциями:

```python
async with ...
async for ...
```

Например:

```python
class AsyncManager:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        pass
```

---

## Syntax

Общий синтаксис magic method:

```python
class ClassName:

    def __special_method__(self, ...):
        ...
```

Пример нескольких наиболее распространённых методов:

```python
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User({self.name!r})"

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __call__(self):
        return self.name.upper()
```

Использование:

```python
user = User("Roman")

print(user)
print(repr(user))
print(len(user))
print(user == User("Roman"))
print(user())
```

---

## Rules

1. Magic methods определяются внутри класса.
2. Неявный вызов специальных методов выполняется через тип объекта, поэтому установка magic method только в `__dict__` экземпляра не изменяет соответствующее поведение встроенной операции.
3. Возвращаемое значение magic method должно соответствовать требованиям конкретного протокола.
4. `__len__()` должен возвращать целое число, большее или равное `0`.
5. `__bool__()` должен возвращать `True` или `False`.
6. `__str__()` и `__repr__()` должны возвращать объект типа `str`.
7. `__iter__()` должен возвращать итератор.
8. При переопределении `__eq__()` необходимо учитывать взаимосвязь с `__hash__()`.
9. `__new__()` отвечает за создание объекта, а `__init__()` — за его инициализацию.
10. Если `__new__()` не возвращает экземпляр `cls`, `__init__()` для этого объекта не вызывается.
11. Специальный метод можно установить в `None`, чтобы соответствующая операция считалась недоступной. Например, `__iter__ = None` запрещает использование объекта как итерируемого объекта через `iter()`.

---

## Examples

### Custom Container

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items


cart = ShoppingCart()

cart.add("Book")
cart.add("Laptop")

print(len(cart))
print(cart[0])
print("Laptop" in cart)
```

### Custom Numeric Type

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __repr__(self):
        return f"Money({self.amount})"


a = Money(100)
b = Money(50)

print(a + b)
print(a - b)
```

### Comparable Objects

```python
class Product:
    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price


cheap = Product(100)
expensive = Product(200)

print(cheap < expensive)
print(cheap == expensive)
```

---

## Edge Cases

### Special Method Defined Only on Instance

```python
class Example:
    pass


obj = Example()
obj.__len__ = lambda: 5

print(obj.__len__())
```

Прямой вызов метода работает:

```text
5
```

Но:

```python
len(obj)
```

не использует установленный таким образом метод и приводит к ошибке, потому что неявный специальный поиск выполняется через класс объекта.

### Missing `__bool__()`

Если класс не определяет `__bool__()`, Python может использовать `__len__()`:

```python
class Collection:
    def __len__(self):
        return 0


collection = Collection()

print(bool(collection))
```

Результат:

```text
False
```

### `__repr__()` Without `__str__()`

```python
class User:
    def __repr__(self):
        return "User()"


user = User()

print(str(user))
```

Если `__str__()` отсутствует, `__repr__()` используется также для неформального представления объекта.

### `__iter__()` Set to `None`

```python
class NotIterable:
    __iter__ = None


obj = NotIterable()

iter(obj)
```

Такой класс явно сообщает Python, что объект не поддерживает протокол итерации. В этом случае `iter()` не переходит к fallback через `__getitem__()`.

---

## Common Mistakes

### Calling Magic Methods Instead of Using the Protocol

Не следует без необходимости писать:

```python
obj.__len__()
```

В обычном коде предпочтительнее:

```python
len(obj)
```

А вместо:

```python
obj.__str__()
```

использовать:

```python
str(obj)
```

Magic methods прежде всего предназначены для интеграции объекта с протоколами и синтаксисом Python.

### Defining Special Methods on Instances

Неправильно полагаться на:

```python
obj.__len__ = ...
```

для изменения поведения:

```python
len(obj)
```

Специальные методы для неявных операций должны определяться на уровне класса.

### Incorrect Return Type

Например, `__len__()` не должен возвращать строку:

```python
class Example:
    def __len__(self):
        return "10"
```

`__len__()` должен возвращать целое число `>= 0`.

### Confusing `__str__()` and `__repr__()`

`__str__()` предназначен для удобного строкового представления, тогда как `__repr__()` должен стремиться к информативному и однозначному представлению объекта, полезному прежде всего для разработчика и отладки.

### Incorrect `__hash__()` Implementation

Нельзя реализовывать `__hash__()` независимо от логики `__eq__()`. Если два объекта равны согласно `__eq__()`, они должны иметь одинаковый хеш.

---

## Related Concepts

* Object model
* Data model
* Classes
* Instances
* Operator overloading
* Iterators
* Iterables
* Sequence protocol
* Mapping protocol
* Context managers
* Asynchronous iterators
* Descriptors
* Attribute access
* `__new__()`
* `__init__()`
* `__repr__()`
* `__str__()`
* `__eq__()`
* `__hash__()`
* `__getitem__()`
* `__iter__()`
* `__call__()`

---

## Key Takeaways

* Magic methods — это специальные методы Python, определяющие поведение пользовательских объектов.
* Они позволяют объектам работать со встроенными функциями, операторами и синтаксическими конструкциями Python.
* `__init__()` отвечает за инициализацию объекта, а `__new__()` — за его создание.
* `__repr__()` используется для информативного представления объекта, а `__str__()` — для удобного отображения.
* `__len__()` интегрирует объект с `len()`.
* `__bool__()` определяет поведение объекта в логическом контексте.
* `__getitem__()`, `__setitem__()` и `__delitem__()` позволяют реализовать индексирование и работу с элементами.
* `__iter__()` позволяет объекту поддерживать итерацию.
* `__contains__()` управляет поведением `in` и `not in`.
* Arithmetic magic methods позволяют реализовать операторы вроде `+`, `-`, `*` и `/`.
* Comparison magic methods позволяют определить поведение `==`, `<`, `>`, `<=`, `>=` и `!=`.
* Неявный поиск специальных методов выполняется через тип объекта, поэтому определение magic method только у экземпляра не заменяет метод класса.
* Magic methods являются частью Python Data Model и позволяют пользовательским классам вести себя как встроенные типы Python.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Data Model — Special method names
* Python Language Reference — Data Model — Special method lookup
* Python Language Reference — Data Model — Basic customization
* Python Language Reference — Data Model — Emulating container types
* Python Language Reference — Data Model — Special method names
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html
* Official documentation: https://docs.python.org/3.14/reference/index.html
