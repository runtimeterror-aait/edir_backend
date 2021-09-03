from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler
auth_handler = AuthHandler()


router = APIRouter(
    prefix="/api/v1/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)