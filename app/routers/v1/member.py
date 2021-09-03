from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/api/v1/members",
    tags=["Manage Members"],
    responses={404: {"description": "Not found"}},
)