from fastapi import FastAPI
import api.auth as auth
from starlette.middleware.sessions import SessionMiddleware
from settings import get_settings


def configure(app: FastAPI):
    # mounting apis
    app.mount("/auth", auth.create())

    # mounting middlewares
    app.add_middleware(
        SessionMiddleware,
        secret_key=get_settings().session_secret
    )
