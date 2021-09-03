from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler
from app.schemas import EventCreate, EventUpdate, Event as EventSchema
from app.db.database import get_db
from app.db.repository.event import get_events, get_event_by_id, create_event, update_event, delete_event
from app.db.repository.edir import get_edir_by_id
auth_handler = AuthHandler()

router = APIRouter(
    prefix="/api/v1/events",
    tags=["Manage Events"],
    responses={404: {"description": "Not found"}},
)