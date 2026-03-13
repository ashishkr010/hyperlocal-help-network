from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class HelpRequest(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)
    urgency = Column(String, default="low")
    status = Column(String, default="open")
    user_id = Column(Integer, ForeignKey("users.id"))
