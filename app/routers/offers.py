from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.offer import Offer
from app.models.user import User
from app.schemas.offer import OfferCreate, OfferResponse
from app.services.auth import get_current_user

router = APIRouter(prefix="/offers", tags=["offers"])


@router.post("/", response_model=OfferResponse)
async def make_offer(data: OfferCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    offer = Offer(request_id=data.request_id, offered_by=current_user.id)
    db.add(offer)
    await db.commit()
    await db.refresh(offer)
    return offer


@router.patch("/{offer_id}/accept", response_model=OfferResponse)
async def accept_offer(offer_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Offer).where(Offer.id == offer_id))
    offer = result.scalar_one_or_none()
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    if offer.status != "pending":
        raise HTTPException(status_code=400, detail=f"Cannot accept an offer with status '{offer.status}'")
    offer.status = "accepted"
    await db.commit()
    await db.refresh(offer)
    return offer


@router.patch("/{offer_id}/cancel", response_model=OfferResponse)
async def cancel_offer(offer_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Offer).where(Offer.id == offer_id))
    offer = result.scalar_one_or_none()
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    if offer.status != "pending":
        raise HTTPException(status_code=400, detail=f"Cannot cancel an offer with status '{offer.status}'")
    offer.status = "cancelled"
    await db.commit()
    await db.refresh(offer)
    return offer
