from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped

from app.config import get_db_url
from app.db.annotations import created_at, updated_at


DATABASE_URL = get_db_url()
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]