from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
import uuid

from infrastructure.database.base import Base
from infrastructure.database.models.notes_model import Note

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )
    
    password_hash: Mapped[str] = mapped_column(
        String(200),
    )
    
    notes: Mapped[list["Note"]] = relationship(
        "Note",
        back_populates="user",
        lazy="selectin"
    )
