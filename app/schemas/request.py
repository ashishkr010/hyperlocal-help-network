from pydantic import BaseModel
from typing import Optional, Literal


class HelpRequestCreate(BaseModel):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    urgency: Literal["low", "medium", "high", "emergency"] = "low"
    user_id: int


class HelpRequestResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    category: Optional[str]
    urgency: str
    status: str
    user_id: int

    model_config = {"from_attributes": True}
