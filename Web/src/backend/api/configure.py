from fastapi import FastAPI
from api.auth.main import auth
from starlette.middleware.sessions import SessionMiddleware
from settings import get_settings


def configure(app: FastAPI):
    # mounting apis
    app.mount("/auth", auth)

    # mounting middlewares
    app.add_middleware(
        SessionMiddleware,
        secret_key=get_settings().session_secret
    )
