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

