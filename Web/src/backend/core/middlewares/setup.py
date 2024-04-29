from fastapi import FastAPI
from core.middlewares.error import HttpErrorMiddleware
from fastapi.middleware.cors import CORSMiddleware
from settings import get_settings


def setup_core_middlewares(app: FastAPI):
    app.add_middleware(HttpErrorMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=get_settings().cors_origins,
        allow_credentials=True,
        allow_methods=get_settings().cors_allow_methods,
        allow_headers=get_settings().cors_allow_headers,
    )
