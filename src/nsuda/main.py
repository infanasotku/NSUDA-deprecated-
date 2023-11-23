from fastapi import FastAPI


app = FastAPI()

from fastapi.staticfiles import StaticFiles
from pathlib import Path
srcPath = Path(__file__).parent.parent.absolute()

app.mount(
    "/static",
    StaticFiles(directory=srcPath / "static"),
    name="static"
)


from nsuda.routers import roots
app.include_router(roots.router)

from nsuda.routers import users
app.include_router(users.router)

from nsuda.internal import admin
app.include_router(admin.router)