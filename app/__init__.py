# app/__init__.py

import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


def create_app():
    app = Flask(
        __name__,
        template_folder=str(BASE_DIR / "templates"),
        static_folder=str(BASE_DIR / "static"),
    )

    app.secret_key = os.getenv(
        "FLASK_SECRET_KEY",
        "dev-secret-key",
    )

    from app.routes import main

    app.register_blueprint(main)

    return app
