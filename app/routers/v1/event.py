from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler
from app.schemas import EventCreate, EventUpdate, Event as EventSchema
from app.db.database import get_db
from app.db.repository.event import get_events, get_event_by_id, create_event, update_event, delete_event
from app.db.repository.edir import get_edir_by_id
auth_handler = AuthHandler()

router = APIRouter(
    prefix="/api/v1/events",
    tags=["Manage Events"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{edir_id}")
def get_all_events(edir_id: int, skip: int = 0, limit: int = 10,  email=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    if get_edir_by_id(db=db, id=edir_id) is None:     
        raise HTTPException(status_code=404, detail="Edir doesn't exist")   
    else:
        events = get_events(db=db, edir_id=edir_id, skip=skip, limit=limit)
        return events

@router.get("/{edir_id}/{event_id}")
def get_one_event(edir_id: int, event_id: int, db: Session = Depends(get_db), email=Depends(auth_handler.auth_wrapper)):
    event = get_event_by_id(db=db, id=event_id)
    return event

@router.post("/")
def create_new_event(event: EventCreate, email=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    if get_edir_by_id(db=db, id=event.edir_id) is None:     
        raise HTTPException(status_code=404, detail="Edir doesn't exist")   
    else:
        return create_event(db=db, email=email, event=event)


@router.put("/{event_id}")
def update_existing_event(event_id: int, event: EventUpdate, email=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
        return update_event(db=db, event_id=event_id, event=event)

@router.delete("/{event_id}")
def delete_existing_event(event_id: int, email=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    return delete_event(db=db, event_id=event_id)