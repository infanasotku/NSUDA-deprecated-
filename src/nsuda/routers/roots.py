from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

from pathlib import Path
srcPath = Path(__file__).parent.parent.parent.absolute()

templates = Jinja2Templates(directory=srcPath / "templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/NSUDA", response_class=HTMLResponse)
async def nsuda(request: Request):
    return templates.TemplateResponse("NSUDA.html", {"request": request})

@router.get("/downloads", response_class=HTMLResponse)
async def nsuda(request: Request):
    return templates.TemplateResponse("download.html", {"request": request})