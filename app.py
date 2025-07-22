from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Month(BaseModel):
    year: int
    month: int

class Person(BaseModel):
    name: str
    work: str
    days: list
    should_work_times: int
    worked_times: int

class People(BaseModel):
    people: list[Person]



