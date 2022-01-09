import uvicorn

from fastapi import FastAPI, File, UploadFile
from tempfile import NamedTemporaryFile
from typing import IO

app = FastAPI()

# 파일을 바이트로 받음
@app.post('/file/size')
def get_file_size(file: bytes = File(...)):
    return {"file_size": len(file)}

# 파일 정보 출력
@app.post("/file/info")
def get_file_info(file: UploadFile = File(...)):
    return {
        "content_type": file.content_type,
        "filename": file.filename
    }

# 비동기 작업
@app.post("/file/info")
async def get_file_info(file: UploadFile = File(...)):
    file_like_obj = file.file
    contents = await file.read()

    return {
        "content_type": file.content_type,
        "filename": file.filename,
    }


# 파일 저장
async def save_file(file: IO):
    # s3 업로드라고 생각해 봅시다. delete=True(기본값)이면
    # 현재 함수가 닫히고 파일도 지워집니다.
    with NamedTemporaryFile("wb", delete=False) as tempfile:
        tempfile.write(file.read())
        return tempfile.name

@app.post("/file/store")
async def store_file(file: UploadFile = File(...)):
    path = await save_file(file.file)
    return {"filepath": path}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)