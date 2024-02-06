from fastapi.routing import APIRouter

users = APIRouter()

@users.get("/")
async def index():
    return "Hello world!"