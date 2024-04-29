from fastapi import FastAPI
from api.configure import configure


def create() -> FastAPI:
    api = FastAPI(
        redoc_url=None,
        docs_url=None
    )

    configure(api)
    return api
