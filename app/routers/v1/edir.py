from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler
from app.schemas import EdirCreate, EdirUpdate, Edir as EdirSchema
from app.db.database import get_db
from app.db.repository.edir import get_edirs, get_edir_by_id, get_edir_by_username, create_edir, update_edir, delete_edir

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/v1/edirs",
    tags=["Manage Edir"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_all_edirs(skip: int = 0, limit: int = 10, email=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    posts = get_edirs(db=db, email=email, skip=skip, limit=limit)
    return posts

@router.get("/{edir_id}")
def get_one_edir(edir_id: int, db: Session = Depends(get_db), email=Depends(auth_handler.auth_wrapper)):
    edir = get_edir_by_id(db=db, id=edir_id)
    return edir
