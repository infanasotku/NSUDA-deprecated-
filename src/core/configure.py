from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from site_root.site_root import wsgi
from api.main import api

def configure(app: FastAPI):
    '''Configures all app.
    1) Mounts api
    2) Mounts django
    '''
    # mount api
    app.mount("/api", api)

    # mount Django app
    app.mount("/", WSGIMiddleware(wsgi.application))
    