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
    message = None
    if email: # Email setted up by form
        db_user = crud.get_user_by_email(db, email=email)
        if db_user:
            db_user.days_left += added_days
            crud.update_user(db, user=db_user)
        else:
            new_user = schemas.UserCreate(email=email, 
                                          days_left=added_days, password_hash="")
            crud.create_user(db, user=new_user)
        message = "User created successful!"
    db_user = crud.get_user(db, user_id=1)
    if db_user:
        if not password:
            pass
        elif sha256(password.encode('utf-8 ')).hexdigest() == db_user.password_hash:
            return templates.TemplateResponse("admin.html", 
                                              { "request": request, 
                                               "password": password,
                                                "message": message })
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
    else:
        if password:
            hash = sha256(password.encode('utf-8 ')).hexdigest()
            new_user = schemas.UserCreate(email="Admin", 
                                          days_left=-1, 
                                          password_hash=hash)
            message = "Admin created successful!"
            crud.create_user(db, user=new_user)
            return templates.TemplateResponse("admin.html", 
                                              { "request": request, 
                                               "password": password,
                                                "message": message })
    response.status_code = status.HTTP_404_NOT_FOUND
    return "Page not found"

from nsuda.xray import handler

@router.get("/get_uuid")
async def get_uuid(password: str, response: Response, 
                   db: Session = Depends(crud.get_db)):
    db_user = crud.get_user(db, user_id=1)
    if not password:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        if sha256(password.encode('utf-8 ')).hexdigest() == db_user.password_hash:
            return handler.HandlerBuilder.get_instanse().cur_uuid