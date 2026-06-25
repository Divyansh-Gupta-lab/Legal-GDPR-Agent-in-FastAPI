"""Session for the database"""
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=20,
    pool_recycle=3600,
    pool_timeout=30,
    max_overflow=10,
    echo=False
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=True,
    expire_on_commit=False
)
