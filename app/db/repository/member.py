from app.dependencies.authorization import user
from app.db.repository.user import get_user
from sqlalchemy.orm import Session, joinedload
from app.schemas import Member as MemberSchema, MemberCreate, MemberUpdate, User
from app.db.models import Member, Payment
from app.db.repository.edir import get_edir_by_id, get_edir_by_username

def get_all_members(db: Session, edir_id: int, skip: int = 0, limit:int = 0):
    db_edir = db.query(Member).filter(Member.edir_id == edir_id).options(joinedload(Member.user)).all()
    return db_edir

def get_member_by_id(db:Session, edir_id: int, user_id: int):
    db_member = db.query(Member).filter(Member.edir_id == edir_id, Member.user_id == user_id).first()
    return db_member

def get_member_by_edir_username(db:Session, username:str):
    edir = get_edir_by_username(db=db, username=username)
    db_member = db.query(Member).filter(Member.edir_id == edir.id).first()
    return db_member


def get_member_by_user_id(db:Session, user_id: int):
    db_member = db.query(Member).filter(Member.user_id == user_id).options(joinedload(Member.edir)).first()
    return db_member

def get_member_by_member_id(db:Session, id: int):
    db_member = db.query(Member).filter(Member.id == id).first()
    return db_member

def check_member_exist(db:Session, edir_id: int, user_id: int):
    db_member = get_member_by_id(db=db, edir_id=edir_id, user_id=user_id)
    if db_member is None:
        return False
    return True

def create_member(db:Session, member: MemberCreate):
    user = get_user(db=db, user_id=member.user_id);
    edir = get_edir_by_username(db=db, username=member.edir_username);
    db_member = Member(user_id=user.id, edir_id=edir.id, status="p")
    db.add(db_member)
    db.commit()
    return db_member

def update_member(db:Session, member_id: int):
    db_member = db.query(Member).filter(Member.id == member_id).first()
    db_member.status = "a"
    db.commit()
    db.refresh(db_member)
    return db_member

def delete_member(db: Session, member_id: int):
    member = db.query(Member).filter(Member.id == member_id)
    fetch = member.first()

    for payment in fetch.payments:
        db.query(Payment).filter(Payment.id == payment.id).delete()

    member.delete()
    
    db.commit()

