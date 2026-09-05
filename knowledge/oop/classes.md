# Classes

## Definition

Класс (`class`) — это шаблон, который определяет структуру и поведение объектов в Python.

Класс может содержать:

* атрибуты, хранящие данные;
* методы, определяющие поведение;
* конструктор `__init__()`, выполняющий начальную настройку объекта;
* другие специальные методы;
* свойства и другие элементы, связанные с объектом.

Объект — это конкретный экземпляр класса.

Например, класс `Person` может описывать общие характеристики человека, а объекты `person1` и `person2` будут конкретными экземплярами этого класса.

---

## Purpose

Классы используются для объединения данных и функций, работающих с этими данными, в единую структуру.

Они позволяют:

* моделировать сущности предметной области;
* создавать несколько объектов с одинаковой структурой;
* объединять состояние и поведение объекта;
* переиспользовать код;
* скрывать детали реализации;
* создавать основу для наследования и полиморфизма.

Классы особенно полезны в больших программах, где необходимо описывать сложные сущности и их взаимодействие.

---

## Core Concepts

Основные понятия, которые необходимо знать для понимания классов.

### Class Definition

Класс объявляется с помощью ключевого слова `class`:

```python
class Person:
    pass
```

После `class` указывается имя класса.

По соглашению имена классов записываются в стиле `PascalCase`:

```python
class UserAccount:
    pass

class BankAccount:
    pass
```

---

### Object

Объект — это экземпляр определённого класса.

```python
class Person:
    pass


person = Person()
```

Здесь `Person` — класс, а `person` — объект этого класса.

Можно создавать несколько независимых объектов одного класса:

```python
person1 = Person()
person2 = Person()
```

Оба объекта имеют один и тот же класс, но являются разными объектами.

---

### Instance

Экземпляр (`instance`) — конкретный объект, созданный на основе класса.

Проверить принадлежность объекта классу можно с помощью `isinstance()`:

```python
class Person:
    pass


person = Person()

print(isinstance(person, Person))
# True
```

Один объект может быть экземпляром класса и его базовых классов.

---

### Attributes

Атрибуты хранят данные, связанные с объектом или классом.

Атрибут экземпляра обычно создаётся через `self`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

После создания объекта:

```python
person = Person("Roman", 27)

print(person.name)
# Roman

print(person.age)
# 27
```

`name` и `age` являются атрибутами экземпляра.

---

### self

`self` — это ссылка на текущий экземпляр объекта.

Он используется внутри методов для доступа к атрибутам и другим методам этого объекта:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")
```

При вызове:

```python
person = Person("Roman")
person.introduce()
```

Python автоматически передаёт объект в метод как первый аргумент.

Имя `self` является общепринятым соглашением Python. Технически можно использовать другое имя, но делать это не рекомендуется.

---

### Methods

Метод — это функция, определённая внутри класса.

```python
class Person:
    def say_hello(self):
        print("Hello")
```

Метод вызывается через объект:

```python
person = Person()
person.say_hello()
```

Методы обычно работают с состоянием объекта через `self`.

---

### **init**()

`__init__()` — специальный метод, который вызывается после создания экземпляра класса.

Обычно он используется для начальной настройки объекта:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Теперь при создании объекта необходимо передать необходимые значения:

```python
person = Person("Roman", 27)
```

После этого объект содержит соответствующие атрибуты.

`__init__()` не создаёт сам объект. Он используется для его инициализации после создания.

---

### Class Attributes

Атрибут можно определить непосредственно внутри класса.

Такой атрибут является атрибутом класса:

```python
class Person:
    species = "human"
```

Все экземпляры могут обращаться к нему:

```python
person1 = Person()
person2 = Person()

print(person1.species)
# human

print(person2.species)
# human
```

Атрибут класса обычно используется для значения, общего для всех экземпляров.

---

### Instance Attributes

Атрибут экземпляра принадлежит конкретному объекту.

```python
class Person:
    def __init__(self, name):
        self.name = name
```

Теперь:

```python
person1 = Person("Roman")
person2 = Person("Alice")

print(person1.name)
# Roman

print(person2.name)
# Alice
```

Изменение атрибута одного объекта не изменяет атрибут другого объекта.

---

### Attribute Lookup

Когда Python обращается к атрибуту объекта, он выполняет поиск в соответствии с правилами модели объектов Python.

Например:

```python
class Person:
    species = "human"

    def __init__(self, name):
        self.name = name
```

Для:

```python
person = Person("Roman")
```

`person.name` находится среди атрибутов экземпляра, а `person.species` может быть найден среди атрибутов класса.

---

### Changing Attributes

Атрибут экземпляра можно изменить после создания объекта:

```python
class Person:
    def __init__(self, name):
        self.name = name


person = Person("Roman")

person.name = "Alex"

print(person.name)
# Alex
```

Также можно добавлять новые атрибуты экземпляру, если класс не ограничивает это поведение:

```python
person.age = 27
```

Теперь у объекта появился атрибут `age`.

---

### Deleting Attributes

Атрибут объекта можно удалить с помощью `del`:

```python
class Person:
    def __init__(self, name):
        self.name = name


person = Person("Roman")

del person.name
```

После удаления обращение к атрибуту вызовет `AttributeError`, если атрибут не будет найден другим способом.

---

### Methods and State

Методы могут изменять состояние объекта:

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
```

Использование:

```python
counter = Counter()

counter.increment()
counter.increment()

print(counter.value)
# 2
```

Метод `increment()` изменяет атрибут `value` конкретного объекта.

---

### Instance Methods

Обычный метод экземпляра принимает `self` первым параметром:

```python
class Person:
    def greet(self, message):
        print(message)
```

Вызов:

```python
person = Person()
person.greet("Hello")
```

Python автоматически передаёт `person` в `self`.

---

### Class Methods

Метод класса создаётся с помощью декоратора `@classmethod`.

Первым параметром он получает класс, обычно обозначаемый как `cls`:

```python
class Person:
    species = "human"

    @classmethod
    def get_species(cls):
        return cls.species
```

Вызов:

```python
print(Person.get_species())
# human
```

`classmethod` используется, когда логика метода относится к классу, а не к конкретному экземпляру.

---

### Static Methods

Статический метод создаётся с помощью `@staticmethod`.

Он не получает автоматически ни экземпляр (`self`), ни класс (`cls`):

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```

Вызов:

```python
print(MathUtils.add(2, 3))
# 5
```

Статический метод используется для логики, которая логически относится к классу, но не требует доступа к его экземпляру или классу.

---

### Class Namespace

Класс создаёт собственное пространство имён, в котором хранятся его атрибуты.

Получить атрибуты класса можно, например, через `__dict__`:

```python
class Person:
    species = "human"

print(Person.__dict__)
```

`__dict__` содержит внутреннее представление пространства имён класса.

---

### Instance Namespace

У обычного объекта также может быть собственное пространство имён:

```python
class Person:
    def __init__(self, name):
        self.name = name


person = Person("Roman")

print(person.__dict__)
# {'name': 'Roman'}
```

Атрибуты экземпляра хранятся отдельно от атрибутов класса.

---

### Encapsulation Through Naming Conventions

Python не использует строгую систему `private`-полей как некоторые другие языки.

Для обозначения внутреннего атрибута часто используется одно подчёркивание:

```python
class Account:
    def __init__(self):
        self._balance = 0
```

Это соглашение означает, что атрибут предназначен для внутреннего использования.

Два подчёркивания в начале имени запускают механизм name mangling:

```python
class Account:
    def __init__(self):
        self.__balance = 0
```

Это изменяет имя атрибута внутри класса, но не делает его абсолютно недоступным.

---

### Properties

Свойства позволяют управлять доступом к атрибуту через синтаксис обычного атрибута.

Для этого используется `@property`:

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

Теперь:

```python
person = Person(27)

print(person.age)
# 27
```

`property` часто используется для контроля чтения и изменения состояния объекта.

---

### `type()`

Функция `type()` позволяет узнать класс объекта:

```python
class Person:
    pass


person = Person()

print(type(person))
# <class '__main__.Person'>
```

Также `type()` может использоваться для динамического создания классов, хотя такой способ обычно не нужен в обычном коде.

---

### `isinstance()`

`isinstance()` проверяет, является ли объект экземпляром указанного класса или его подкласса:

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
# True

print(isinstance(dog, Animal))
# True
```

Для проверки типа объекта в большинстве практических случаев предпочтительнее использовать `isinstance()`, а не сравнение результата `type()`.

---

## Syntax

Основной синтаксис Python.

```python
class Person:
    species = "human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}"


person = Person("Roman", 27)

print(person.name)
print(person.age)
print(person.introduce())
```

Класс с методом класса:

```python
class Person:
    species = "human"

    @classmethod
    def get_species(cls):
        return cls.species
```

Класс со статическим методом:

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```

Класс со свойством:

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

---

## Rules

1. Класс объявляется с помощью ключевого слова `class`.
2. Объект является экземпляром класса.
3. Один класс может иметь множество экземпляров.
4. Атрибуты экземпляра обычно создаются через `self`.
5. `self` обозначает текущий экземпляр объекта.
6. `__init__()` используется для инициализации экземпляра.
7. `__init__()` не создаёт сам объект.
8. Атрибут класса является общим атрибутом класса и может быть доступен его экземплярам.
9. Атрибуты экземпляра принадлежат конкретному объекту.
10. Методы экземпляра обычно получают `self` первым параметром.
11. `@classmethod` создаёт метод, который получает `cls`.
12. `@staticmethod` не получает автоматически `self` или `cls`.
13. Атрибуты экземпляра можно изменять после создания объекта, если класс не ограничивает такое изменение.
14. `del` может использоваться для удаления атрибутов.
15. `isinstance()` проверяет принадлежность объекта классу или его подклассу.
16. `type()` возвращает фактический тип объекта.
17. Одно подчёркивание в начале имени обычно обозначает внутренний атрибут по соглашению.
18. Двойное подчёркивание в начале имени запускает name mangling.
19. `@property` позволяет предоставить доступ к методу через синтаксис атрибута.
20. Класс может содержать данные, методы и специальные методы.
21. Наследование позволяет создавать новые классы на основе существующих.
22. Полиморфизм позволяет использовать объекты разных классов через общий интерфейс.
23. Специальные методы имеют имена вида `__name__` и позволяют объектам взаимодействовать со встроенными операциями Python.

---

## Examples

### Example 1 — Basic Class

```python
class Person:
    pass


person = Person()

print(type(person))
# <class '__main__.Person'>
```

Explanation:

Создан класс `Person` и его экземпляр `person`.

---

### Example 2 — Constructor and Attributes

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Roman", 27)

print(person.name)
# Roman

print(person.age)
# 27
```

Explanation:

`__init__()` получает значения при создании объекта и сохраняет их в атрибутах экземпляра.

---

### Example 3 — Instance Method

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"


person = Person("Roman")

print(person.greet())
# Hello, my name is Roman
```

Explanation:

Метод `greet()` использует состояние конкретного объекта через `self`.

---

### Example 4 — Multiple Instances

```python
class Person:
    def __init__(self, name):
        self.name = name


person1 = Person("Roman")
person2 = Person("Alice")

print(person1.name)
# Roman

print(person2.name)
# Alice
```

Explanation:

Один класс может использоваться для создания множества независимых объектов.

---

### Example 5 — Class Attribute

```python
class Person:
    species = "human"

    def __init__(self, name):
        self.name = name


person1 = Person("Roman")
person2 = Person("Alice")

print(person1.species)
# human

print(person2.species)
# human
```

Explanation:

`species` является атрибутом класса и доступен обоим экземплярам.

---

### Example 6 — Changing Instance State

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


counter = Counter()

counter.increment()
counter.increment()
counter.increment()

print(counter.value)
# 3
```

Explanation:

Каждый вызов `increment()` изменяет состояние конкретного экземпляра.

---

### Example 7 — Class Method

```python
class Person:
    species = "human"

    @classmethod
    def get_species(cls):
        return cls.species


print(Person.get_species())
# human
```

Explanation:

Метод работает с самим классом через параметр `cls`.

---

### Example 8 — Static Method

```python
class MathUtils:
    @staticmethod
    def multiply(a, b):
        return a * b


print(MathUtils.multiply(4, 5))
# 20
```

Explanation:

Методу не нужен ни объект, ни класс. Он просто содержит функцию, логически связанную с классом.

---

### Example 9 — Property

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age


person = Person(27)

print(person.age)
# 27
```

Explanation:

Метод `age()` оформлен как свойство, поэтому к нему можно обращаться как к обычному атрибуту.

---

### Example 10 — Checking an Instance

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
# True

print(isinstance(dog, Animal))
# True
```

Explanation:

`isinstance()` учитывает не только непосредственный класс объекта, но и его базовые классы.

---

## Edge Cases

### Empty Class

Класс может не содержать никаких собственных атрибутов и методов:

```python
class Empty:
    pass
```

`pass` используется как пустая инструкция, позволяющая создать синтаксически корректный блок.

---

### Class Attribute Shadowing

Атрибут экземпляра может перекрыть атрибут класса с таким же именем:

```python
class Person:
    species = "human"


person = Person()

person.species = "unknown"

print(person.species)
# unknown

print(Person.species)
# human
```

Изменённый атрибут относится к экземпляру и не изменяет атрибут класса.

---

### Mutable Class Attributes

Особенно важно соблюдать осторожность с изменяемыми атрибутами класса:

```python
class User:
    roles = []


user1 = User()
user2 = User()

user1.roles.append("admin")

print(user2.roles)
# ['admin']
```

Список `roles` является общим для экземпляров.

Если каждому объекту нужен собственный список, его следует создавать в `__init__()`:

```python
class User:
    def __init__(self):
        self.roles = []
```

---

### Missing Attribute

Если атрибут отсутствует у объекта и не найден через механизм поиска атрибутов, возникает `AttributeError`:

```python
class Person:
    pass


person = Person()

print(person.name)
# AttributeError
```

---

### Constructor Arguments

Если `__init__()` требует аргументы, их необходимо передать при создании объекта:

```python
class Person:
    def __init__(self, name):
        self.name = name


person = Person()
# TypeError
```

Правильно:

```python
person = Person("Roman")
```

---

### `__init__()` Return Value

`__init__()` должен возвращать `None`.

Нельзя использовать его как обычную функцию, возвращающую произвольный объект:

```python
class Person:
    def __init__(self):
        return 123
        # TypeError
```

---

### Dynamic Attributes

В обычном классе атрибуты могут добавляться объекту после его создания:

```python
class Person:
    pass


person = Person()

person.name = "Roman"
person.age = 27

print(person.name)
# Roman
```

Однако конкретный класс может ограничивать возможность динамического добавления атрибутов, например с помощью `__slots__`.

---

### `isinstance()` and Inheritance

`isinstance()` возвращает `True` также для базового класса:

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Animal))
# True
```

Это важно учитывать при проверке типов в иерархиях классов.

---

## Common Mistakes

### Mistake 1 — Forgetting `self`

Неправильно:

```python
class Person:
    def __init__(name):
        name = name
```

Правильно:

```python
class Person:
    def __init__(self, name):
        self.name = name
```

`self` необходим для доступа к конкретному экземпляру.

---

### Mistake 2 — Confusing Class and Instance Attributes

Неправильно использовать изменяемый объект класса, если каждый экземпляр должен иметь собственное значение:

```python
class User:
    items = []
```

Правильно:

```python
class User:
    def __init__(self):
        self.items = []
```

---

### Mistake 3 — Expecting `__init__()` to Create the Object

`__init__()` отвечает за инициализацию уже созданного экземпляра.

```python
class Person:
    def __init__(self, name):
        self.name = name
```

Не следует воспринимать `__init__()` как обычный конструктор, который непосредственно создаёт объект. Создание и инициализация объекта — разные этапы модели объектов Python.

---

### Mistake 4 — Modifying a Class Attribute Accidentally

```python
class Counter:
    values = []


counter1 = Counter()
counter2 = Counter()

counter1.values.append(10)

print(counter2.values)
# [10]
```

Оба объекта используют один и тот же список класса.

---

### Mistake 5 — Comparing Types Incorrectly

Вместо чрезмерно жёсткой проверки:

```python
if type(value) == Animal:
    ...
```

часто лучше использовать:

```python
if isinstance(value, Animal):
    ...
```

`isinstance()` учитывает наследование.

---

### Mistake 6 — Using Class Methods When Instance State Is Required

Если метод должен работать с данными конкретного объекта, ему обычно нужен `self`:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return self.name
```

`@classmethod` следует использовать для операций, относящихся к классу.

---

## Related Concepts

* Object — конкретный экземпляр класса.
* Instance — экземпляр класса.
* `self` — ссылка на текущий экземпляр.
* `__init__()` — инициализация экземпляра.
* `@classmethod` — метод класса.
* `@staticmethod` — статический метод.
* `@property` — управление доступом к атрибутам через свойства.
* Inheritance — наследование классов.
* Polymorphism — полиморфизм.
* Encapsulation — организация и ограничение доступа к внутреннему состоянию.
* Magic Methods — специальные методы Python.
* `isinstance()` — проверка принадлежности объекта классу.
* `type()` — получение типа объекта.
* `__dict__` — пространство имён объекта или класса.
* `__slots__` — механизм ограничения набора атрибутов экземпляра.

---

## Key Takeaways

* `class` используется для создания классов.
* Объект является экземпляром класса.
* Один класс может иметь множество независимых экземпляров.
* `self` используется для доступа к состоянию конкретного экземпляра.
* `__init__()` используется для инициализации объекта.
* Атрибуты экземпляра принадлежат конкретному объекту.
* Атрибуты класса могут быть общими для всех экземпляров.
* Методы определяют поведение объектов.
* `@classmethod` работает с классом через `cls`.
* `@staticmethod` не получает автоматически ни объект, ни класс.
* `@property` позволяет контролировать доступ к данным через интерфейс атрибута.
* Изменяемые атрибуты класса могут случайно стать общими для всех экземпляров.
* `isinstance()` учитывает наследование при проверке типа.
* Классы являются фундаментальной основой объектно-ориентированного программирования в Python.
* Наследование, полиморфизм, инкапсуляция и специальные методы строятся на базовой модели классов.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Classes
* Python Language Reference — Data model — Classes
* Python Language Reference — Data model — Objects, values and types
* Python 3.14 Tutorial — Classes
* Python 3.14 Tutorial — An Informal Introduction to Python
* Official documentation: https://docs.python.org/3.14/reference/compound_stmts.html#class-definitions
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html#classes
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html#objects-values-and-types
* Official documentation: https://docs.python.org/3.14/tutorial/classes.html
