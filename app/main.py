from fastapi import FastAPI
from app.core.database import init_db
from app.api.diary import router as diary_router
import asyncio
from sqlalchemy.exc import OperationalError

app = FastAPI(title="Diary API Test Task")
app.include_router(diary_router, prefix="/v1")

MAX_RETRIES = 30
RETRY_DELAY = 2


@app.on_event("startup")
async def on_startup():
    print("Starting database initialization...")

    for attempt in range(MAX_RETRIES):
        try:
            await init_db()
            print("Database initialized successfully.")

        except OperationalError as e:
            # Ловим ошибку, если БД не готова
            print(
                f"Attempt {attempt + 1}/{MAX_RETRIES}: Database connection failed ({e.__class__.__name__}). Retrying in {RETRY_DELAY}s..."
            )
            await asyncio.sleep(RETRY_DELAY)

        except Exception as e:
            # Если возникла другая ошибка
            print(
                f"Attempt {attempt + 1}/{MAX_RETRIES}: An unexpected error occurred: {e.__class__.__name__}: {e}. Retrying in {RETRY_DELAY}s..."
            )
            await asyncio.sleep(RETRY_DELAY)
    print(
        f"FATAL: Could not connect to database after {MAX_RETRIES} attempts. Application shutting down."
    )
    raise RuntimeError("Failed to connect to the database upon startup.")
