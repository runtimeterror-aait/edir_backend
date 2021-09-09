from sqlalchemy.orm import Session, joinedload
from app.schemas import Member as MemberSchema, MemberCreate, MemberUpdate
from app.db.models import Member 
from app.db.repository.edir import get_edir_by_id

def get_all_members(db: Session, edir_id: int, skip: int = 0, limit:int = 0):
    # db_edir = db.query(Edir).filter(Edir.id == edir_id).options(joinedload(Edir.members)).all()
    db_edir = db.query(Member).filter(Member.edir_id == edir_id).options(joinedload(Member.user)).all()
    print(db_edir)  
    return db_edir

def get_member_by_id(db:Session, edir_id: int, user_id: int):
    db_member = db.query(Member).filter(Member.edir_id == edir_id, Member.user_id == user_id).first()
    return db_member

def check_member_exist(db:Session, edir_id: int, user_id: int):
    db_member = get_member_by_id(db=db, edir_id=edir_id, user_id=user_id)
    if db_member is None:
        return False
    return True
def create_member(db:Session, member: MemberCreate):
    db_member = Member(user_id=member.edir_id, edir_id=member.edir_id, status="pending")
    db.add(db_member)
    db.commit()
    return db_member

def update_member(db:Session, member_id: int, member: MemberUpdate):
    db_member = db.query(Member).filter(Member.id == member_id).first()
    db_member.status = member.status
    db.commit()
    db.refresh(db_member)
    return db_member

def delete_member(db: Session, member_id: int):
    db.query(Member).filter(Member.id == member_id).delete()
    db.commit()

