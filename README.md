# Python Teacher AI

Учебная AI-система для изучения Python.

Проект объединяет **RAG, несколько AI-агентов, PostgreSQL и Flask** в единую систему обучения:

```text
Пользователь
     ↓
   Flask
     ↓
RAG Retrieval
     ↓
AI Agents
 ┌───┼───────────┐
 ↓   ↓           ↓
Task Generator  Checker  Tutor
     ↓
PostgreSQL
```

## Возможности

Система позволяет:

* зарегистрироваться и войти в приложение;
* выбрать тему и сложность Python-задачи;
* получить сгенерированную AI практическую задачу;
* решить задачу;
* получить автоматическую проверку решения и оценку;
* задать дополнительные вопросы AI-репетитору;
* сохранять задачи, решения, оценки и диалоги в PostgreSQL;
* использовать базу знаний Python для генерации, проверки и объяснения материала.

---

# Технологии

* Python 3.14
* Flask
* OpenAI API
* Qdrant
* PostgreSQL
* SQLAlchemy
* psycopg
* Jinja2
* Docker / Docker Compose
* `qdrant-client`
* `text-embedding-3-small`

---

# Архитектура

Проект состоит из нескольких основных частей.

### Knowledge Base + RAG

Официальная документация Python преобразуется в RAG-базу:

```text
Markdown
   ↓
Loader
   ↓
Semantic Chunking
   ↓
Embeddings
   ↓
Qdrant
   ↓
Semantic Retrieval
```

RAG используется AI-агентами как контекст из проверенной базы знаний.

### AI Agents

В проекте работают три агента:

**Task Generator**

Получает тему, сложность и релевантный контекст из RAG и создаёт практическую задачу.

**Task Checker**

Получает условие задачи, решение пользователя и контекст RAG. Проверяет решение и возвращает:

* корректность;
* оценку от 0 до 10;
* ошибки;
* объяснение;
* рекомендации.

**Tutor**

Работает после проверки задачи. Использует условие, решение, результат проверки, RAG-контекст и историю диалога, чтобы
отвечать на вопросы пользователя и помогать разобраться в теме.

---

# Структура проекта

```text
python-teacher-ai/
│
├── ai/
│   ├── gpt.py
│   ├── task_generator.py
│   ├── task_checker.py
│   └── tutor.py
│
├── app/
│   ├── routes.py
│   └── pipeline.py
│
├── database/
│   ├── connection.py
│   ├── models.py
│   ├── crud.py
│   └── init_db.py
│
├── knowledge/
│   ├── basics/
│   ├── data_structures/
│   └── oop/
│
├── knowledgebase_pipeline/
│   ├── config.py
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── retrieval.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── generate.html
│   └── task.html
│
├── tests/
│   ├── test_task_generator.py
│   ├── test_task_checker.py
│   ├── test_tutor.py
│   └── test_pipeline.py
│
├── data/
│   └── chunks/
│
├── docker-compose.yml
├── requirements.txt
└── run.py
```

---
# Установка

Клонировать репозиторий:

```bash
git clone https://github.com/uldiniumGit/python-teacher-ai.git
cd python-teacher-ai
```

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать виртуальное окружение.

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

---

# Настройка `.env`

Создать файл `.env` на основе `.env.example`.

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

### Linux / macOS

```bash
cp .env.example .env
```

Открыть `.env` и указать свой OpenAI API key:

```dotenv
OPENAI_API_KEY=your_openai_api_key

EMBEDDING_MODEL=text-embedding-3-small

CHUNK_SIZE=800
CHUNK_OVERLAP=100

QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION=python_knowledge

POSTGRES_DB=python_teacher
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=15432

DATABASE_URL=postgresql+psycopg://postgres:postgres@127.0.0.1:15432/python_teacher

FLASK_SECRET_KEY=dev-secret-key
```

---

# Запуск

Для запуска Qdrant и PostgreSQL требуется Docker.

Установить и запустить Docker Desktop на Windows или Docker Engine + Docker Compose на Linux.

Из корня проекта выполнить:

```bash
docker compose up -d
```

Проверить состояние контейнеров:

```bash
docker compose ps
```

Проект использует два независимых Docker-сервиса:

* **Qdrant** — векторная база знаний;
* **PostgreSQL** — база данных приложения.

Qdrant доступен по адресу:

```text
http://localhost:6333
```

PostgreSQL доступен по адресу:

```text
localhost:15432
```

Инициализировать таблицы PostgreSQL:

```bash
python database/init_db.py
```


# RAG Pipeline

Если RAG-база ещё не подготовлена, выполнить:

```powershell
python knowledgebase_pipeline/config.py
python knowledgebase_pipeline/loader.py
python knowledgebase_pipeline/chunker.py
python knowledgebase_pipeline/embeddings.py
python knowledgebase_pipeline/vector_store.py
```

Основные результаты:

```text
data/chunks/chunks.jsonl
data/chunks/embeddings.jsonl
```

После загрузки в Qdrant агенты могут выполнять semantic retrieval и использовать найденные chunks как контекст.

Проверить retrieval:

```powershell
python test_rag.py
```

Результат сохраняется в:

```text
data/rag_test_report.txt
```

---

# Запуск AI Teacher

После запуска Docker, подготовки RAG и инициализации PostgreSQL:

```powershell
python run.py
```

Приложение доступно по адресу:

```text
http://127.0.0.1:5000
```

Основной пользовательский сценарий:

```text
Регистрация / вход
       ↓
Выбор темы и сложности
       ↓
RAG Retrieval
       ↓
Task Generator
       ↓
Задача
       ↓
Решение пользователя
       ↓
RAG Retrieval
       ↓
Task Checker
       ↓
Оценка + обратная связь
       ↓
Tutor
       ↓
Диалог по задаче
```

---

# Хранение данных

PostgreSQL содержит две таблицы:

```text
users
tasks
```

`users` хранит пользователей.

`tasks` хранит:

* тему;
* сложность;
* условие задачи;
* решение пользователя;
* результат проверки;
* оценку;
* дату создания;
* историю диалога с Tutor.

Полный диалог по задаче хранится в `tasks.solution_text`.

---

# Тестирование

Тесты AI-агентов:

```powershell
python tests/test_task_generator.py
python tests/test_task_checker.py
python tests/test_tutor.py
```

Полный тест pipeline:

```powershell
python tests/test_pipeline.py
```

Он проверяет последовательную работу:

```text
RAG
 ↓
Task Generator
 ↓
PostgreSQL
 ↓
Task Checker
 ↓
PostgreSQL
 ↓
Tutor
 ↓
PostgreSQL
```

---

# Текущий результат

RAG-база содержит:

```text
Chunks:              744
Embeddings:          744
Vector dimension:    1536
Embedding model:     text-embedding-3-small
Qdrant collection:   python_knowledge
Distance:             COSINE
```

База знаний включает основные темы Python:

* Basics;
* Data Structures;
* Object-Oriented Programming.

Источник материалов — официальная документация Python 3.14:

https://docs.python.org/3.14/

Сгенерированные chunks и embeddings находятся в репозитории:

```text
data/chunks/chunks.jsonl
data/chunks/embeddings.jsonl
```

Это позволяет ознакомиться с результатом подготовки RAG-базы без повторного запуска embeddings pipeline.

---

# Обновление зависимостей

После установки всех зависимостей в активированном `.venv`:

```powershell
pip freeze > requirements.txt
```

Проверить содержимое:

```powershell
Get-Content requirements.txt
```
