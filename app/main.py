import uvicorn

from pydantic import BaseModel, HttpUrl
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


class User(BaseModel):
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None


@app.get("/", response_model=User)
def main(user):
    return user


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
