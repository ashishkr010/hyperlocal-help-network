from pydantic import BaseModel, field_validator
from typing import Optional


class ReviewCreate(BaseModel):
    reviewed_user: int
    rating: float
    comment: Optional[str] = None
    request_id: int

    @field_validator("rating")
    @classmethod
    def rating_in_range(cls, v):
        if not 1 <= v <= 5:
            raise ValueError("rating must be between 1 and 5")
        return v


class ReviewResponse(BaseModel):
    id: int
    reviewed_user: int
    rating: float
    comment: Optional[str]
    request_id: int

    model_config = {"from_attributes": True}
