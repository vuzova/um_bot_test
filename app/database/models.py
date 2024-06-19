from sqlalchemy import Integer, BigInteger, String, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    name: Mapped[str] = mapped_column(String(25))
    surname: Mapped[str] = mapped_column(String(25))

    __table_args__ = (
        UniqueConstraint('tg_id'),
    )

class Subject(Base):
    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(25))

class Result(Base):
    __tablename__ = 'results'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    subject: Mapped[int] = mapped_column(ForeignKey('subjects.id'))
    score: Mapped[int] = mapped_column(CheckConstraint("score >= 0 AND score <= 100"))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)