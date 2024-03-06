from fastapi.routing import APIRouter
from fastapi import Depends, Request
from typing import Annotated


google = APIRouter()

from api.auth.dependency import auth_by_google
from api.auth.database.shemas import GoogleOIDCModel


@google.get("/")
async def index(model: Annotated[GoogleOIDCModel, Depends(auth_by_google)]) -> GoogleOIDCModel:
    return model

