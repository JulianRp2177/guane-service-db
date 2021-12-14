from typing import Optional
from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    password: str
    document: str
    email: Optional[str]
    phone: Optional[str]

class UpdateUser(BaseModel):
    username: Optional[str]
    password: Optional[str]
    document: Optional[str]
    email: Optional[str]
    phone: Optional[str]

class PayloadUser(BaseModel):
    username: Optional[str]
    password: Optional[str]
    document: Optional[str]
    email: Optional[str]
    phone: Optional[str]
class UserInDB(UpdateUser):
    id: int

    class Config:
        orm_mode = True
