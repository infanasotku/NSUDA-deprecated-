import api.auth.routers.index as index
from fastapi import FastAPI


def configure(app: FastAPI):
    # Routers
    app.include_router(index.router)
