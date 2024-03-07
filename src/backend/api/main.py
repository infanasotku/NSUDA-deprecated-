from fastapi import FastAPI

api = FastAPI(
    redoc_url=None,
    docs_url=None
)

from api.configure import configure

configure(api)
