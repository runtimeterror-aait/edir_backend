from app.dependencies.authorization import admin
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler
from app.db.repository.payment import get_all_members_payment, create_payment, get_all_user_payment, update_payment, delete_payment
from app.db.repository.member import get_member_by_id, get_member_by_member_id
from app.db.repository.edir import get_edir_by_id
from app.db.database import get_db
from app.schemas import Payment, PaymentCreate, PaymentUpdate

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/api/v1/payments",
    tags=["Manage Payments"],
    responses={404: {"description": "Not found"}},
)


# get payments by a member
@router.get("/user/{user_id}")
def get_all_payments_by_user_id(user_id: int, skip: int = 0, limit: int = 10, db:Session = Depends(get_db), email=Depends(auth_handler.auth_wrapper)):
    
    payments = get_all_user_payment(db=db, user_id=user_id, skip=skip, limit=limit)

    #if there's no payment
    if payments is None:
        raise HTTPException(status_code=404, detail="No payment exist")
    return payments

@router.get("user/{member_id}")
def get_all_payments(edir_id: int, member_id: int, skip: int = 0, limit: int = 10, db:Session = Depends(get_db), email=Depends(auth_handler.auth_wrapper)):
    #if member doesn't exist
    if not get_member_by_member_id(db=db, id=member_id):
        raise HTTPException(status_code=404, detail="Oops, User doesn't exist in this edir")
    
    #if edir doesn't exist
    if not get_edir_by_id(db=db, id=edir_id):
        raise HTTPException(status_code=404, detail="Oops, Edir doesn't exist")
    payments = get_all_members_payment(db=db, edir_id=edir_id, user_id=member_id, skip=skip, limit=limit)

    #if there's no payment
    if payments is None:
        raise HTTPException(status_code=404, detail="No payment exist")
    return payments

#add payment
@router.post("/")
def add_new_payment(payment: PaymentCreate, email=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db),check_admin = Depends(admin)):
    if not get_member_by_member_id(db=db, id=payment.member_id):
        raise HTTPException(status_code=404, detail="Oops, User doesn't exist in this edir")
    return create_payment(db=db, payment=payment)

#update payment
@router.put("/{payment_id}")
def update_member_payment(payment_id: int, payment: PaymentUpdate, email=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db), check_admin = Depends(admin)):
    return update_payment(db=db, payment_id=payment_id, payment=payment)
    
#remove payment
@router.delete("/{payment_id}")
def remove_member_payment(payment_id: int, email=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db), check_admin = Depends(admin)):
    return delete_payment(db=db, payment_id=payment_id)