from fastapi import FastAPI
from core.configure import configure


def create() -> FastAPI:
    app = FastAPI(
        title="InfaNaSotkuSite",
        version="1.0.0",
        redoc_url=None,
        docs_url=None
    )

    configure(app)
    return app
