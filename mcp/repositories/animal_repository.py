from database import get_db


class AnimalRepository:

    async def get_by_id(self, animal_id: str):

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
                return None

            return dict(row)
