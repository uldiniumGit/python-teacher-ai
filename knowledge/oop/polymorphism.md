# Polymorphism

## Definition

Полиморфизм — это способность разных объектов поддерживать общий интерфейс, но реализовывать одинаковую операцию по-разному.

В Python полиморфизм позволяет писать код, который работает с разными типами объектов без необходимости знать их конкретный класс. Важным механизмом такого подхода является duck typing: объект рассматривается с точки зрения поддерживаемого им поведения, а не только его типа.

---

## Purpose

Полиморфизм используется для создания гибкого и расширяемого кода.

Он позволяет:

* использовать одну функцию с объектами разных типов;
* работать с объектами через общий интерфейс;
* заменять одну реализацию другой без изменения кода, который использует объект;
* уменьшать количество проверок конкретных типов;
* добавлять новые классы без изменения существующего кода;
* отделять код, использующий объект, от конкретной реализации объекта.

Полиморфизм обычно применяется при проектировании классов, функций, интерфейсов и систем, работающих с несколькими реализациями одного поведения.

---

## Core Concepts

### Common Interface

Общий интерфейс — это набор операций, которые объект должен поддерживать для использования в определенном контексте.

В Python интерфейс не обязательно должен быть представлен отдельным базовым классом. Он может существовать неформально: например, функция может ожидать от объекта наличие метода `save()`.

```python
def save_data(storage):
    storage.save()
```

Функции `save_data()` не требуется знать конкретный класс `storage`. Ей важно только наличие метода `save()`.

---

### Duck Typing

Duck typing — подход, при котором при использовании объекта важнее его поддерживаемые операции, чем принадлежность к конкретному классу.

Идея заключается в том, что если объект поддерживает необходимое поведение, его можно использовать в соответствующем контексте.

```python
class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


def make_sound(animal):
    return animal.speak()
```

`Dog` и `Cat` не обязаны наследоваться от одного класса. Функции `make_sound()` достаточно наличия метода `speak()`.

---

### Polymorphism Through Inheritance

Наследование является одним из способов реализации полиморфизма.

Базовый класс может определять общий метод, а подклассы могут переопределять его и предоставлять собственную реализацию.

```python
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"
```

Теперь один и тот же вызов `speak()` дает разный результат в зависимости от объекта.

```python
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

---

### Method Overriding

Переопределение метода происходит, когда подкласс предоставляет собственную реализацию метода, уже определенного в базовом классе.

```python
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"
```

При вызове:

```python
animal = Dog()
print(animal.speak())
```

будет использована реализация `Dog.speak()`.

Переопределение позволяет разным подклассам предоставлять различное поведение через один и тот же интерфейс.

---

### Polymorphism Without Inheritance

Полиморфизм в Python не требует обязательного использования наследования.

Несколько независимых классов могут предоставлять одинаковый метод.

```python
class FileLogger:
    def write(self, message):
        print(f"File: {message}")


class ConsoleLogger:
    def write(self, message):
        print(f"Console: {message}")


def log_message(logger, message):
    logger.write(message)
```

Функция `log_message()` может работать с обоими классами:

```python
log_message(FileLogger(), "Hello")
log_message(ConsoleLogger(), "Hello")
```

Это пример duck typing и полиморфного поведения без общей иерархии классов.

---

### Built-in Polymorphism

Многие встроенные функции Python работают с объектами разных типов через общий интерфейс.

Например, функция `len()` применяется к строкам, спискам, кортежам и другим объектам, поддерживающим операцию определения длины.

```python
print(len("Python"))
print(len([1, 2, 3]))
print(len((10, 20)))
```

Код использует одну функцию независимо от конкретного типа объекта.

---

### Operator Polymorphism

Операторы Python также могут иметь разное поведение для разных типов.

Например, `+` используется для числового сложения и объединения последовательностей.

```python
print(2 + 3)
print("Hello " + "Python")
print([1, 2] + [3, 4])
```

Одна и та же запись `a + b` может выполнять разные действия в зависимости от типов объектов.

---

### Function Polymorphism

Функция может принимать объекты разных типов, если все они поддерживают необходимые операции.

```python
def get_length(value):
    return len(value)
```

Такая функция может работать с разными объектами:

```python
print(get_length("Python"))
print(get_length([1, 2, 3]))
print(get_length((10, 20)))
```

Функции не требуется создавать отдельную реализацию для каждого конкретного типа.

---

### EAFP

EAFP означает "Easier to Ask for Forgiveness than Permission".

Это распространенный в Python подход, при котором код сначала выполняет необходимую операцию, а затем обрабатывает ожидаемое исключение, если операция невозможна.

```python
def read_data(source):
    try:
        return source.read()
    except AttributeError:
        return None
```

Такой подход может использоваться вместе с duck typing.

Однако нельзя без необходимости перехватывать слишком широкий класс исключений, поскольку это может скрыть настоящую ошибку внутри вызываемого метода.

---

### Type Checking

Python предоставляет `isinstance()` для проверки принадлежности объекта классу или его подклассу.

```python
if isinstance(value, Dog):
    value.speak()
```

Проверка типа иногда необходима, когда поведение программы действительно зависит от конкретного типа.

Однако большое количество проверок конкретных классов может сделать код менее гибким.

Вместо:

```python
if isinstance(value, Dog):
    ...
elif isinstance(value, Cat):
    ...
```

часто можно использовать общий интерфейс:

```python
value.speak()
```

---

### Abstract Base Classes

Абстрактные базовые классы позволяют явно определить общий интерфейс для группы классов.

Для этого используется модуль `abc`.

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```

Подклассы должны реализовать абстрактный метод:

```python
class Dog(Animal):
    def speak(self):
        return "Woof"
```

Абстрактные базовые классы полезны, когда общий интерфейс должен быть явно определен и соблюдаться подклассами.

---

### Protocol

`typing.Protocol` позволяет описывать общий интерфейс на основе структуры объекта.

```python
from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str:
        ...
```

Класс не обязан явно наследоваться от `Speaker`, чтобы соответствовать такому протоколу с точки зрения статической проверки типов.

```python
class Dog:
    def speak(self) -> str:
        return "Woof"


class Robot:
    def speak(self) -> str:
        return "Beep"
```

Оба класса предоставляют необходимый метод `speak()`.

---

## Syntax

Полиморфизм через общий интерфейс:

```python
class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


def make_sound(animal):
    return animal.speak()


print(make_sound(Dog()))
print(make_sound(Cat()))
```

Полиморфизм через наследование:

```python
class Animal:
    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"
```

Использование `isinstance()`:

```python
if isinstance(obj, Animal):
    obj.speak()
```

Использование `Protocol`:

```python
from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str:
        ...
```

---

## Rules

1. Полиморфизм позволяет использовать разные объекты через общий интерфейс.

2. Для полиморфизма в Python не обязательно использовать наследование.

3. Duck typing основывается на поддерживаемом объектом поведении.

4. Подклассы могут реализовывать общий интерфейс через переопределение методов.

5. Один и тот же вызов метода может приводить к разному поведению для разных объектов.

6. Функция может работать с объектами разных типов, если они поддерживают необходимые операции.

7. Встроенные функции Python также могут работать полиморфно с разными типами объектов.

8. Операторы Python могут выполнять разные действия в зависимости от типов операндов.

9. `isinstance()` следует использовать, когда конкретный тип действительно влияет на логику программы.

10. Не следует создавать большое количество проверок типов там, где достаточно общего интерфейса.

11. Абстрактные базовые классы позволяют явно определить обязательные методы интерфейса.

12. `typing.Protocol` позволяет описывать интерфейс на основе структуры объекта.

13. Совместимость объектов определяется не только названием методов, но и их ожидаемой сигнатурой и поведением.

---

## Examples

### Example 1 — Duck Typing

```python
class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


def make_sound(animal):
    print(animal.speak())


make_sound(Dog())
make_sound(Cat())
```

Explanation:

`make_sound()` работает с объектами разных классов. Функции не требуется знать, является объект собакой или кошкой. Она использует общий метод `speak()`.

---

### Example 2 — Inheritance and Overriding

```python
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

Explanation:

`Dog` и `Cat` наследуются от `Animal` и переопределяют метод `speak()`. Один и тот же вызов метода приводит к разным результатам.

---

### Example 3 — Independent Classes

```python
class FileStorage:
    def save(self, data):
        print(f"Saving to file: {data}")


class DatabaseStorage:
    def save(self, data):
        print(f"Saving to database: {data}")


def save_data(storage, data):
    storage.save(data)


save_data(FileStorage(), "Python")
save_data(DatabaseStorage(), "Python")
```

Explanation:

Классы не обязаны иметь общего родителя. Функция использует только общий метод `save()`.

---

### Example 4 — Built-in Function

```python
values = [
    "Python",
    [1, 2, 3],
    (10, 20)
]

for value in values:
    print(len(value))
```

Explanation:

`len()` работает с разными типами объектов, поддерживающими соответствующий протокол определения длины.

---

### Example 5 — Operator Polymorphism

```python
print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])
```

Explanation:

Оператор `+` используется для разных типов и имеет соответствующее каждому типу поведение.

---

### Example 6 — Protocol

```python
from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str:
        ...


class Dog:
    def speak(self) -> str:
        return "Woof"


class Robot:
    def speak(self) -> str:
        return "Beep"


def make_sound(speaker: Speaker):
    print(speaker.speak())


make_sound(Dog())
make_sound(Robot())
```

Explanation:

`Dog` и `Robot` не наследуются от `Speaker`, но оба предоставляют совместимый метод `speak()`. Протокол описывает необходимую структуру интерфейса.

---

## Edge Cases

### Missing Method

Если объект не предоставляет необходимый метод, полиморфный вызов не сможет выполниться.

```python
class Dog:
    def speak(self):
        return "Woof"


def make_sound(animal):
    return animal.speak()


make_sound(10)
```

У объекта `int` нет метода `speak()`, поэтому возникнет `AttributeError`.

---

### Incompatible Method Signature

Одинаковое название метода не гарантирует совместимость.

```python
class Dog:
    def speak(self):
        return "Woof"


class Robot:
    def speak(self, volume):
        return "Beep"
```

Вызов:

```python
obj.speak()
```

работает для `Dog`, но требует аргумент для `Robot`.

Поэтому при проектировании общего интерфейса необходимо учитывать сигнатуры методов.

---

### Different Semantics

Два объекта могут предоставлять метод с одинаковым именем, но выполнять совершенно разное действие.

Например, `save()` одного объекта может записывать данные в файл, а `save()` другого — отправлять данные в базу данных.

Поэтому полиморфный интерфейс должен иметь понятный контракт поведения.

---

### Overridden Method with Different Behavior

Переопределенный метод может выполнять специфическую для подкласса работу, но он должен сохранять смысл общего интерфейса.

Если код ожидает, что `speak()` возвращает строку, реализация, возвращающая совершенно другой тип или требующая дополнительных обязательных аргументов, может нарушить ожидаемый контракт.

---

### Exceptions in Duck Typing

При использовании duck typing ошибка может возникнуть только в момент выполнения операции.

```python
def process(obj):
    return obj.process()
```

Если объект не поддерживает `process()`, ошибка будет обнаружена во время выполнения.

Это является одной из особенностей динамической типизации Python.

---

## Common Mistakes

### Excessive Type Checking

Неправильный подход:

```python
def make_sound(animal):
    if isinstance(animal, Dog):
        return animal.speak()
    elif isinstance(animal, Cat):
        return animal.speak()
```

Если все объекты имеют общий интерфейс, проверки типов не нужны:

```python
def make_sound(animal):
    return animal.speak()
```

---

### Assuming Inheritance Is Required

Полиморфизм не означает обязательное наличие общего базового класса.

Независимые классы также могут использоваться полиморфно, если предоставляют совместимый интерфейс.

---

### Ignoring Interface Compatibility

Наличие метода с одинаковым названием не гарантирует, что объекты совместимы.

Необходимо учитывать параметры метода, возвращаемые значения и ожидаемое поведение.

---

### Catching All Exceptions

Не следует использовать слишком широкий `except Exception` только для того, чтобы поддержать duck typing.

```python
try:
    obj.process()
except Exception:
    return None
```

Такой код может скрыть настоящую ошибку внутри `process()`.

---

### Confusing Polymorphism with Overriding

Переопределение методов является одним из механизмов реализации полиморфизма, но полиморфизм значительно шире.

Он также может реализовываться через duck typing, встроенные протоколы Python и структурную типизацию.

---

### Designing an Unclear Interface

Если общий интерфейс не имеет четко определенного поведения, разные реализации могут стать несовместимыми на логическом уровне.

Интерфейс должен описывать понятный набор операций и ожидаемый результат их выполнения.

---

## Related Concepts

* Classes
* Objects
* Inheritance
* Method Overriding
* Encapsulation
* Abstraction
* Duck Typing
* Abstract Base Classes
* `abc`
* `typing.Protocol`
* `isinstance()`
* `issubclass()`
* Special Methods
* Operator Overloading
* Protocols
* Structural Typing

---

## Key Takeaways

* Полиморфизм позволяет использовать разные объекты через общий интерфейс.
* В Python одним из основных механизмов полиморфизма является duck typing.
* Для полиморфизма не обязательно использовать наследование.
* Переопределение методов позволяет подклассам предоставлять собственное поведение.
* Встроенные функции и операторы Python также демонстрируют полиморфное поведение.
* `isinstance()` полезен, когда логика действительно зависит от конкретного типа.
* Избыточные проверки типов могут сделать код менее гибким.
* Абстрактные базовые классы позволяют явно задавать общий интерфейс.
* `typing.Protocol` позволяет описывать структурные интерфейсы.
* Совместимость интерфейса определяется не только именами методов, но и их сигнатурами и ожидаемым поведением.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Data model — Custom classes
* Python Language Reference — Data model — Special method names
* Python 3.14 Tutorial — Classes
* Python 3.14 Tutorial — Inheritance
* Python Standard Library — `abc` — Abstract Base Classes
* Python Standard Library — `typing` — Support for type hints
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html
* Official documentation: https://docs.python.org/3.14/tutorial/classes.html
* Official documentation: https://docs.python.org/3.14/library/abc.html
* Official documentation: https://docs.python.org/3.14/library/typing.html
