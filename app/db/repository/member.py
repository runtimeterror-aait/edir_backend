from sqlalchemy.orm import Session
from app.schemas import Member as MemberSchema, MemberCreate, MemberUpdate
from app.db.models import Member 
from app.db.repository.edir import get_edir_by_id

def get_all_members(db: Session, edir_id: int, skip: int = 0, limit:int = 0):
    db_edir = get_edir_by_id(db=db, id=edir_id)
    return db_edir.members

def get_member_by_id(db:Session, edir_id: int, user_id: int):
    db_member = db.query(Member).filter(Member.edir_id == edir_id, Member.user_id == user_id).first()
    return db_member

def check_member_exist(db:Session, edir_id: int, user_id: int):
    db_member = get_member_by_id(db=db, edir_id=edir_id, user_id=user_id)
    if db_member is None:
        return False
    return True