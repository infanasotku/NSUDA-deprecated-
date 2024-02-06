from fastapi import FastAPI
from api.nsuda_api.routers.users import users

nsuda_api = FastAPI()

nsuda_api.include_router(users)