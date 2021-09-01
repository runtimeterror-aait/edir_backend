from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserUpdate
from passlib.context import CryptContext
from app.db.models import User