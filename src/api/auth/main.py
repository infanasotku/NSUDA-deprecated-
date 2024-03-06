from fastapi import FastAPI
from api.auth.configure import configure

auth = FastAPI()

configure(auth)