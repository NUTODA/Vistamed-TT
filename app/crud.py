from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.models.diary_entry import DiaryEntry
from app.schemas.diary import DiaryEntryCreate, DiaryEntryUpdate


class DiaryCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_entry(self, entry_data: DiaryEntryCreate) -> DiaryEntry:
        new_entry = DiaryEntry(**entry_data.model_dump())
        self.session.add(new_entry)
        await self.session.commit()
        await self.session.refresh(new_entry)
        return new_entry

    async def get_entry(self, entry_id: int) -> DiaryEntry | None:
        result = await self.session.execute(
            select(DiaryEntry).where(DiaryEntry.id == entry_id)
        )
        return result.scalar_one_or_none()

    async def get_entries(self, skip: int = 0, limit: int = 100) -> list[DiaryEntry]:
        stmt = select(DiaryEntry).offset(skip).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def update_entry(
        self, entry_id: int, entry_data: DiaryEntryUpdate
    ) -> DiaryEntry | None:
        values = entry_data.model_dump(exclude_unset=True)

        stmt = update(DiaryEntry).where(DiaryEntry.id == entry_id).values(**values)
        await self.session.execute(stmt)
        await self.session.commit()
        return await self.get_entry(entry_id)

    async def delete_entry(self, entry_id: int) -> bool:
        stmt = delete(DiaryEntry).where(DiaryEntry.id == entry_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0

    async def mark_completed(
        self, entry_id: int, is_completed: bool = True
    ) -> DiaryEntry | None:
        stmt = (
            update(DiaryEntry)
            .where(DiaryEntry.id == entry_id)
            .values(is_completed=is_completed)
        )
        await self.session.execute(stmt)
        await self.session.commit()
        return await self.get_entry(entry_id)
