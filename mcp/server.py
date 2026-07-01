from mcp.server.fastmcp import FastMCP
from database import get_db
from tools.get_animal import get_animal

mcp = FastMCP("Animal Rescure Database")


@mcp.tool()
async def get_animal(animal_id: str):
    """
    Get the Animal detials when animal id is passed
    """
    return await get_animal(animal_id)


if __name__ == "__main__":
    mcp.run(transport="stdio")
