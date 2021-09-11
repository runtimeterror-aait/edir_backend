from sqlalchemy.orm import Session
from app.schemas import Payment, PaymentCreate, PaymentUpdate
from app.db.models import Member, Payment
from app.db.repository.member import get_member_by_id

def get_all_members_payment(db: Session, edir_id: int, user_id: int, skip: int = 0, limit: int = 10):
    db_payments = db.query(Payment).filter(
        Payment.member_id == user_id).offset(skip).limit(limit).all()
    return db_payments

def get_all_user_payment(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    edir = db.query(Member).filter(Member.user_id == user_id).first()
    member_id = edir.id;
    db_payments = db.query(Payment).filter(
        Payment.member_id == member_id).offset(skip).limit(limit).all()
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
