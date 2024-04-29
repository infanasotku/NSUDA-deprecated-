from fastapi import FastAPI
from api.auth.configure import configure


def create() -> FastAPI:
    auth = FastAPI()

    configure(auth)
    return auth
