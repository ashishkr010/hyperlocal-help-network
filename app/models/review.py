from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    reviewed_user = Column(Integer, ForeignKey("users.id"))
    rating = Column(Float, nullable=False)
    comment = Column(String)
    request_id = Column(Integer, ForeignKey("requests.id"))
