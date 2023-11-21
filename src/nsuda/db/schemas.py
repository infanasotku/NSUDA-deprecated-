from pydantic import BaseModel

class UserBase(BaseModel):
   class Config:
        from_attributes = True

class User(UserBase):
    id: int
    email: str
    days_left: int

class UserCreate(BaseModel):
    email: str
    days_left: int
 

