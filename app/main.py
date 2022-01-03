import uvicorn
from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class Enumcls(str, Enum):
    Name = "name"
    Phone = "phone"
    Birthday = "birthday"


@app.get("/")
def main(param: Enumcls):
    return f"Hello, World {param}"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
