from mcp.server.fastmcp import FastMCP
from tools.get_animal import register
from services.animal_service import AnimalService
from repositories.animal_repository import AnimalRepository

mcp = FastMCP("Animal Rescure Database")

animal_repository = AnimalRepository()
animal_service = AnimalService(animal_repository)

register(mcp=mcp, animal_service=animal_service)


if __name__ == "__main__":
    mcp.run(transport="stdio")
