# Python Teacher AI

Учебный проект по созданию RAG-системы.

Проект демонстрирует полный pipeline подготовки базы знаний:

```text
Markdown-файлы
      ↓
Загрузка документов
      ↓
Семантическое разбиение на chunks
      ↓
Создание embeddings
      ↓
Qdrant
      ↓
Семантический поиск
      ↓
Получение релевантных фрагментов
```

## Цель проекта

Основная цель проекта — продемонстрировать работу основных компонентов RAG-системы:

* подготовка базы знаний;
* загрузка документов;
* семантическое разбиение документов на chunks;
* создание metadata;
* создание embeddings;
* хранение векторных представлений в Qdrant;
* семантический поиск;
* проверка качества retrieval.

---

# Технологии

* Python 3.14
* OpenAI API
* `text-embedding-3-small`
* Qdrant
* Docker
* Docker Compose
* `qdrant-client`
* `python-dotenv`

---

# Структура проекта

```text
python_teacher_aI/
│
├── knowledge/
│   ├── basics/
│   │   ├── variables.md
│   │   ├── data_types.md
│   │   ├── conditions.md
│   │   ├── loops.md
│   │   └── functions.md
│   │
│   ├── data_structures/
│   │   ├── list.md
│   │   ├── tuple.md
│   │   ├── set.md
│   │   └── dict.md
│   │
│   └── oop/
│       ├── classes.md
│       ├── encapsulation.md
│       ├── inheritance.md
│       ├── polymorphism.md
│       └── magic_methods.md
│
├── knowledgebase_pipeline/
│   ├── __init__.py
│   ├── config.py
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   └── vector_store.py
│
├── data/
│   ├── chunks/
│   │   ├── chunks.jsonl
│   │   └── embeddings.jsonl
│   │
│   └── rag_test_report.txt
│
├── docker-compose.yml
├── requirements.txt
├── test_rag.py
├── .env.example
├── .gitignore
└── README.md
```

---

# Требования

Перед запуском необходимо установить:

* Python 3.14;
* Docker Desktop;
* Git;

Qdrant запускается локально в Docker.


---

# 1. Клонирование проекта

Клонировать репозиторий:

```powershell
git clone https://github.com/uldiniumGit/python-teacher-ai.git
```

Перейти в директорию проекта:

```powershell
cd python-teacher-ai
```

---

# 2. Создание виртуального окружения

Создать виртуальное окружение:

```powershell
python -m venv .venv
```

Активировать его:

```powershell
.venv\Scripts\Activate.ps1
```

---

# 3. Установка зависимостей

Установить зависимости проекта:

```powershell
pip install -r requirements.txt
```

---

# 4. Настройка переменных окружения

В корне проекта находится файл:

```text
.env.example
```

Создать на его основе файл `.env`:

```powershell
Copy-Item .env.example .env
```

Открыть `.env` и указать свой OpenAI API key:

```dotenv
OPENAI_API_KEY=your_openai_api_key
```

Остальные параметры можно оставить без изменений.

Пример конфигурации:

```dotenv
OPENAI_API_KEY=your_openai_api_key

EMBEDDING_MODEL=text-embedding-3-small

CHUNK_SIZE=800
CHUNK_OVERLAP=100

QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION=python_knowledge
```

---

# 5. Запуск Qdrant в Docker

Qdrant используется как локальная векторная база данных.

Перед запуском pipeline необходимо запустить Docker Desktop.

Затем в директории проекта выполнить:

```powershell
docker compose up -d
```

Проверить состояние контейнера:

```powershell
docker compose ps
```

Контейнер Qdrant должен иметь статус `Up`.

Qdrant будет доступен по адресу:

```text
http://localhost:6333
```

Для остановки контейнера:

```powershell
docker compose stop
```

Для повторного запуска:

```powershell
docker compose start
```

Данные Qdrant сохраняются в Docker volume и не удаляются при обычной остановке контейнера.

> Не используйте `docker compose down -v`, если необходимо сохранить созданную базу Qdrant. Эта команда удаляет Docker volume вместе с данными.

---

# 6. Запуск pipeline

Файлы pipeline запускаются **последовательно**, один за другим.

Автоматического единого файла запуска pipeline в проекте нет.

Порядок запуска следующий.

## Шаг 1. Проверка конфигурации

```powershell
python knowledgebase_pipeline/config.py
```

Скрипт проверяет конфигурацию проекта и наличие необходимых параметров окружения.

---

## Шаг 2. Загрузка документов

```powershell
python knowledgebase_pipeline/loader.py
```

Скрипт загружает Markdown-файлы из директории:

```text
knowledge/
```

В результате формируется набор документов для дальнейшей обработки.

---

## Шаг 3. Создание chunks

```powershell
python knowledgebase_pipeline/chunker.py
```

Скрипт:

* анализирует структуру Markdown;
* учитывает заголовки `#`, `##`, `###`;
* сохраняет code blocks;
* разделяет документы на семантически связанные фрагменты;
* создаёт metadata;
* присваивает каждому chunk уникальный ID.

Результат сохраняется в:

```text
data/chunks/chunks.jsonl
```

---

## Шаг 4. Создание embeddings

```powershell
python knowledgebase_pipeline/embeddings.py
```

Для каждого chunk создаётся embedding с использованием модели:

```text
text-embedding-3-small
```

Результат сохраняется в:

```text
data/chunks/embeddings.jsonl
```

---

## Шаг 5. Загрузка embeddings в Qdrant

Перед этим шагом Qdrant должен быть запущен:

```powershell
docker compose up -d
```

Затем:

```powershell
python knowledgebase_pipeline/vector_store.py
```

Скрипт:

* подключается к Qdrant;
* создаёт коллекцию `python_knowledge`, если она отсутствует;
* загружает embeddings;
* сохраняет текст chunks;
* сохраняет metadata;
* выполняет проверку количества загруженных точек.

---

# 7. Тестирование RAG

После выполнения всех предыдущих шагов можно запустить:

```powershell
python test_rag.py
```

Тест выполняет семантический поиск по базе знаний.

Используются тестовые запросы:

```text
Что такое list в Python?

Что такое наследование в Python?

Что такое магические методы в Python?
```

Для каждого запроса:

1. создаётся embedding запроса;
2. выполняется поиск в Qdrant;
3. извлекаются наиболее релевантные chunks;
4. выводится similarity score;
5. выводятся metadata найденных chunks;
6. выводится содержимое найденных фрагментов.

Результаты тестирования сохраняются в:

```text
data/rag_test_report.txt
```

---

# Полный порядок запуска

После установки проекта весь pipeline запускается следующими командами:

```powershell
docker compose up -d

python knowledgebase_pipeline/config.py

python knowledgebase_pipeline/loader.py

python knowledgebase_pipeline/chunker.py

python knowledgebase_pipeline/embeddings.py

python knowledgebase_pipeline/vector_store.py

python test_rag.py
```

Каждый следующий этап использует результат предыдущего.

---

# Результат pipeline

После успешного выполнения pipeline получаем:

```text
knowledge/*.md
       ↓
Documents
       ↓
Chunks
       ↓
data/chunks/chunks.jsonl
       ↓
Embeddings
       ↓
data/chunks/embeddings.jsonl
       ↓
Qdrant
       ↓
python_knowledge
       ↓
Semantic Retrieval
```

Текущий результат базы знаний:

```text
Chunks:              744
Embeddings:          744
Vector dimension:    1536
Embedding model:     text-embedding-3-small
Qdrant collection:   python_knowledge
Distance:             COSINE
```

---

# Данные для проверки

Сгенерированные файлы intentionally находятся в репозитории:

```text
data/chunks/chunks.jsonl
data/chunks/embeddings.jsonl
```

Это позволяет проверить результат работы ingestion pipeline без необходимости генерировать embeddings заново.

Также в репозитории находится отчёт:

```text
data/rag_test_report.txt
```

с результатами тестирования semantic retrieval.

---

# Источник базы знаний

Материалы базы знаний подготовлены на основе официальной документации Python 3.14:

https://docs.python.org/3.14/

Темы организованы по категориям:

* Basics
* Data Structures
* Object-Oriented Programming

Markdown-файлы имеют структуру, подготовленную для дальнейшей RAG-обработки.

