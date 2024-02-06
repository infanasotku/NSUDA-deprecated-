from fastapi import FastAPI
from core.middlewares.error import HttpErrorMiddleware

def setup_core_middlewares(app: FastAPI):
    app.add_middleware(HttpErrorMiddleware)
