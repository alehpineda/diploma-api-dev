from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Participant(BaseModel):
    id: int
    name: str
    last_name: str


class Diploma(BaseModel):
    name: str
    last_name: str


@app.get("/")
def read_root():
    return {"Hola": "Mundo"}


@app.post("/v1/diploma_test", response_model=Diploma)
def post_data(participant: Participant) -> Diploma:
    return participant


@app.get("/v1/health", status_code=200)
def health_check():
    return {"Message": "DIPLOMA API V10 - Up and running!!!"}
