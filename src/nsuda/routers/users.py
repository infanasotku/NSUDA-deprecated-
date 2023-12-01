from fastapi import Depends, APIRouter, WebSocket
from sqlalchemy.orm import Session

from nsuda.db import crud


router = APIRouter()


from nsuda.xray import handler

@router.get("/get_config")
async def get_config(email: str,  db: Session = Depends(crud.get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user:
        if db_user.days_left == 0:
            return { "error": 'License is over, top up your account' }
    else:
        return { "error": f'User: {email} - is not exist' }
    
    xray = await handler.HandlerBuilder.get_instanse()
    return { "config": xray.client_config, "last_update":  xray.last_update}
