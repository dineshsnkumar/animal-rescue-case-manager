from repositories.animal_repository import AnimalRepository


class AnimalService:

    def __init__(self, repository: AnimalRepository):
        self.repository = repository

    async def get_animal(self, animal_id: str):
        animal = await self.repository.get_by_id(animal_id=animal_id)

        if animal is None:
            return {"found": False}

        return animal
