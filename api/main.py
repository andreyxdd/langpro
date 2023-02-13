from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel
from noteprocessor import process_prompt

app = FastAPI()


class Notes(BaseModel):
    contents: List[str]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/post-contents")
def update_item(body: Notes):
    request = 'Summary'
    processed_notes = []
    for note in body.contents:
        processed_notes.append(process_prompt(request, note))
    print(processed_notes)
    return {"status": "Success!"}
