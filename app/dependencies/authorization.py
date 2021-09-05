from fastapi import Depends, HTTPException
from app.db.repository.auth import AuthHandler
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.repository.user import get_user_role
auth_handler = AuthHandler()


async def admin(db: Session = Depends(get_db), email: str = Depends(auth_handler.auth_wrapper)):
    role = get_user_role(db=db, email=email)

    if role == "u":
        raise HTTPException(status_code=401, detail="User unauthorized. admin only")
    elif role == "a":
        pass
    else:
        raise HTTPException(status_code=401, detail="Unknown user role. contact the developer")

async def user(db: Session = Depends(get_db), email: str = Depends(auth_handler.auth_wrapper)):
    role = get_user_role(db=db, email=email)

    if role == "a":
        raise HTTPException(status_code=401, detail="Admin unauthorized. user only")
    elif role == "u":
        pass
    else:
        raise HTTPException(status_code=401, detail="Unknown user role. contact the developer")
