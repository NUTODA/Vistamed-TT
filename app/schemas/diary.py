from pydantic import BaseModel
from datetime import datetime


# Схема для создания/обновления (входящие данные)
class DiaryEntryBase(BaseModel):
    title: str
    content: str | None = None


class DiaryEntryCreate(DiaryEntryBase):
    pass


class DiaryEntryUpdate(DiaryEntryBase):
    pass


# Схема для чтения (исходящие данные)
class DiaryEntryRead(DiaryEntryBase):
    id: int
    created_at: datetime
    is_completed: bool

    class Config:
        from_attributes = True
