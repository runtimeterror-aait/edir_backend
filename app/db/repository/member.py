from sqlalchemy.orm import Session
from app.schemas import Member as MemberSchema, MemberCreate, MemberUpdate
from app.db.models import Member 
from app.db.repository.edir import get_edir_by_id

