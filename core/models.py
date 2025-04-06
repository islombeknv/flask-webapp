from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from datetime import datetime

# Define the base class for declarative models
class Base(DeclarativeBase):
    pass

class Event(Base):
    __tablename__ = 'Event'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    description: Mapped[str|None]

    def __repr__(self) -> str:
        return f"Event(task_id={self.id!r}, title={self.name!r})"

