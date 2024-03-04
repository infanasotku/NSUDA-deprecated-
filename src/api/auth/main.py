from fastapi import FastAPI
from api.auth.routers.google import google


auth = FastAPI()

auth.include_router(google, prefix='/google')
