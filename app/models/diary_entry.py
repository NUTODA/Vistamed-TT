from sqlalchemy import Column, Integer, String, Boolean, DateTime, Index
from sqlalchemy.sql import func
from app.core.database import Base


class DiaryEntry(Base):
    __tablename__ = "diary_entries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=False)
    content = Column(String(4096), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    is_completed = Column(Boolean, default=False, index=True)

    __table_args__ = (Index("idx_completed", is_completed),)
