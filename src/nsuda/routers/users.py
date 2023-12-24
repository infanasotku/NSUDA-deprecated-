from fastapi import Depends, APIRouter, WebSocket
from sqlalchemy.orm import Session
from hashlib import sha256

from nsuda.db import crud


router = APIRouter()


from nsuda.xray import handler

@router.get("/get_config")
async def get_config(email: str, password: str,  db: Session = Depends(crud.get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user and db_user.password_hash == sha256(password.encode('utf-8 ')).hexdigest():
        if db_user.days_left == 0:
            return { "error": 'License is over, top up your account' }
    else:
        return { "error": f'Incorrect user or password' }
    
    xray = await handler.HandlerBuilder.get_instanse()
    return { "config": xray.client_config, "last_update":  xray.last_update}



class DaysHandler:
    _handler: int = None
    
    @staticmethod
    def update_days():
        '''Updates days of user subscription. 
        '''
        if not DaysHandler._handler:
            DaysHandler._handler = 1 # Initing flag
            return
        db_handler = crud.get_db()
        db: Session = next(db_handler)

        users = crud.get_all_users(db)

        for user in users:
            if user.days_left > 0:
                user.days_left -= 1
                crud.update_user(db, user=user)
                
        next(db_handler)