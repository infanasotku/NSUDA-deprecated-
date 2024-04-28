from fastapi.routing import APIRouter
from fastapi import Depends, Request
from typing import Annotated
from database.shemas import BaseUserModel
from api.auth.auth import AuthFactory


router = APIRouter()


@router.get('/')
async def index(
    model: Annotated[BaseUserModel, Depends(AuthFactory.build)]
) -> BaseUserModel:
    return model


@router.post("/signout")
async def signout(request: Request):
    if 'auth_service' in request.session:
        request.session.clear()
