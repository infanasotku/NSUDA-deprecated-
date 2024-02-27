from fastapi import FastAPI
from api.session.routers.auth import auth


session = FastAPI()

session.include_router(auth, '/auth')
