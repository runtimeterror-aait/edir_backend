from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler
from app.schemas import UserCreate, AuthDetails, User as UserSchema
from app.db.database import get_db
from app.db.repository.user import create_user, check_user_exist , check_encrypted_password, get_user_by_email

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)