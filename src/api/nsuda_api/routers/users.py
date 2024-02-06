from fastapi.routing import APIRouter

users = APIRouter(prefix="/users")

@users.get("/")
async def index():
    return "Hello world!"