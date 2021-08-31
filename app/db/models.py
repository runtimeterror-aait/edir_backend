import datetime as _dt
from sqlalchemy import Column,Integer,String,DateTime, Float,Text
from sqlalchemy import relationship, backerf
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