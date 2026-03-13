from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.request import HelpRequest
from app.models.user import User
from app.schemas.request import HelpRequestCreate, HelpRequestResponse
from typing import List, Optional

router = APIRouter(prefix="/requests", tags=["requests"])


@router.post("/", response_model=HelpRequestResponse)
async def create_request(data: HelpRequestCreate, db: AsyncSession = Depends(get_db)):
    request = HelpRequest(**data.model_dump())
    db.add(request)
    await db.commit()
    await db.refresh(request)
    return request


@router.get("/", response_model=List[HelpRequestResponse])
async def list_requests(pincode: Optional[str] = None, db: AsyncSession = Depends(get_db)):
    query = select(HelpRequest)
    if pincode:
        query = query.join(User, HelpRequest.user_id == User.id).where(User.pincode == pincode)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/{request_id}", response_model=HelpRequestResponse)
async def get_request(request_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(HelpRequest).where(HelpRequest.id == request_id))
    request = result.scalar_one_or_none()
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    return request


@router.patch("/{request_id}/status", response_model=HelpRequestResponse)
async def update_status(request_id: int, status: str, db: AsyncSession = Depends(get_db)):
    valid = ["open", "in_progress", "closed"]
    if status not in valid:
        raise HTTPException(status_code=400, detail=f"status must be one of {valid}")
    result = await db.execute(select(HelpRequest).where(HelpRequest.id == request_id))
    request = result.scalar_one_or_none()
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    request.status = status
    await db.commit()
    await db.refresh(request)
    return request
