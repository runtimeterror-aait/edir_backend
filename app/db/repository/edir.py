from sqlalchemy.orm import Session
from app.schemas import Edir, EdirCreate, EdirUpdate
from app.db.models import Edir 
from app.db.repository.user import get_user_by_email
