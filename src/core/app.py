from fastapi import FastAPI


app = FastAPI(
    title="InfaNaSotkuSite",
    version="1.0.0",
    redoc_url=None,
    docs_url=None
)

from core.configure import configure

configure(app)