from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from time import sleep
from pathlib import Path
from tempfile import NamedTemporaryFile
import shutil
import cv2
from imgProc.getFrame import save_all_frames


def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
        tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path


def get_length_of_video(path: str) -> int:
    cap = cv2.VideoCapture(path)                  # load video
    video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # get num frame
    video_fps = cap.get(cv2.CAP_PROP_FPS)                 # get frame rate
    video_len_sec = video_frame_count / video_fps         # calc
    return video_len_sec


app = FastAPI()
# for calling js under 'static/'
app.mount("/static", StaticFiles(directory="static"), name="static")
# for rendering index.html under 'templates/'

templates = Jinja2Templates(directory="templates")


@app.post("/api")
def api(video: UploadFile = File(...)):
    tmp_path = save_upload_file_tmp(video)
    tmp_path = str(tmp_path)

    save_all_frames(tmp_path)

    data = 'OK!!!!!!'

    return {"art": data}


@app.get("/")
def index(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("index.html", {"request": request})
