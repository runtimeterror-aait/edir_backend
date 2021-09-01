import datetime as _dt
from sqlalchemy import Column,Integer,String,DateTime, Float,Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ForeignKey
from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255),unique=True,index=True,nullable=False)
    phone = Column(String(255), unique=True,index=True, nullable=False)
    password = Column(Text(4294000000), nullable=False)
    role = Column(String(255))  

    edirs = relationship("Edir", back_populates = "owner")
    joined = relationship("Edir", secondary = "members")

class Edir(Base):
    __tablename__ = "edirs"
    id = Column(Integer, primary_key = True, index=True)
    payment_frequency = Column(String(255))
    initial_deposit = Column(Float)
    username = Column(String(255), unique=True,index=True)
    owner_id = Column(Integer, ForeignKey('Users.id'))

    owner = relationship("User", back_populates="edirs")
    events = relationship("Event", back_populates="edir")
    members = relationship("User",back_populates="members")

class Event(Base):
    __tablename__= "events"
    id = Column(Integer ,primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    event_date = Column(String(255))
    edir_id = Column(Integer, ForeignKey("edirs.id"))

    edir = relationship("Edir", back_populates="events")

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    edir_id = Column(Integer, ForeignKey('edirs.id'), index=True)
    status = Column(String(255))
    
    # owner
    user = relationship("User", backref=backref("member", cascade="all, delete-orphan"))
    edir = relationship("Edir", backref=backref("member", cascade="all, delete-orphan"))
    payments = relationship("Payment", back_populates='member')








    