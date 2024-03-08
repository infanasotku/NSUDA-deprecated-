from fastapi import FastAPI
from core.middlewares.error import HttpErrorMiddleware
from fastapi.middleware.cors import CORSMiddleware
from api.env.global_api_env import CORS_ORIGINS, CORS_ALLOW_METHODS, CORS_ALLOW_HEADERS

def setup_core_middlewares(app: FastAPI):
    app.add_middleware(HttpErrorMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=CORS_ALLOW_METHODS,
        allow_headers=CORS_ALLOW_HEADERS,
    )

