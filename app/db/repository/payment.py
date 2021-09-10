from sqlalchemy.orm import Session
from app.schemas import Payment, PaymentCreate, PaymentUpdate
from app.db.models import Payment
from app.db.repository.member import get_member_by_id

def get_all_members_payment(db: Session, edir_id: int, user_id: int, skip: int = 0, limit: int = 10):
    member = get_member_by_id(db=db, edir_id=edir_id, user_id=user_id)

    db_payments = db.query(Payment).filter(
        Payment.member_id == member.id).offset(skip).limit(limit).all()
    return db_payments


def create_payment(db: Session, payment: PaymentCreate):
    db_payment = Payment(note=payment.note, payment=payment.payment,
                         member_id=payment.member_id, payment_date=payment.payment_date)
    db.add(db_payment)
    db.commit()
    return db_payment


def update_payment(db: Session, payment_id: int, payment: PaymentUpdate):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    db_payment.note = payment.note
    db_payment.payment = payment.payment
    db_payment.payment_date = payment.payment_date
    db.commit()
    db.refresh(db_payment)
    return db_payment

def delete_payment(db: Session, payment_id):
    db.query(Payment).filter(Payment.id == payment_id).delete()
    db.commit()
