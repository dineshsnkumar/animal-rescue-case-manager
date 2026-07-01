from pathlib import Path
from contextlib import asynccontextmanager
import aiosqlite

DB_PATH = Path(__file__).parent.parent / "data" / "animal_rescue.db"


@asynccontextmanager
async def get_db():
    db = await aiosqlite.connect(DB_PATH)
    db.row_factory = aiosqlite.Row

    try:
        yield db
    finally:
        await db.close()
