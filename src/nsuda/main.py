from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every


app = FastAPI()

# Connects static files

from fastapi.staticfiles import StaticFiles
from pathlib import Path

srcPath = Path(__file__).parent.parent.absolute()

app.mount(
    "/static",
    StaticFiles(directory=srcPath / "static"),
    name="static"
)

# Connects gpt module
from gpt_module import main
app.mount(
    "/gpt",
    main.app,
    "gpt"
)

# Connects routers

from nsuda.routers import roots
app.include_router(roots.router)

from nsuda.routers import users
app.include_router(users.router)

from nsuda.internal import admin
app.include_router(admin.router)


# Connects xray updating event
from nsuda.xray import handler

@app.on_event("startup")
@repeat_every(seconds=10)
async def update_server():
    await (await handler.HandlerBuilder.get_instanse()).update_uuid()