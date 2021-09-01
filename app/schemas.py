from pydantic import BaseModel

from typing import List, Optional

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