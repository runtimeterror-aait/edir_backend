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
