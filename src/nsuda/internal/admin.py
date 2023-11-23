from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from ..db import crud, schemas
from hashlib import sha256


router = APIRouter(prefix="/admin")



@router.get("/")
async def index(response: Response, password: str = None, db: Session = Depends(crud.get_db)):
    db_user = crud.get_user_by_email(db, id=1)
    print(sha256(password).name)
    if db_user:
        if not password:
            response.status_code = status.HTTP_404_NOT_FOUND
        elif sha256(password).name == db_user.password_hash:
            return "Welcome to admin page!"
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code = status.HTTP_404_NOT_FOUND