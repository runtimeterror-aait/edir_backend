from sqlalchemy.orm import Session
from app.schemas import Event, EventCreate, EventUpdate
from app.db.models import Event 
from app.db.repository.user import get_user_by_email
from app.db.repository.edir import get_edir_by_id