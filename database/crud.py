# database/crud.py
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.connection import SessionLocal


def create(model: type, **fields: Any):
    """
    Создать новую запись.

    Пример:
        create(
            User,
            username="roman",
            password="123"
        )
    """

    with SessionLocal() as session:
        obj = model(**fields)

        session.add(obj)
        session.commit()
        session.refresh(obj)

        return obj


def get(model: type, object_id: int):
    """
    Получить одну запись по ID.

    Пример:
        get(User, 1)
    """

    with SessionLocal() as session:
        return session.get(model, object_id)


def get_all(model: type, **filters: Any):
    """
    Получить все записи с указанными фильтрами.

    Примеры:
        get_all(User)

        get_all(Task, user_id=1)

        get_all(Task, topic="lists", difficulty="easy")
    """

    with SessionLocal() as session:
        query = select(model)

        for field, value in filters.items():
            column = getattr(model, field)
            query = query.where(column == value)

        return list(session.scalars(query).all())


def update_field(
        model: type,
        object_id: int,
        field: str,
        value: Any,
):
    """
    Изменить одно поле записи.

    Пример:
        update_field(
            User,
            1,
            "username",
            "new_username"
        )
    """

    with SessionLocal() as session:
        obj = session.get(model, object_id)

        if obj is None:
            return None

        if not hasattr(model, field):
            raise ValueError(
                f"Field '{field}' does not exist in {model.__name__}"
            )

        setattr(obj, field, value)

        session.commit()
        session.refresh(obj)

        return obj


def update(
        model: type,
        object_id: int,
        **fields: Any,
):
    """
    Изменить несколько полей записи.

    Пример:
        update(
            Task,
            1,
            solution_text="print('Hello')",
            score=10
        )
    """

    with SessionLocal() as session:
        obj = session.get(model, object_id)

        if obj is None:
            return None

        for field, value in fields.items():
            if not hasattr(model, field):
                raise ValueError(
                    f"Field '{field}' does not exist in {model.__name__}"
                )

            setattr(obj, field, value)

        session.commit()
        session.refresh(obj)

        return obj


def delete(model: type, object_id: int):
    """
    Удалить запись по ID.

    Пример:
        delete(Task, 1)
    """

    with SessionLocal() as session:
        obj = session.get(model, object_id)

        if obj is None:
            return False

        session.delete(obj)
        session.commit()

        return True
