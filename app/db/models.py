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