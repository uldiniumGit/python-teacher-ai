# Encapsulation

## Definition

Инкапсуляция (`encapsulation`) — принцип объектно-ориентированного программирования, при котором данные и методы, работающие с этими данными, объединяются внутри объекта, а внутреннее состояние объекта отделяется от внешнего интерфейса.

В Python инкапсуляция реализуется в основном с помощью соглашений об именовании, name mangling, свойств (`property`) и методов.

В отличие от некоторых языков программирования, Python не предоставляет строгих модификаторов доступа `private` и `protected`. Вместо этого язык предоставляет механизмы и соглашения, которые позволяют обозначать внутренние детали реализации.

---

## Purpose

Инкапсуляция используется для управления доступом к внутреннему состоянию объектов и отделения внутренней реализации от публичного интерфейса.

Она позволяет:

* скрывать детали реализации;
* контролировать изменение внутреннего состояния;
* предотвращать случайное изменение важных данных;
* предоставлять объекту понятный публичный интерфейс;
* изменять внутреннюю реализацию без изменения внешнего кода;
* создавать более предсказуемые и поддерживаемые классы.

Например, банковский счёт может хранить баланс внутри объекта и предоставлять методы `deposit()` и `withdraw()` вместо прямого изменения баланса.

---

## Core Concepts

Основные понятия, которые необходимо знать для понимания инкапсуляции.

### Public Attributes

Обычный атрибут без специальных соглашений считается публичным.

```python
class Person:
    def __init__(self, name):
        self.name = name
```

Такой атрибут можно напрямую читать и изменять:

```python
person = Person("Roman")

print(person.name)

person.name = "Alex"
```

Python не запрещает прямой доступ к публичным атрибутам.

---

### Protected Convention

Одно подчёркивание в начале имени используется как соглашение для обозначения внутреннего атрибута:

```python
class Account:
    def __init__(self):
        self._balance = 0
```

`_balance` считается внутренним атрибутом, предназначенным в первую очередь для использования внутри класса и его наследников.

Однако Python технически не запрещает доступ к нему:

```python
account = Account()

print(account._balance)
```

Одно подчёркивание — это соглашение, а не механизм строгой защиты.

---

### Private Convention

Два подчёркивания в начале имени вызывают механизм name mangling:

```python
class Account:
    def __init__(self):
        self.__balance = 0
```

Python изменяет внутреннее имя атрибута примерно на:

```text
_Account__balance
```

Это позволяет избежать случайных конфликтов имён, особенно при наследовании.

Name mangling не является абсолютным запретом доступа к атрибуту.

---

### Name Mangling

Name mangling применяется к идентификаторам, начинающимся как минимум с двух подчёркиваний и не заканчивающимся двумя подчёркиваниями.

Например:

```python
class Person:
    def __init__(self):
        self.__name = "Roman"
```

Внутри объекта имя хранится с учётом имени класса:

```python
person = Person()

print(person.__dict__)
# {'_Person__name': 'Roman'}
```

Обращение через исходное имя:

```python
print(person.__name)
# AttributeError
```

Но технически атрибут можно найти через преобразованное имя:

```python
print(person._Person__name)
# Roman
```

Поэтому name mangling предназначен прежде всего для предотвращения случайных конфликтов имён, а не для обеспечения абсолютной приватности.

---

### Private Methods

Name mangling применяется не только к атрибутам, но и к методам:

```python
class Account:
    def __validate_amount(self, amount):
        return amount > 0

    def deposit(self, amount):
        if self.__validate_amount(amount):
            print("Deposit accepted")
```

Метод `__validate_amount()` становится внутренним методом класса с преобразованным именем.

---

### Public Interface

Публичный интерфейс — это набор атрибутов и методов, которые предназначены для использования внешним кодом.

Например:

```python
class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance
```

Пользователь класса взаимодействует с объектом через `deposit()` и `get_balance()`, а `_balance` рассматривается как внутренняя деталь реализации.

---

### Controlled Access

Инкапсуляция позволяет контролировать изменение состояния объекта.

Например, вместо прямого изменения баланса:

```python
account._balance = -1000
```

можно предоставить метод:

```python
account.deposit(500)
```

Метод может проверять входные данные:

```python
class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount
```

Теперь правила изменения состояния сосредоточены внутри класса.

---

### Properties

`property` позволяет предоставить доступ к внутреннему состоянию через интерфейс атрибута.

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

Использование:

```python
person = Person(27)

print(person.age)
```

Внешний код обращается к `age` как к атрибуту, хотя фактически вызывается метод.

---

### Property Setter

С помощью `@<property>.setter` можно контролировать изменение значения.

```python
class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value
```

Теперь:

```python
person = Person(27)

person.age = 30

print(person.age)
# 30
```

При попытке установить некорректное значение:

```python
person.age = -5
# ValueError
```

Таким образом, setter позволяет централизовать проверку данных.

---

### Read-Only Properties

Если определить только getter и не создавать setter, свойство становится доступным только для чтения через этот интерфейс:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
```

Попытка:

```python
circle = Circle(10)

circle.radius = 20
```

приведёт к ошибке, поскольку setter для `radius` не определён.

---

### Methods for State Modification

Вместо прямого доступа к внутреннему состоянию можно использовать методы.

```python
class Counter:
    def __init__(self):
        self._value = 0

    def increment(self):
        self._value += 1

    def decrement(self):
        self._value -= 1

    def get_value(self):
        return self._value
```

Такой подход позволяет определить допустимые операции над состоянием объекта.

---

### Encapsulation and Invariants

Инкапсуляция помогает поддерживать инварианты объекта — условия, которые должны оставаться истинными во время работы программы.

Например, баланс банковского счёта не должен становиться отрицательным:

```python
class Account:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
```

Все операции изменения состояния проходят через методы, которые проверяют ограничения.

---

### Encapsulation and Abstraction

Инкапсуляция и абстракция связаны, но не являются одним и тем же.

**Инкапсуляция** организует состояние и поведение объекта и определяет, как к внутренним данным можно обращаться.

**Абстракция** позволяет скрыть сложность реализации и предоставить пользователю только важную часть интерфейса.

Например, метод:

```python
account.withdraw(100)
```

предоставляет простой интерфейс, тогда как проверка баланса и изменение внутреннего состояния выполняются внутри класса.

---

### Encapsulation in Python

В Python инкапсуляция основана на принципе доверия и соглашениях.

Язык позволяет разработчику обратиться к большинству атрибутов напрямую:

```python
class User:
    def __init__(self):
        self._name = "Roman"


user = User()

print(user._name)
```

Следовательно, `_name` не является настоящим `private`-полем.

Инкапсуляция в Python означает прежде всего проектирование понятного интерфейса и обозначение деталей, которые не предназначены для внешнего использования.

---

## Syntax

Основной синтаксис Python.

```python
class Account:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    @property
    def balance(self):
        return self._balance
```

Использование:

```python
account = Account(100)

account.deposit(50)

print(account.balance)
# 150
```

Name mangling:

```python
class User:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
```

Свойство с getter и setter:

```python
class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value
```

---

## Rules

1. Python не предоставляет строгие модификаторы доступа `private` и `protected`.
2. Обычные атрибуты считаются публичными.
3. Одно подчёркивание `_name` обозначает внутренний атрибут по соглашению.
4. `_name` технически всё ещё доступен из внешнего кода.
5. Два подчёркивания `__name` запускают механизм name mangling.
6. Name mangling изменяет внутреннее имя атрибута с учётом имени класса.
7. Name mangling не обеспечивает абсолютную приватность.
8. Имена вида `__name__` с двумя подчёркиваниями с обеих сторон относятся к специальным методам и атрибутам Python и не используют обычный name mangling.
9. Инкапсуляция позволяет скрывать детали реализации за публичным интерфейсом.
10. `@property` позволяет предоставить доступ к данным через синтаксис атрибута.
11. Setter свойства позволяет проверять данные перед изменением состояния объекта.
12. Свойство без setter можно использовать как интерфейс только для чтения.
13. Методы могут использоваться для контролируемого изменения состояния объекта.
14. Внутренние атрибуты часто имеют префикс `_`.
15. Инкапсуляция помогает поддерживать инварианты объекта.
16. Сокрытие реализации позволяет изменять внутреннюю реализацию без необходимости менять публичный интерфейс.
17. Инкапсуляция не означает, что внутренние данные должны быть физически недоступны.
18. Хорошая инкапсуляция должна определять понятный и предсказуемый интерфейс взаимодействия с объектом.

---

## Examples

### Example 1 — Protected Convention

```python
class User:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


user = User("Roman")

print(user.get_name())
# Roman
```

Explanation:

`_name` обозначает внутренний атрибут класса. Внешний код технически может обратиться к нему напрямую, но по соглашению этого делать не следует.

---

### Example 2 — Name Mangling

```python
class User:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


user = User("Roman")

print(user.get_name())
# Roman
```

Explanation:

`__name` подвергается name mangling. Внутри класса к нему можно обращаться через исходное имя.

---

### Example 3 — Property Getter

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

Свойство предоставляет внешний интерфейс для чтения внутреннего атрибута `_age`.

---

### Example 4 — Property Setter

```python
class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value


person = Person(27)

person.age = 30

print(person.age)
# 30
```

Explanation:

Setter проверяет значение перед сохранением его во внутренний атрибут.

---

### Example 5 — Read-Only Property

```python
class Product:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


product = Product("Laptop")

print(product.name)
# Laptop
```

Explanation:

Для `name` определён только getter. Внешний код может получить значение через свойство, но setter отсутствует.

---

### Example 6 — Controlled State Changes

```python
class Counter:
    def __init__(self):
        self._value = 0

    def increment(self):
        self._value += 1

    def get_value(self):
        return self._value


counter = Counter()

counter.increment()
counter.increment()

print(counter.get_value())
# 2
```

Explanation:

Состояние счётчика хранится во внутреннем атрибуте `_value`, а изменение происходит через метод `increment()`.

---

### Example 7 — Maintaining an Invariant

```python
class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount

    @property
    def balance(self):
        return self._balance


account = BankAccount(100)

account.withdraw(40)

print(account.balance)
# 60
```

Explanation:

Публичный интерфейс не позволяет обычным операциям нарушить условие, что баланс не должен становиться отрицательным.

---

### Example 8 — Private Method

```python
class Calculator:
    def __validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")

    def square(self, value):
        self.__validate(value)
        return value ** 2


calculator = Calculator()

print(calculator.square(5))
# 25
```

Explanation:

`__validate()` является внутренним методом. Name mangling изменяет его имя и помогает избежать случайного конфликта с одноимёнными методами в подклассах.

---

## Edge Cases

### Direct Access to Protected Attribute

Атрибут с одним подчёркиванием всё ещё доступен:

```python
class User:
    def __init__(self):
        self._name = "Roman"


user = User()

print(user._name)
# Roman
```

Это не является ошибкой Python, поскольку `_name` — соглашение, а не запрет.

---

### Accessing a Name-Mangled Attribute

Name mangling не делает атрибут абсолютно недоступным:

```python
class User:
    def __init__(self):
        self.__name = "Roman"


user = User()

print(user._User__name)
# Roman
```

Обычно так делать не следует. Механизм предназначен для предотвращения случайного доступа и конфликтов имён, а не для обеспечения секретности.

---

### Double Underscores on Both Sides

Имена вида `__name__` имеют специальное значение в Python:

```python
class Person:
    def __init__(self):
        self.__name__ = "Roman"
```

Такое имя не следует использовать для обычных приватных атрибутов, поскольку двойные подчёркивания с обеих сторон обычно зарезервированы для специальных методов и атрибутов Python.

---

### Mutable Internal Objects

Даже если используется внутренний атрибут, содержащий изменяемый объект, этот объект может быть изменён:

```python
class User:
    def __init__(self):
        self._roles = ["user"]

    @property
    def roles(self):
        return self._roles


user = User()

user.roles.append("admin")

print(user.roles)
# ['user', 'admin']
```

Если необходимо строго контролировать изменение коллекции, следует предоставлять более ограниченный интерфейс или возвращать подходящую копию/неизменяемое представление.

---

### Setter Validation

Setter может отклонять некорректные значения:

```python
class Person:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Invalid age")

        self._age = value
```

Попытка:

```python
person = Person()
person.age = -1
```

приведёт к `ValueError`.

---

## Common Mistakes

### Mistake 1 — Thinking `_name` Is Truly Private

Неправильно считать, что:

```python
self._name
```

делает атрибут недоступным извне.

В Python это только соглашение.

---

### Mistake 2 — Thinking `__name` Provides Security

Name mangling не предназначен для защиты секретных данных:

```python
self.__password = password
```

Такой атрибут не следует рассматривать как механизм безопасного хранения паролей или другой секретной информации.

---

### Mistake 3 — Using Double Underscores Everywhere

Не следует использовать `__attribute` без необходимости.

Name mangling полезен прежде всего при необходимости избежать конфликтов имён в иерархии наследования.

В большинстве случаев одного `_` достаточно для обозначения внутреннего API.

---

### Mistake 4 — Exposing Internal Mutable Data

Прямой возврат внутреннего списка может позволить внешнему коду изменить состояние объекта:

```python
class User:
    def __init__(self):
        self._roles = ["user"]

    @property
    def roles(self):
        return self._roles
```

Теперь внешний код может выполнить:

```python
user.roles.clear()
```

Если такое изменение не должно быть разрешено, интерфейс следует спроектировать иначе.

---

### Mistake 5 — Duplicating Validation

Если значение можно изменить разными способами, проверки не следует копировать во множество мест.

Например, property setter позволяет централизовать проверку:

```python
class Person:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value
```

Теперь вся установка `age` проходит через одно место проверки.

---

### Mistake 6 — Confusing Encapsulation with Hiding

Инкапсуляция не означает, что абсолютно все внутренние данные должны быть скрыты.

Главная цель — определить чёткий интерфейс и контролировать взаимодействие с состоянием объекта там, где это действительно необходимо.

---

## Related Concepts

* Classes — классы, объединяющие состояние и поведение.
* Objects — экземпляры классов.
* Attributes — данные объекта или класса.
* Methods — поведение объекта.
* `@property` — механизм создания управляемых свойств.
* Name Mangling — изменение имён атрибутов с двойным подчёркиванием.
* Abstraction — сокрытие сложности реализации за простым интерфейсом.
* Inheritance — создание новых классов на основе существующих.
* Polymorphism — использование объектов разных типов через общий интерфейс.
* `__slots__` — механизм ограничения набора атрибутов экземпляра.
* Special Methods — специальные методы Python.

---

## Key Takeaways

* Инкапсуляция объединяет состояние и поведение объекта и помогает контролировать доступ к внутренней реализации.
* Python не имеет строгих модификаторов `private` и `protected`.
* `_name` — соглашение об обозначении внутреннего атрибута.
* `__name` запускает name mangling.
* Name mangling не обеспечивает абсолютную приватность.
* Имена `__name__` относятся к специальному синтаксису Python и не являются обычным способом обозначения приватных атрибутов.
* `@property` позволяет контролировать доступ к атрибутам через интерфейс свойства.
* Setter позволяет проверять значения перед изменением состояния.
* Методы могут использоваться для контролируемого изменения внутреннего состояния.
* Инкапсуляция помогает поддерживать инварианты объектов.
* В Python важную роль играют соглашения и дизайн интерфейса, а не жёсткие ограничения доступа.
* Хорошая инкапсуляция позволяет изменять внутреннюю реализацию, сохраняя стабильный внешний интерфейс.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Data model — Classes
* Python Language Reference — Data model — Customization
* Python Language Reference — Reserved classes of identifiers
* Python 3.14 Tutorial — Classes
* Python 3.14 Tutorial — Private Variables and Class-local References
* Python 3.14 Tutorial — Odds and Ends
* Python Standard Library — Built-in Functions — `property()`
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html#classes
* Official documentation: https://docs.python.org/3.14/reference/lexical_analysis.html#reserved-classes-of-identifiers
* Official documentation: https://docs.python.org/3.14/tutorial/classes.html#private-variables
* Official documentation: https://docs.python.org/3.14/library/functions.html#property
