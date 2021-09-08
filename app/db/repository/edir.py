from sqlalchemy.orm import Session
from app.schemas import Edir, EdirCreate, EdirUpdate
from app.db.models import Edir 
from app.db.repository.user import get_user_by_email

def get_edirs(db: Session, email: str, skip: int = 0, limit: int = 10):
    db_user = get_user_by_email(db, email)
    return db.query(Edir).filter(Edir.owner_id == db_user.id).offset(skip).limit(limit).first()

def get_edir_by_id(db: Session, id: int):
    return db.query(Edir).filter(Edir.id == id).first()

def get_edir_by_username(db:Session, username: str):
    return db.query(Edir).filter(Edir.username == username).first()

def create_edir(db: Session, email: str, edir: EdirCreate):
    db_user = get_user_by_email(db, email)
    db_edir = Edir(name=edir.name, payment_frequency=edir.payment_frequency, initial_deposit=edir.initial_deposit, username=edir.username, owner_id=db_user.id)
    db.add(db_edir)
    db.commit()
    db.refresh(db_user)
    return db_edir

def update_edir(db: Session, edir_id: int, edir: EdirUpdate):
    db_edir = get_edir_by_id(db=db, id=edir_id)
    db_edir.name = edir.name
    db_edir.payment_frequency = edir.payment_frequency
    db_edir.initial_deposit = edir.initial_deposit
    db.commit()
    db.refresh(db_edir)
    return db_edir

def delete_edir(db: Session, edir_id: int):
    db.query(Edir).filter(Edir.id == edir_id).delete()
    db.commit()