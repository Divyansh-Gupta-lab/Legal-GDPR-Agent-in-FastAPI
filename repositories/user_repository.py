"""User repository"""
import uuid
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from infrastructure.database.dependency import get_db
from infrastructure.database.models.user_model import User
from schemas.auth_schema import SignUpRequest

class UserRepository:
    """User repository"""
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_by_id(self, user_id: uuid.UUID) -> User | None:
        """Get a user by id"""
        return await self.db.get(User, user_id)
    
    async def get_by_username(self, username: str) -> User | None:
        """Get a user by username"""
        return await self.db.scalar(select(User).where(User.username == username))

    async def create(self, create_user: SignUpRequest) -> User:
        """Create a user"""
        user = User(
            username=create_user.username
        )
        await self.db.add(user)
        return user

def get_user_repo(db: AsyncSession= Depends(get_db)) -> UserRepository:
    """Get a user repository"""
    return UserRepository(db)
