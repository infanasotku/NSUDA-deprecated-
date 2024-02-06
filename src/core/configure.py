from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware


def configure(app: FastAPI):
    '''Configures all app.
    1) Mounts api
    2) Mounts django
    '''


    # mount Django app
    