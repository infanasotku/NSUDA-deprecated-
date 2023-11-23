from fastapi import APIRouter, Depends, Response, status, Request
from sqlalchemy.orm import Session
from ..db import crud, schemas
from hashlib import sha256


router = APIRouter(prefix="/admin")

from ..routers.roots import templates


@router.get("/")
async def index(response: Response, request: Request, 
                password: str = None, db: Session = Depends(crud.get_db), 
                email: str = None,
                added_days: int = None):
    if email: # Email setted up by form
        return email
    db_user = crud.get_user(db, user_id=1)
    if db_user:
        if not password:
            response.status_code = status.HTTP_404_NOT_FOUND
        elif db_user.password_hash == "":
            db_user.password_hash = sha256(password.encode('utf-8 ')).hexdigest()
            crud.update_user(db, user=db_user)
            return "New password set!"
        elif sha256(password.encode('utf-8 ')).hexdigest() == db_user.password_hash:
            return templates.TemplateResponse("admin.html", {"request": request, "password": password})
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
    return "Page not found"

