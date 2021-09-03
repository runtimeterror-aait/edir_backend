from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserUpdate
from passlib.context import CryptContext
from app.db.models import User

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
)

def encrypt_password(password):
    return pwd_context.encrypt(password)

def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

def check_user_exist(db: Session, email: str, password: str):
    user_exist = db.query(User).filter(User.email == email).first()
    if user_exist is not None:
        if check_encrypted_password(password, user_exist.password):
            return True
        else: 
            return False
    else:
        return False

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_users_role(db: Session, user_id: int):
    return get_user(db, user_id).role

def create_user(db: Session, user: UserCreate):
    hashed_password = encrypt_password(user.password)
    db_user = User(full_name=user.full_name, email=user.email, phone=user.phone, password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, email: str, user: UserUpdate):
    db_user = get_user_by_email(db=db, email=email)
    db_user.full_name = user.full_name
    db_user.email = user.email
    db_user.phone = user.phone
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, email: str):
    db.query(User).filter(User.email == email).delete()
    db.commit()