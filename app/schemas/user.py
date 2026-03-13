from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    pincode: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    pincode: str
    trust_score: float

    model_config = {"from_attributes": True}
