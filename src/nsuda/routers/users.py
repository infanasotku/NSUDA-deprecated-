from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from nsuda.db import crud, models, schemas
from nsuda.db.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/get_config")
async def get_config(email: str,  db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    print(db_user)

@router.get("/create_config")
async def create_config(email: str,  db: Session = Depends(get_db)):
    user = schemas.UserCreate(email=email, days_left=1)
    return crud.create_user(db=db, user=user)