from fastapi import APIRouter, Depends, Request, HTTPException, Body
from sqlalchemy.orm import Session
from nsuda.db import crud, schemas
from hashlib import sha256


router = APIRouter(prefix="/admin")

from nsuda.routers.roots import templates



@router.get("/")
async def index(request: Request, 
                password: str = None, db: Session = Depends(crud.get_db)):
    message = None
    db_user = crud.get_user(db, user_id=1)
    if db_user:
        if password:
            if sha256(password.encode('utf-8 ')).hexdigest() == db_user.password_hash:
                return templates.TemplateResponse("admin.html", 
                                                { "request": request, 
                                                "password": password,
                                                    "message": message })
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
    raise HTTPException(status_code=404)

from nsuda.xray import handler

async def validate_password(password: str, db: Session = Depends(crud.get_db)):
    db_user = crud.get_user(db, user_id=1)
    if sha256(password.encode('utf-8 ')).hexdigest() != db_user.password_hash:
        raise HTTPException(status_code=404)
    return password

from urllib.parse import urlparse, parse_qs

@router.post("/")
async def update_user(request: Request,
                      user_info = Body(),
                      password = Depends(validate_password),
                      db: Session = Depends(crud.get_db)):
    parsed_url = urlparse("?" + user_info.decode())
    data = parse_qs(parsed_url.query)
    email = data["email"][0]
    added_days = int(data["added_days"][0])
    if not email or not added_days:
        raise HTTPException(status_code=404)

    db_user = crud.get_user_by_email(db, email=email)
    if db_user:
        db_user.days_left += added_days
        crud.update_user(db, user=db_user)
    else:
        new_user = schemas.UserCreate(email=email, 
                                        days_left=added_days, password_hash="")
        crud.create_user(db, user=new_user)
    message = "User created successful!"
    return templates.TemplateResponse("admin.html", 
                                            { "request": request, 
                                            "password": password,
                                            "message": message })

@router.get("/get_uuid")
async def get_uuid(_ = Depends(validate_password)):
    return (await handler.HandlerBuilder.get_instanse()).cur_uuid
        
@router.get("/get_users")
async def get_users(_ = Depends(validate_password), 
                   db: Session = Depends(crud.get_db)):
    return crud.get_all_users(db)
    