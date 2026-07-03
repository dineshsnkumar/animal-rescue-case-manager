from database import get_db
from services.animal_service import AnimalService
from repositories.animal_repository import AnimalRepository


def register(mcp, animal_service: AnimalService):
    @mcp.tool()
    async def get_animal(animal_id: str):
        """
        Given animal_id; return infomation about the animal
        """
        return await animal_service.get_animal(animal_id)
