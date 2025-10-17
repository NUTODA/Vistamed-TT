from fastapi import APIRouter, Depends, HTTPException, status
from app.core.database import get_async_session
from app.schemas.diary import DiaryEntryCreate, DiaryEntryUpdate, DiaryEntryRead
from app.crud import DiaryCRUD
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/diary", tags=["Diary"])


async def get_crud(session: AsyncSession = Depends(get_async_session)):
    return DiaryCRUD(session)


# [POST] Создать запись
@router.post("/", response_model=DiaryEntryRead, status_code=status.HTTP_201_CREATED)
async def create_entry(data: DiaryEntryCreate, crud: DiaryCRUD = Depends(get_crud)):
    return await crud.create_entry(data)


# [GET] Получить список записей
@router.get("/", response_model=list[DiaryEntryRead])
async def list_entries(
    skip: int = 0, limit: int = 100, crud: DiaryCRUD = Depends(get_crud)
):
    return await crud.get_entries(skip=skip, limit=limit)


# [GET] Читать одну запись
@router.get("/{entry_id}", response_model=DiaryEntryRead)
async def read_entry(entry_id: int, crud: DiaryCRUD = Depends(get_crud)):
    entry = await crud.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry


# [PUT] Редактировать запись
@router.put("/{entry_id}", response_model=DiaryEntryRead)
async def update_entry(
    entry_id: int, data: DiaryEntryUpdate, crud: DiaryCRUD = Depends(get_crud)
):
    updated = await crud.update_entry(entry_id, data)
    if updated is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return updated


# [DELETE] Удалить запись
@router.delete("/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entry(entry_id: int, crud: DiaryCRUD = Depends(get_crud)):
    if not await crud.delete_entry(entry_id):
        raise HTTPException(status_code=404, detail="Entry not found")


# [PATCH] Пометить отработанной
@router.patch("/{entry_id}/complete", response_model=DiaryEntryRead)
async def complete_entry(entry_id: int, crud: DiaryCRUD = Depends(get_crud)):
    completed = await crud.mark_completed(entry_id, is_completed=True)
    if completed is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return completed
