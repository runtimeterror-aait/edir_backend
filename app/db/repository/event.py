from sqlalchemy.orm import Session
from app.schemas import Event, EventCreate, EventUpdate
from app.db.models import Event 
from app.db.repository.user import get_user_by_email
from app.db.repository.edir import get_edir_by_id

def get_events(db: Session, edir_id: int, skip: int = 0, limit: int = 10):
    return db.query(Event).filter(Event.edir_id == edir_id).offset(skip).limit(limit).all()

def get_event_by_id(db: Session, id: int):
    return db.query(Event).filter(Event.id == id).first()

def create_event(db: Session, email: str, event: EventCreate):
    db_event = Event(title=event.title, description=event.description, event_date=event.event_date, edir_id=event.edir_id)
    db.add(db_event)
    db.commit()
    return db_event

def update_event(db: Session, event_id: int, event: EventUpdate):

    db_event = get_event_by_id(db=db, id=event_id)
    db_event.title = event.title
    db_event.description = event.description
    db_event.event_date = event.event_date
    db.commit()
    db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db.query(Event).filter(Event.id == event_id).delete()
    db.commit()
