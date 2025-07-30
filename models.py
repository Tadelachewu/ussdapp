from sqlalchemy import create_engine, Column, Integer, String, Float, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String, unique=True, nullable=False)

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String, nullable=False)
    amount = Column(Integer)
    status = Column(String)
    score = Column(Float)
    created_at = Column(TIMESTAMP, server_default=func.now())
