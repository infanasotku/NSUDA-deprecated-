from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import site_root.site_root.wsgi as django
from api.main import api
from core.middlewares.setup import setup_core_middlewares

def configure(app: FastAPI):
    '''Configures all app.
    1) Mounts api
    2) Mounts django
    3) Mounts middlewares
    '''
    # mount api
    app.mount("/api", api)

    # mount Django app
    app.mount("/", WSGIMiddleware(django.application))
    
    # mount core middlewares
    setup_core_middlewares(app)