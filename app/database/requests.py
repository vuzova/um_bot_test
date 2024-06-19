from sqlalchemy.orm import joinedload

from app.database.models import async_session
from app.database.models import User, Subject, Result
from sqlalchemy import select

async def get_user(tg_id):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))

async def get_subjects():
    async with async_session() as session:
        return await session.scalars(select(Subject))

async def get_subject(id):
    async with async_session() as session:
        return await session.scalar(select(Subject).where(Subject.id == id))

async def get_user_scores(tg_id):
    async with async_session() as session:
        user = await get_user(tg_id)
        return await session.scalars(select(Result).where(Result.user == user.id))

async def get_user_scores_current_sbj(user_id, sbj_id, session=None):
    if session is None:  # Если сессия не передана, используем новую
        async with async_session() as session:
            return await session.scalar(select(Result).where(Result.user == user_id, Result.subject == sbj_id))
    else:  # Иначе используем переданную сессию
        return await session.scalar(select(Result).where(Result.user == user_id, Result.subject == sbj_id))


async def set_user(tg_id, name, surname):
    async with async_session() as session:
        if not await get_user(tg_id):
            session.add(User(tg_id=tg_id, name=name, surname=surname))
            await session.commit()

async def set_score(tg_id, subject_id, score):
    async with async_session() as session:
        user = await get_user(tg_id)
        if not await get_user_scores_current_sbj(user.id, subject_id):
            session.add(Result(user=user.id, subject=subject_id, score=score))
            await session.commit()
            return True
        else:
            result = await get_user_scores_current_sbj(user.id, subject_id,  session=session)
            result.score = score
            session.merge(result)
            await session.commit()
            return False
