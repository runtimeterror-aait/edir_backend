from sqlalchemy.sql.functions import user
from pydantic import BaseModel

from typing import List, Optional

from sqlalchemy.sql.sqltypes import Enum

# event defnation

class _EventBase(BaseModel):
    title: str
    description: str
    event_date: str

class EventCreate(_EventBase):
    edir_id: int


class EventUpdate(_EventBase):
    pass

class Event(_EventBase):
    id: int
    edir_id: int

    class Config:
        orm_mode = True

#edir defnition

class _EdirBase(BaseModel):
    name:str
    payment_frequency: str
    initial_deposit:int
    username:   str

class EdirCreate(_EdirBase):
    pass

class Edir(_EdirBase):
    id: int
    owner_id: int
    events: List[Event] = []
    
    class Config:
        orm_mode = True
        
class EdirUpdate(BaseModel):
    name: str
    payment_frequency: str
    initial_deposite: int

class RoleChoice(str, Enum):
    u = "u"
    a = "a"

# user defnition 
class _UserBase(BaseModel):
    full_name: str
    email: str
    phone: str
    role: RoleChoice

class UserUpdate(BaseModel):
    full_name: str
    email: str
    phone: str
    password: str

class UserCreate(_UserBase):
    password:str

class User(_UserBase):
    id: int
    edirs: List[Edir] = []
    joined: List[Edir] =[]

    class config:
        orm_mode = True

class _PaymentBase(BaseModel):
    note: str
    payment:str
    member_id: int
    payment_date:str

class Payment(_PaymentBase):
    id: int

    class config:
        orm_mode = True
class PaymentCreate(_PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    note:str
    payment:str
    payment_date:str
    
# member defnition

class _MemberBase(BaseModel):
    user_id:str
    edir_id:str
    status:str

class MemberCreate(_MemberBase):
    pass

class Member(_MemberBase):
    id: int
    user: List[User] = []
    edir: List[Edir] = []
    payments: List[Payment] = []

class MemberUpdate(BaseModel):
    status:str

class Token(BaseModel):
    accessToken:str
    tokenType:str

class TokenData(BaseModel):
    email: Optional[str] = None
    userType: Optional[str] = None

class AuthDetails(BaseModel):
    email: str
    password: str