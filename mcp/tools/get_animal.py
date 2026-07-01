from database import get_db


async def get_animal(animal_id: str):

    async with get_db() as db:
        cursor = await db.execute(
            """
            SELECT *
            FROM intakes
            WHERE animal_id = ?
            """,
            (animal_id,),
        )

        row = await cursor.fetchone()

        if row is None:
            return {"found": False}

        return dict(row)
