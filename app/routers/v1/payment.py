from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler
from app.db.repository.payment import get_all_members_payment
from app.db.repository.member import get_member_by_id
from app.db.repository.edir import get_edir_by_id
from app.db.database import get_db

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/api/v1/payments",
    tags=["Manage Payments"],
    responses={404: {"description": "Not found"}},
)


#get payments by a member
@router.get("/{edir_id}/{member_id}}")
def get_all_payments(edir_id: int, member_id: int, skip: int = 0, limit: int = 10, db:Session = Depends(get_db), email=Depends(auth_handler.auth_wrapper)):
    #if member doesn't exist
    if get_member_by_id(db=db, id=user_id):
        raise HTTPException(status_code=404, detail="Oops, User doesn't exist in this edir")
    
    #if edir doesn't exist
    if get_edir_by_id(db=db, id=edir_id):
        raise HTTPException(status_code=404, detail="Oops, Edir doesn't exist")
    payments = get_all_members_payment(db=db, edir_id=edir_id, user_id=user_id, skip=skip, limit=limit)

    #if there's no payment
    if payments is None:
        raise HTTPException(status_code=404, detail="No payment exist")
    return payments