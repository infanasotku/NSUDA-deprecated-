from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from ..db import crud, schemas


router = APIRouter()



@router.get("/get_config")
async def get_config(email: str,  db: Session = Depends(crud.get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user:
        if db_user.days_left == 0:
            return { "error": 'License is over, top up your account' }
    else:
        return { "error": f'User: {email} - is not exist' }
    return "config...."
