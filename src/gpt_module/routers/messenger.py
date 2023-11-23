from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def greet():
    return "Greetings from GPT model!"