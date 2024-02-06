from fastapi import FastAPI

api = FastAPI()

from api.configure import configure

configure(api)
