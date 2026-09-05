# Inheritance

## Definition

Наследование (`inheritance`) — механизм объектно-ориентированного программирования, который позволяет создавать новый класс на основе существующего.

Новый класс называется **дочерним классом** (`subclass`), а класс, от которого он наследуется, — **базовым классом** (`base class`) или **родительским классом** (`parent class`).

Дочерний класс получает доступ к атрибутам и методам базового класса и может добавлять собственные атрибуты и методы или переопределять существующее поведение.

---

## Purpose

Наследование используется для повторного использования кода и создания иерархий связанных классов.

Оно позволяет:

* переиспользовать существующую реализацию;
* добавлять новое поведение к существующему классу;
* переопределять методы базового класса;
* создавать специализированные версии объектов;
* моделировать отношения между сущностями;
* использовать полиморфизм;
* уменьшать дублирование кода.

Например, можно создать общий класс `Animal`, а затем определить `Dog` и `Cat` как его дочерние классы.

---

## Core Concepts

Основные понятия, которые необходимо знать для понимания наследования.

### Base Class

Базовый класс содержит общие атрибуты и методы, которые могут использоваться дочерними классами.

```python
class Animal:
    def eat(self):
        print("Eating")
```

`Animal` является базовым классом.

---

### Subclass

Дочерний класс создаётся с указанием базового класса в круглых скобках:

```python
class Dog(Animal):
    pass
```

Теперь `Dog` наследует поведение `Animal`.

```python
dog = Dog()

dog.eat()
# Eating
```

Метод `eat()` определён в `Animal`, но доступен экземпляру `Dog`.

---

### Inherited Methods

Дочерний класс автоматически получает доступ к методам базового класса, если они доступны через обычный механизм поиска атрибутов.

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


dog = Dog()

dog.eat()
```

Нет необходимости повторно определять `eat()` в `Dog`.

---

### Inherited Attributes

Наследоваться могут не только методы, но и атрибуты класса.

```python
class Animal:
    species = "animal"


class Dog(Animal):
    pass


print(Dog.species)
# animal
```

Экземпляр дочернего класса также может получить доступ к этому атрибуту:

```python
dog = Dog()

print(dog.species)
# animal
```

---

### Extending a Class

Дочерний класс может добавлять собственные атрибуты и методы:

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Woof")
```

Теперь объект `Dog` имеет оба метода:

```python
dog = Dog()

dog.eat()
dog.bark()
```

Таким образом, дочерний класс расширяет функциональность базового класса.

---

### Method Overriding

Дочерний класс может определить метод с тем же именем, что и в базовом классе.

В этом случае дочерняя реализация переопределяет поведение базового класса:

```python
class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof")
```

Теперь:

```python
dog = Dog()

dog.speak()
# Woof
```

Python использует метод `Dog.speak()` вместо `Animal.speak()`.

---

### Calling the Parent Implementation

Для обращения к реализации базового класса часто используется `super()`:

```python
class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")
```

Результат:

```text
Some sound
Woof
```

`super()` позволяет обращаться к следующему классу в порядке разрешения методов (`MRO`), а не просто означает «родительский класс».

---

### `super()` in `__init__()`

`super()` часто используется для вызова `__init__()` базового класса:

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

Теперь:

```python
dog = Dog("Rex", "Labrador")

print(dog.name)
# Rex

print(dog.breed)
# Labrador
```

Дочерний класс использует инициализацию базового класса и добавляет собственную.

---

### `isinstance()`

`isinstance()` позволяет проверить, является ли объект экземпляром указанного класса или его подкласса:

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

Объект `dog` является экземпляром `Dog`, а также экземпляром `Animal` с точки зрения отношения наследования.

---

### `issubclass()`

`issubclass()` проверяет, является ли один класс подклассом другого:

```python
class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
# True

print(issubclass(Animal, Dog))
# False
```

Функция принимает классы, а не экземпляры.

---

### Multiple Inheritance

Python поддерживает множественное наследование.

Дочерний класс может наследоваться сразу от нескольких базовых классов:

```python
class Flyer:
    def fly(self):
        print("Flying")


class Swimmer:
    def swim(self):
        print("Swimming")


class Duck(Flyer, Swimmer):
    pass
```

Теперь `Duck` получает методы обоих классов:

```python
duck = Duck()

duck.fly()
duck.swim()
```

---

### Method Resolution Order

При множественном наследовании Python должен определить, в каком порядке искать методы и атрибуты.

Этот порядок называется **Method Resolution Order (MRO)**.

Получить MRO можно через `__mro__`:

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.__mro__)
```

Также можно использовать:

```python
print(C.mro())
```

MRO определяет порядок поиска методов при обращении к атрибутам объекта.

---

### Diamond Inheritance

Проблема ромба возникает, когда два класса наследуются от одного базового класса, а другой класс наследуется от обоих:

```text
      A
     / \
    B   C
     \ /
      D
```

Python решает такую ситуацию с помощью MRO.

Пример:

```python
class A:
    def hello(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
```

MRO определяет порядок поиска `hello()` для объекта `D`.

---

### Abstract Base Classes

Для определения общего интерфейса можно использовать абстрактные базовые классы из модуля `abc`.

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```

Класс с абстрактным методом нельзя использовать для создания экземпляра до тех пор, пока все абстрактные методы не будут реализованы в дочернем классе.

```python
class Dog(Animal):
    def speak(self):
        print("Woof")
```

Теперь можно создать:

```python
dog = Dog()
```

Абстрактные классы особенно полезны для определения общего интерфейса группы классов.

---

### Inheritance and Polymorphism

Наследование часто используется вместе с полиморфизмом.

Несколько классов могут реализовывать один и тот же метод по-разному:

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

Теперь можно работать с объектами через общий интерфейс:

```python
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

Каждый объект использует собственную реализацию `speak()`.

---

### Inheritance and Attributes

Если дочерний класс определяет атрибут с таким же именем, он может скрыть соответствующий атрибут базового класса при обычном обращении:

```python
class Animal:
    species = "animal"


class Dog(Animal):
    species = "dog"


print(Dog.species)
# dog
```

При необходимости можно обратиться к базовой реализации через имя базового класса:

```python
print(Animal.species)
# animal
```

---

### Private Attributes and Inheritance

Атрибуты с двумя ведущими подчёркиваниями подвергаются name mangling.

```python
class Parent:
    def __init__(self):
        self.__value = 10
```

Имя такого атрибута изменяется с учётом имени класса.

Это позволяет избежать случайного конфликта с одноимённым атрибутом в дочернем классе.

```python
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = 20
```

В данном случае `Parent.__value` и `Child.__value` будут разными атрибутами после name mangling.

---

### Object Class

Если класс не указывает другой базовый класс, он неявно наследуется от `object`:

```python
class Person:
    pass
```

Это эквивалентно наследованию от `object` в смысле базовой иерархии Python:

```python
class Person(object):
    pass
```

`object` является базовым классом для классов Python.

---

### `super()` and MRO

`super()` не означает буквально «вызвать метод родителя».

Он возвращает объект-посредник для доступа к атрибутам и методам в соответствии с MRO.

Это особенно важно при множественном наследовании:

```python
class A:
    def hello(self):
        print("A")


class B(A):
    def hello(self):
        print("B")
        super().hello()


class C(A):
    def hello(self):
        print("C")
        super().hello()


class D(B, C):
    def hello(self):
        print("D")
        super().hello()
```

Порядок вызовов определяется MRO класса `D`.

---

## Syntax

Основной синтаксис Python.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")


class Dog(Animal):
    def bark(self):
        print("Woof")


dog = Dog("Rex")

dog.speak()
dog.bark()
```

Переопределение метода:

```python
class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof")
```

Использование `super()`:

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

Множественное наследование:

```python
class Flyer:
    def fly(self):
        print("Flying")


class Swimmer:
    def swim(self):
        print("Swimming")


class Duck(Flyer, Swimmer):
    pass
```

Проверка наследования:

```python
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
```

Получение MRO:

```python
print(Dog.__mro__)
print(Dog.mro())
```

---

## Rules

1. Наследование позволяет создавать новый класс на основе существующего.
2. Базовый класс предоставляет атрибуты и методы, доступные дочернему классу.
3. Дочерний класс может добавлять собственные атрибуты и методы.
4. Дочерний класс может переопределять методы базового класса.
5. `super()` используется для обращения к следующему классу в MRO.
6. `super().__init__()` часто используется для вызова инициализации базового класса.
7. Python поддерживает множественное наследование.
8. MRO определяет порядок поиска методов и атрибутов.
9. `isinstance()` проверяет объект с учётом иерархии наследования.
10. `issubclass()` проверяет отношение между классами.
11. Класс без явно указанного базового класса наследуется от `object`.
12. Атрибут дочернего класса может перекрывать атрибут с таким же именем базового класса.
13. Методы с двумя ведущими подчёркиваниями подвергаются name mangling.
14. Name mangling учитывает имя класса и помогает предотвращать случайные конфликты имён.
15. Абстрактные базовые классы могут использоваться для определения общего интерфейса.
16. Абстрактные методы требуют реализации в конкретном дочернем классе.
17. Наследование часто используется вместе с полиморфизмом.
18. Множественное наследование требует понимания MRO.
19. `super()` не следует воспринимать исключительно как механизм вызова непосредственного родительского класса.
20. Наследование следует использовать для выражения логической связи между классами и повторного использования общего поведения.

---

## Examples

### Example 1 — Basic Inheritance

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


dog = Dog()

dog.eat()
# Eating
```

Explanation:

`Dog` наследуется от `Animal`, поэтому экземпляр `Dog` получает метод `eat()`.

---

### Example 2 — Extending a Base Class

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Woof")


dog = Dog()

dog.eat()
dog.bark()
```

Explanation:

Дочерний класс сохраняет унаследованное поведение и добавляет собственный метод `bark()`.

---

### Example 3 — Method Overriding

```python
class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof")


animal = Animal()
dog = Dog()

animal.speak()
# Some sound

dog.speak()
# Woof
```

Explanation:

`Dog` переопределяет метод `speak()` и предоставляет собственную реализацию.

---

### Example 4 — Using `super()`

```python
class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")


dog = Dog()

dog.speak()
```

Explanation:

`super().speak()` вызывает реализацию метода, найденную следующим по MRO классом.

---

### Example 5 — Extending `__init__()`

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Rex", "Labrador")

print(dog.name)
# Rex

print(dog.breed)
# Labrador
```

Explanation:

`Dog` использует инициализацию `Animal` для `name` и добавляет собственный атрибут `breed`.

---

### Example 6 — Multiple Inheritance

```python
class Flyer:
    def fly(self):
        print("Flying")


class Swimmer:
    def swim(self):
        print("Swimming")


class Duck(Flyer, Swimmer):
    pass


duck = Duck()

duck.fly()
duck.swim()
```

Explanation:

`Duck` наследуется одновременно от `Flyer` и `Swimmer` и получает методы обоих классов.

---

### Example 7 — Checking Inheritance

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

print(issubclass(Dog, Animal))
# True
```

Explanation:

`isinstance()` работает с объектами, а `issubclass()` — с классами.

---

### Example 8 — Polymorphism Through Inheritance

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


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

Explanation:

Оба класса имеют общий интерфейс `speak()`, но реализуют его по-разному.

---

### Example 9 — Method Resolution Order

```python
class A:
    def hello(self):
        print("A")


class B(A):
    pass


class C(B):
    pass


print(C.mro())
```

Explanation:

`mro()` показывает порядок, в котором Python ищет методы и атрибуты для объектов класса `C`.

---

### Example 10 — Diamond Inheritance

```python
class A:
    def hello(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())

d = D()
d.hello()
# A
```

Explanation:

Python использует MRO для разрешения неоднозначности в иерархии наследования.

---

## Edge Cases

### Base Class Initialization

Если дочерний класс определяет собственный `__init__()`, `__init__()` базового класса автоматически не вызывается как часть переопределённого метода.

```python
class Parent:
    def __init__(self):
        self.value = 10


class Child(Parent):
    def __init__(self):
        self.other = 20
```

В этом случае:

```python
child = Child()

print(child.value)
# AttributeError
```

Если необходима инициализация базового класса, её обычно вызывают явно:

```python
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.other = 20
```

---

### Overridden Attribute

Дочерний класс может определить атрибут с тем же именем:

```python
class Animal:
    species = "animal"


class Dog(Animal):
    species = "dog"


print(Dog.species)
# dog
```

Реализация дочернего класса имеет приоритет при обычном обращении.

---

### `super()` Is Not Always the Parent

При множественном наследовании `super()` обращается к следующему классу согласно MRO:

```python
class A:
    def hello(self):
        print("A")


class B(A):
    def hello(self):
        print("B")
        super().hello()


class C(A):
    def hello(self):
        print("C")
        super().hello()


class D(B, C):
    def hello(self):
        print("D")
        super().hello()
```

Для `D` цепочка вызовов зависит от MRO, а не просто от непосредственного родителя.

---

### Inheritance Cycle

Нельзя создать циклическую иерархию наследования:

```python
class A(B):
    pass


class B(A):
    pass
```

Такая структура невозможна и приведёт к ошибке при определении классов.

---

### Incompatible Method Signatures

При переопределении метода дочерний класс может изменить сигнатуру, но это может нарушить ожидаемый интерфейс:

```python
class Animal:
    def feed(self, food):
        pass


class Dog(Animal):
    def feed(self):
        pass
```

Код, ожидающий интерфейс `Animal`, может передать аргумент и получить `TypeError`.

Поэтому при переопределении методов важно сохранять совместимый интерфейс.

---

### Multiple Inheritance Conflicts

Если несколько базовых классов определяют одинаковый метод, результат зависит от MRO:

```python
class A:
    def hello(self):
        print("A")


class B:
    def hello(self):
        print("B")


class C(A, B):
    pass


C().hello()
# A
```

Python ищет метод в соответствии с MRO.

---

## Common Mistakes

### Mistake 1 — Forgetting `super().__init__()`

Если дочерний класс переопределяет `__init__()`, инициализация базового класса не выполняется автоматически через этот переопределённый метод.

```python
class Parent:
    def __init__(self):
        self.value = 10


class Child(Parent):
    def __init__(self):
        self.other = 20
```

Если требуется состояние `Parent`, следует вызвать:

```python
super().__init__()
```

---

### Mistake 2 — Calling the Parent Class Directly

Иногда пишут:

```python
Parent.__init__(self)
```

В простых случаях это может работать, но при множественном наследовании такой подход может нарушить цепочку MRO.

Предпочтительный вариант:

```python
super().__init__()
```

---

### Mistake 3 — Assuming `super()` Means Immediate Parent

`super()` работает согласно MRO.

Особенно важно понимать это при множественном наследовании.

```python
class C(B, A):
    ...
```

Следующий класс определяется не простым правилом «родитель справа или слева», а полным порядком MRO.

---

### Mistake 4 — Excessive Inheritance

Не каждый случай повторного использования кода требует наследования.

Если классы не имеют логического отношения «является разновидностью» (`is-a`), часто лучше использовать композицию — один объект содержит другой.

---

### Mistake 5 — Ignoring MRO

При множественном наследовании недостаточно знать только список базовых классов:

```python
class D(B, C):
    pass
```

Следует понимать порядок разрешения методов:

```python
print(D.mro())
```

---

### Mistake 6 — Breaking the Parent Interface

Переопределение метода с несовместимой сигнатурой может привести к ошибкам:

```python
class Parent:
    def process(self, value):
        pass


class Child(Parent):
    def process(self):
        pass
```

Дочерний класс должен по возможности сохранять ожидаемый интерфейс базового класса.

---

## Related Concepts

* Classes — классы Python.
* Objects — экземпляры классов.
* Encapsulation — инкапсуляция.
* Polymorphism — полиморфизм.
* Abstraction — абстракция.
* `super()` — механизм доступа к следующему классу в MRO.
* MRO — порядок разрешения методов.
* `isinstance()` — проверка экземпляра.
* `issubclass()` — проверка наследования между классами.
* `object` — базовый класс объектной модели Python.
* Abstract Base Classes — абстрактные базовые классы.
* Composition — альтернативный подход к повторному использованию и организации объектов.
* Method Overriding — переопределение методов.
* Multiple Inheritance — множественное наследование.

---

## Key Takeaways

* Наследование позволяет создавать новый класс на основе существующего.
* Базовый класс содержит общее поведение и состояние.
* Дочерний класс может расширять или переопределять поведение базового класса.
* Метод дочернего класса с таким же именем переопределяет метод базового класса.
* `super()` позволяет использовать реализацию следующего класса в MRO.
* Если дочерний класс определяет собственный `__init__()`, при необходимости он должен явно вызвать `super().__init__()`.
* Python поддерживает множественное наследование.
* MRO определяет порядок поиска методов и атрибутов.
* `isinstance()` проверяет объект с учётом наследования.
* `issubclass()` проверяет отношение между классами.
* Наследование часто используется для реализации полиморфизма.
* Name mangling помогает избегать конфликтов имён в иерархии классов.
* Наследование следует использовать для логически связанных классов, а не только ради повторного использования небольшого фрагмента кода.
* Композиция является важной альтернативой наследованию.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Inheritance
* Python Language Reference — The standard type hierarchy
* Python Language Reference — Custom classes
* Python Language Reference — `super()`
* Python 3.14 Tutorial — Inheritance
* Python 3.14 Tutorial — Classes
* Python 3.14 Tutorial — Multiple Inheritance
* Python Standard Library — `abc` — Abstract Base Classes
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html#custom-classes
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html#inheritance
* Official documentation: https://docs.python.org/3.14/library/functions.html#super
* Official documentation: https://docs.python.org/3.14/library/functions.html#isinstance
* Official documentation: https://docs.python.org/3.14/library/functions.html#issubclass
* Official documentation: https://docs.python.org/3.14/library/abc.html
* Official documentation: https://docs.python.org/3.14/tutorial/classes.html#inheritance
