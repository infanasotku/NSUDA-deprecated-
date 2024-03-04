from fastapi import FastAPI
from api.nsuda_api.main import nsuda_api
from api.auth.main import auth
from starlette.middleware.sessions import SessionMiddleware
from api.env.global_api_env import SESSION_SECRET

def configure(app: FastAPI):
    # mounting apis
    app.mount("/nsuda", nsuda_api)
    app.mount("/auth", auth)

    # mounting middlewares
    app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)