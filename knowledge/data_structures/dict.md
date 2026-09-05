# Dictionary

## Definition

Словарь (`dict`) — это встроенный изменяемый тип данных Python, предназначенный для хранения данных в виде пар «ключ — значение» (`key-value pairs`).

Каждый ключ в словаре является уникальным и используется для доступа к соответствующему значению.

```python
user = {
    "name": "Alice",
    "age": 25,
    "city": "Da Nang"
}
```

В данном примере `"name"`, `"age"` и `"city"` являются ключами, а `"Alice"`, `25` и `"Da Nang"` — соответствующими значениями.

---

## Purpose

Словари используются для хранения и организации данных, когда каждому значению соответствует определённый ключ.

Они особенно полезны, когда:

* данные имеют структуру «ключ — значение»;
* к значениям необходимо обращаться по понятным именам;
* требуется быстрый поиск значения по ключу;
* данные необходимо изменять после создания;
* нужно представить структурированную информацию;
* объект необходимо представить набором его свойств.

Например, информацию о пользователе удобно хранить в словаре:

```python
user = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}
```

В отличие от списка, где элементы обычно идентифицируются числовыми индексами, словарь позволяет обращаться к данным по смысловым ключам.

---

## Core Concepts

### Key-Value Pairs

Словарь состоит из пар «ключ — значение».

```python
user = {
    "name": "Alice",
    "age": 25
}
```

В этом примере:

* `"name"` — ключ;
* `"Alice"` — значение;
* `"age"` — ключ;
* `25` — значение.

Ключи внутри одного словаря должны быть уникальными.

Если один ключ указан несколько раз, используется последнее значение:

```python
data = {
    "name": "Alice",
    "name": "Bob"
}

print(data)
```

Результат:

```python
{'name': 'Bob'}
```

---

### Keys

Ключом словаря может быть только хешируемый объект.

Например, допустимыми ключами являются строки, целые числа, числа с плавающей точкой и кортежи, состоящие из хешируемых объектов.

```python
data = {
    "name": "Alice",
    1: "one",
    3.14: "pi",
    (1, 2): "tuple"
}
```

Изменяемые объекты, например списки и словари, не могут использоваться в качестве ключей.

```python
# TypeError
data = {
    [1, 2]: "value"
}
```

Ключи должны быть уникальными.

---

### Values

Значением словаря может быть объект любого типа.

Разные значения одного словаря могут иметь совершенно разные типы:

```python
data = {
    "name": "Alice",
    "age": 25,
    "active": True,
    "skills": ["Python", "SQL"],
    "profile": {
        "city": "Da Nang"
    }
}
```

В отличие от ключей, значения не обязаны быть уникальными или хешируемыми.

---

### Creating Dictionaries

Словарь можно создать с помощью фигурных скобок:

```python
user = {
    "name": "Alice",
    "age": 25
}
```

Пустой словарь создаётся следующим образом:

```python
user = {}
```

Также можно использовать конструктор `dict()`:

```python
user = dict(name="Alice", age=25)
```

Словарь можно создать из последовательности пар «ключ — значение»:

```python
user = dict([
    ("name", "Alice"),
    ("age", 25)
])
```

---

### Accessing Values

Для доступа к значению используется соответствующий ключ:

```python
user = {
    "name": "Alice",
    "age": 25
}

print(user["name"])
```

Результат:

```text
Alice
```

Если ключ отсутствует, обращение через квадратные скобки вызывает исключение `KeyError`:

```python
print(user["email"])
```

---

### `get()`

Метод `get()` используется для получения значения по ключу без возникновения `KeyError`, если ключ отсутствует.

```python
user = {
    "name": "Alice"
}

print(user.get("name"))
print(user.get("email"))
```

Результат:

```text
Alice
None
```

Можно указать значение по умолчанию:

```python
email = user.get("email", "Not provided")

print(email)
```

Результат:

```text
Not provided
```

---

### Adding and Updating Items

Новую пару «ключ — значение» можно добавить с помощью присваивания:

```python
user = {}

user["name"] = "Alice"
user["age"] = 25
```

Если такой ключ уже существует, его значение будет заменено:

```python
user["age"] = 26
```

Поскольку словарь является изменяемым объектом, его содержимое можно изменять после создания.

---

### `update()`

Метод `update()` позволяет добавить или изменить несколько элементов одновременно.

```python
user = {
    "name": "Alice",
    "age": 25
}

user.update({
    "age": 26,
    "city": "Da Nang"
})
```

Результат:

```python
{
    "name": "Alice",
    "age": 26,
    "city": "Da Nang"
}
```

Существующий ключ обновляется, а новый ключ добавляется.

---

### Removing Items with `del`

Для удаления элемента можно использовать оператор `del`:

```python
user = {
    "name": "Alice",
    "age": 25
}

del user["age"]
```

После выполнения:

```python
{
    "name": "Alice"
}
```

Если ключ отсутствует, возникает `KeyError`.

---

### `pop()`

Метод `pop()` удаляет указанный ключ и возвращает его значение:

```python
user = {
    "name": "Alice",
    "age": 25
}

age = user.pop("age")

print(age)
print(user)
```

Результат:

```text
25
{'name': 'Alice'}
```

Можно указать значение по умолчанию, которое будет возвращено, если ключ отсутствует:

```python
age = user.pop("age", None)
```

---

### `popitem()`

Метод `popitem()` удаляет и возвращает последнюю добавленную пару «ключ — значение».

```python
user = {
    "name": "Alice",
    "age": 25,
    "city": "Da Nang"
}

item = user.popitem()

print(item)
```

Результатом является кортеж из двух элементов: ключа и его значения.

---

### `clear()`

Метод `clear()` удаляет все элементы словаря:

```python
user = {
    "name": "Alice",
    "age": 25
}

user.clear()

print(user)
```

Результат:

```python
{}
```

---

### `keys()`

Метод `keys()` возвращает представление (`view`) ключей словаря:

```python
user = {
    "name": "Alice",
    "age": 25
}

print(user.keys())
```

Его можно использовать для перебора ключей:

```python
for key in user.keys():
    print(key)
```

Представление ключей отражает изменения исходного словаря.

---

### `values()`

Метод `values()` возвращает представление значений словаря:

```python
user = {
    "name": "Alice",
    "age": 25
}

for value in user.values():
    print(value)
```

Значения могут повторяться:

```python
data = {
    "a": 10,
    "b": 10
}
```

---

### `items()`

Метод `items()` возвращает представление пар «ключ — значение»:

```python
user = {
    "name": "Alice",
    "age": 25
}

for key, value in user.items():
    print(key, value)
```

`items()` удобно использовать, когда во время итерации нужны одновременно ключ и значение.

---

### Membership Testing

Оператор `in` проверяет наличие ключа в словаре:

```python
user = {
    "name": "Alice",
    "age": 25
}

print("name" in user)
print("email" in user)
```

Результат:

```text
True
False
```

При проверке словаря оператор `in` проверяет именно ключи, а не значения.

Для проверки наличия значения используется `values()`:

```python
print("Alice" in user.values())
```

---

### Iteration

При непосредственной итерации по словарю перебираются его ключи:

```python
user = {
    "name": "Alice",
    "age": 25
}

for key in user:
    print(key)
```

Для перебора значений используется:

```python
for value in user.values():
    print(value)
```

Для перебора ключей и значений:

```python
for key, value in user.items():
    print(key, value)
```

---

### Insertion Order

Словари сохраняют порядок добавления элементов.

```python
data = {}

data["first"] = 1
data["second"] = 2
data["third"] = 3

for key in data:
    print(key)
```

Результат:

```text
first
second
third
```

Изменение значения существующего ключа не изменяет его позицию:

```python
data["first"] = 100
```

Ключ `"first"` останется на своей исходной позиции.

Если удалить ключ, а затем добавить его снова, он будет находиться в новой позиции.

---

### Dictionary Comprehensions

Генератор словаря (`dictionary comprehension`) позволяет создавать словари компактным способом.

```python
squares = {
    number: number ** 2
    for number in range(5)
}
```

Результат:

```python
{
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16
}
```

Можно использовать условие:

```python
squares = {
    number: number ** 2
    for number in range(10)
    if number % 2 == 0
}
```

---

### Nested Dictionaries

Значением словаря может быть другой словарь.

```python
users = {
    "user1": {
        "name": "Alice",
        "age": 25
    },
    "user2": {
        "name": "Bob",
        "age": 30
    }
}
```

Для доступа к вложенному значению используются несколько ключей:

```python
print(users["user1"]["name"])
```

Результат:

```text
Alice
```

Вложенные словари позволяют представлять иерархические и сложные структуры данных.

---

### Dictionary Views

Методы `keys()`, `values()` и `items()` возвращают специальные объекты-представления (`view objects`), а не обычные списки.

Они отражают изменения исходного словаря.

```python
data = {
    "a": 1,
    "b": 2
}

keys = data.keys()

data["c"] = 3

print(keys)
```

После добавления `"c"` представление `keys` также отражает этот новый ключ.

---

## Syntax

Создание словаря:

```python
data = {
    key1: value1,
    key2: value2,
    key3: value3
}
```

Создание пустого словаря:

```python
data = {}
```

Создание с помощью `dict()`:

```python
data = dict(key1=value1, key2=value2)
```

Доступ к значению:

```python
value = data[key]
```

Безопасный доступ:

```python
value = data.get(key)
value = data.get(key, default_value)
```

Добавление или изменение элемента:

```python
data[key] = value
```

Обновление нескольких элементов:

```python
data.update(other)
```

Удаление элемента:

```python
del data[key]
```

Удаление с возвратом значения:

```python
value = data.pop(key)
```

Проверка наличия ключа:

```python
if key in data:
    ...
```

Получение ключей:

```python
keys = data.keys()
```

Получение значений:

```python
values = data.values()
```

Получение пар «ключ — значение»:

```python
items = data.items()
```

Итерация по ключам:

```python
for key in data:
    ...
```

Итерация по ключам и значениям:

```python
for key, value in data.items():
    ...
```

Генератор словаря:

```python
result = {
    key: value
    for item in iterable
}
```

---

## Rules

1. `dict` — встроенный изменяемый тип данных Python для хранения пар «ключ — значение».
2. Каждый ключ внутри словаря должен быть уникальным.
3. Ключи должны быть хешируемыми.
4. Значения могут иметь любой тип.
5. Словари являются изменяемыми (`mutable`).
6. Обращение к отсутствующему ключу через `data[key]` вызывает `KeyError`.
7. Метод `get()` позволяет безопасно получать значение отсутствующего ключа.
8. Оператор `in` проверяет наличие ключа.
9. Методы `keys()`, `values()` и `items()` возвращают представления словаря.
10. Словари сохраняют порядок добавления элементов.
11. Присваивание существующему ключу заменяет его значение.
12. `update()` позволяет добавить или изменить несколько элементов.
13. `pop()` удаляет указанный элемент и возвращает его значение.
14. `popitem()` удаляет и возвращает последнюю добавленную пару.
15. `clear()` удаляет все элементы словаря.
16. Значением словаря может быть другой словарь или любая другая структура данных.
17. Не следует изменять размер словаря во время непосредственной итерации по нему.

---

## Examples

### Example 1 — Creating a Dictionary

```python
user = {
    "name": "Alice",
    "age": 25,
    "active": True
}

print(user)
```

Explanation:

Словарь содержит три пары «ключ — значение». Значения имеют разные типы данных.

---

### Example 2 — Accessing Values

```python
user = {
    "name": "Alice",
    "age": 25
}

print(user["name"])
print(user["age"])
```

Explanation:

Квадратные скобки используются для доступа к значению по ключу.

---

### Example 3 — Safe Access with `get()`

```python
user = {
    "name": "Alice"
}

email = user.get("email", "Not provided")

print(email)
```

Explanation:

Ключ `"email"` отсутствует, поэтому метод `get()` возвращает указанное значение по умолчанию.

---

### Example 4 — Adding and Updating Values

```python
user = {
    "name": "Alice"
}

user["age"] = 25
user["name"] = "Bob"

print(user)
```

Explanation:

Ключ `"age"` добавляется, потому что его раньше не было. Значение ключа `"name"` заменяется.

---

### Example 5 — Removing an Item

```python
user = {
    "name": "Alice",
    "age": 25
}

age = user.pop("age")

print(age)
print(user)
```

Explanation:

`pop()` удаляет ключ `"age"` и возвращает его значение.

---

### Example 6 — Iterating Over a Dictionary

```python
user = {
    "name": "Alice",
    "age": 25,
    "city": "Da Nang"
}

for key, value in user.items():
    print(f"{key}: {value}")
```

Explanation:

`items()` позволяет получить ключ и значение на каждой итерации.

---

### Example 7 — Checking Whether a Key Exists

```python
user = {
    "name": "Alice",
    "age": 25
}

if "age" in user:
    print("Age is available")
```

Explanation:

Оператор `in` проверяет наличие `"age"` среди ключей словаря.

---

### Example 8 — Dictionary Comprehension

```python
squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)
```

Explanation:

Создаётся словарь, в котором каждое число является ключом, а его квадрат — соответствующим значением.

---

### Example 9 — Nested Dictionary

```python
user = {
    "name": "Alice",
    "profile": {
        "age": 25,
        "city": "Da Nang"
    }
}

print(user["profile"]["city"])
```

Explanation:

Значение `"profile"` является вложенным словарём. Для получения `"city"` используются два последовательных обращения по ключу.

---

### Example 10 — Counting Values

```python
words = ["python", "java", "python", "go", "python", "java"]

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
```

Результат:

```python
{
    "python": 3,
    "java": 2,
    "go": 1
}
```

Explanation:

Если слово встречается впервые, `get()` возвращает `0`. Затем значение увеличивается на единицу.

---

### Example 11 — Updating Multiple Values

```python
user = {
    "name": "Alice",
    "age": 25
}

user.update({
    "age": 26,
    "city": "Da Nang"
})

print(user)
```

Explanation:

Значение `"age"` заменяется, а новый ключ `"city"` добавляется.

---

## Edge Cases

### Missing Key

Обращение к отсутствующему ключу через квадратные скобки вызывает `KeyError`.

```python
data = {
    "name": "Alice"
}

print(data["age"])
```

Если отсутствие ключа является нормальной ситуацией, можно использовать `get()`:

```python
print(data.get("age"))
```

---

### Duplicate Keys

При наличии одинаковых ключей используется последнее значение:

```python
data = {
    "name": "Alice",
    "name": "Bob"
}

print(data)
```

Результат:

```python
{"name": "Bob"}
```

---

### Unhashable Keys

Списки нельзя использовать в качестве ключей:

```python
data = {
    [1, 2]: "value"
}
```

Это вызывает `TypeError`.

Кортеж может использоваться в качестве ключа, если все его элементы хешируемы:

```python
data = {
    (1, 2): "value"
}
```

---

### Modifying Dictionary Size During Iteration

Добавление или удаление элементов во время итерации по тому же словарю может вызвать `RuntimeError`.

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

for key in data:
    del data[key]
```

Если необходимо удалить элементы, можно сначала создать отдельную коллекцию ключей:

```python
for key in list(data):
    del data[key]
```

---

### Missing Key with `pop()`

Если ключ отсутствует и значение по умолчанию не указано, `pop()` вызывает `KeyError`:

```python
data = {}

data.pop("name")
```

Можно указать значение по умолчанию:

```python
data.pop("name", None)
```

---

### `popitem()` on an Empty Dictionary

Вызов `popitem()` для пустого словаря вызывает `KeyError`:

```python
data = {}

data.popitem()
```

---

### Updating Values During Iteration

Изменение значения существующего ключа не изменяет размер словаря:

```python
data = {
    "a": 1,
    "b": 2
}

for key in data:
    data[key] *= 2
```

Это отличается от добавления или удаления ключей во время итерации.

---

## Common Mistakes

### Mistake 1 — Accessing a Missing Key

Неправильно:

```python
user = {
    "name": "Alice"
}

email = user["email"]
```

Если `"email"` отсутствует, возникает `KeyError`.

Если ключ может отсутствовать, используйте:

```python
email = user.get("email")
```

---

### Mistake 2 — Assuming `in` Checks Values

Неправильно:

```python
user = {
    "name": "Alice"
}

if "Alice" in user:
    print("Found")
```

Оператор `in` проверяет ключи.

Для проверки значения:

```python
if "Alice" in user.values():
    print("Found")
```

---

### Mistake 3 — Using a List as a Key

Неправильно:

```python
data = {
    [1, 2]: "value"
}
```

Список является изменяемым и нехешируемым объектом.

Если нужен составной ключ, можно использовать кортеж:

```python
data = {
    (1, 2): "value"
}
```

---

### Mistake 4 — Expecting `get()` to Add an Item

Метод `get()` только получает значение и не изменяет словарь.

```python
data = {}

data.get("name", "Alice")

print(data)
```

Словарь останется пустым.

Чтобы добавить элемент:

```python
data["name"] = "Alice"
```

---

### Mistake 5 — Changing Dictionary Size During Iteration

Не следует добавлять или удалять ключи непосредственно во время итерации по тому же словарю.

Если необходимо изменить размер словаря, сначала создайте отдельную коллекцию элементов или ключей для обработки.

---

### Mistake 6 — Confusing Keys and Values

Для словаря:

```python
user = {
    "name": "Alice",
    "age": 25
}
```

`"name"` и `"age"` являются ключами.

`"Alice"` и `25` являются значениями.

Это различие важно при использовании `in`, `keys()`, `values()` и `items()`.

---

## Related Concepts

* `list` — упорядоченная изменяемая последовательность.
* `tuple` — упорядоченная неизменяемая последовательность.
* `set` — коллекция уникальных элементов.
* `frozenset` — неизменяемое множество.
* `collections.defaultdict` — подкласс словаря, предоставляющий значения по умолчанию.
* `collections.Counter` — специализированный тип отображения для подсчёта хешируемых объектов.
* Hashability — свойство объекта, необходимое для использования его в качестве ключа словаря.
* Dictionary comprehension — компактный способ создания словарей.
* Iteration — перебор ключей, значений или пар словаря.
* JSON — формат обмена данными, объекты которого часто представляются в Python в виде словарей.

---

## Key Takeaways

* `dict` — встроенный тип данных Python для хранения пар «ключ — значение».
* Ключи словаря уникальны.
* Ключи должны быть хешируемыми.
* Значения могут иметь любой тип.
* Словари являются изменяемыми.
* `data[key]` используется для прямого доступа к значению.
* `data.get(key)` удобно использовать, когда ключ может отсутствовать.
* `keys()`, `values()` и `items()` предоставляют представления содержимого словаря.
* Оператор `in` проверяет наличие ключа.
* `update()` позволяет добавлять и изменять несколько элементов.
* `pop()` и `popitem()` используются для удаления элементов.
* Словари сохраняют порядок добавления элементов.
* Dictionary comprehensions позволяют компактно создавать словари.
* Вложенные словари позволяют представлять иерархические структуры данных.

---

## Source

* Python 3.14 Documentation
* Python Language Reference — Data model — Dictionaries
* Python Standard Library — Built-in Types — `dict`
* Python Standard Library — Mapping Types — `dict`
* Python 3.14 Tutorial — Data Structures
* Python 3.14 Tutorial — Dictionaries
* Official documentation: https://docs.python.org/3.14/reference/datamodel.html#dictionaries
* Official documentation: https://docs.python.org/3.14/library/stdtypes.html#mapping-types-dict
* Official documentation: https://docs.python.org/3.14/tutorial/datastructures.html#dictionaries
