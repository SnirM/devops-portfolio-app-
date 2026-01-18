from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int

DB = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/person")
def get_people():
    return DB

@app.post("/person/{person_id}")
def add_person(person_id: int, person: Person):
    DB[person_id] = person.dict()
    return {"message": "Person added", "data": DB[person_id]}
