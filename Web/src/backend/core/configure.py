from fastapi import FastAPI
from api.main import api
from core.middlewares.setup import setup_core_middlewares

def configure(app: FastAPI):
    '''Configures all app.
    1) Mounts api
    2) Mounts middlewares
    '''
    # mount api
    app.mount("/api", api)

    # mount core middlewares
    setup_core_middlewares(app)