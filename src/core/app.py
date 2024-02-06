from fastapi import FastAPI


app = FastAPI()

from core.configure import configure

configure(app)