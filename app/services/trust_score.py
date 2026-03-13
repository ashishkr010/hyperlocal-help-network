from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.models.review import Review
from app.models.user import User


async def update_trust_score(user_id: int, db: AsyncSession):
    result = await db.execute(
        select(func.avg(Review.rating)).where(Review.reviewed_user == user_id)
    )
    avg = result.scalar()
    if avg is not None:
        user_result = await db.execute(select(User).where(User.id == user_id))
        user = user_result.scalar_one_or_none()
        if user:
            user.trust_score = round(float(avg), 2)
            await db.commit()
