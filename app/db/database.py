from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import false

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://liyu:root@localhost:3306/edir"


# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def  get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
def create_database():
    return Base.metadata.create_all(bind=engine)

    
    