from fastapi import FastAPI

app = FastAPI()

from gpt_module.routers import messenger

app.include_router(messenger.router)

