from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    pincode = Column(String, nullable=False)
    trust_score = Column(Float, default=0.0)
