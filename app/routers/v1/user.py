from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler
from app.schemas import UserUpdate
from app.db.database import get_db
from app.db.repository.user import get_user_by_email, update_user
auth_handler = AuthHandler()


router = APIRouter(
    prefix="/api/v1/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

#get user
@router.get("/")
def auth_user(email=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    return get_user_by_email(db=db, email=email)

#update user
@router.put("/")
def auth_user_update(user: UserUpdate, email: Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    return update_user(db=db, email=email, user=user)