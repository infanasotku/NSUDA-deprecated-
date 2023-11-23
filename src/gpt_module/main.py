from fastapi import FastAPI

app = FastAPI()

from gpt_module.routers import messenger

app.include_router(messenger.router)

from fastapi.staticfiles import StaticFiles
from pathlib import Path
srcPath = Path(__file__).parent.parent.absolute()

app.mount(
    "/static",
    StaticFiles(directory=srcPath / "static"),
    name="static"
)