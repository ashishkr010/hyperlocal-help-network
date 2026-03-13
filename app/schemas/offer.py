from pydantic import BaseModel


class OfferCreate(BaseModel):
    request_id: int


class OfferResponse(BaseModel):
    id: int
    request_id: int
    offered_by: int
    status: str

    model_config = {"from_attributes": True}
