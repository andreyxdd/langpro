from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Notes(BaseModel):
    contents: List[str]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/post-contents")
def update_item(body: Notes):
    print(body.contents)
    return {"status": "Success!"}
