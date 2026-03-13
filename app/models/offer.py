from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("requests.id"))
    offered_by = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="pending")
