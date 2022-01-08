import uvicorn

from fastapi import FastAPI

app = FastAPI()




@app.get("")
def create_item():
    return "item"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)