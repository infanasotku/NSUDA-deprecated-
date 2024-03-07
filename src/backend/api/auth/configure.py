from api.auth.routers.google import google
from api.auth.routers.index import default
from api.auth.settings import auth_services
from fastapi import FastAPI
from api.auth.dependency import auth_by_google


def configure(app: FastAPI):
    # Routers
    app.include_router(google, prefix='/google')
    app.include_router(default, prefix='/default')

    # Auth services
    auth_services['google'] = auth_by_google
