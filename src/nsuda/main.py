from fastapi import FastAPI, BackgroundTasks

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

# Inits and starts xray
from nsuda.xray import handler
handler.HandlerBuilder.init_handler()

# Connects xray handler

#BackgroundTasks().add_task(handler.update_uuid) 

