from fastapi.routing import APIRouter

auth = APIRouter()


@auth.get('/')
async def index():
    pass