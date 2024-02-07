from fastapi import FastAPI
from api.nsuda_api.main import nsuda_api

def configure(app: FastAPI):
    # mounting apis
    app.mount("/nsuda", nsuda_api)