from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/api/v1/payments",
    tags=["Manage Payments"],
    responses={404: {"description": "Not found"}},
)