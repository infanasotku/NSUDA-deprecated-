from fastapi import FastAPI
import api
from core.middlewares.setup import setup_core_middlewares


def configure(app: FastAPI):
    '''Configures all app.
    1) Mounts api
    2) Mounts middlewares
    '''
    # mount api
    app.mount("/api", api.create())

    # mount core middlewares
    setup_core_middlewares(app)
