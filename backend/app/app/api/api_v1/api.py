from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, students

api_router = APIRouter()

# Alive endpoint
@api_router.get("/alive")
async def alive():
    return {"alive": True}

api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(students.router, prefix="/students", tags=["students"])