from fastapi.routing import APIRouter
from fastapi import Depends, Request
from typing import Annotated
from api.auth.database.shemas import BaseUserModel


default = APIRouter()

from api.auth.dependency import auth
@default.get('/')
async def index(model: Annotated[BaseUserModel, Depends(auth)]) -> BaseUserModel:
    return model

@default.post("/signout")
async def signout(request: Request):
    if 'auth_service' in request.session:
        request.session.clear()