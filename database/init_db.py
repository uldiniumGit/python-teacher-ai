# database/init_db.py
from database.connection import engine
from database.models import Base


def create_tables():
    print("1. Starting create_tables()", flush=True)

    print("2. Connecting to PostgreSQL...", flush=True)

    with engine.connect() as connection:
        print("3. PostgreSQL connection established", flush=True)

    print("4. Creating tables...", flush=True)

    Base.metadata.create_all(bind=engine)

    print("5. Tables created", flush=True)


if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully.", flush=True)
