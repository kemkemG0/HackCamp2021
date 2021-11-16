from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse
from fastapi import FastAPI, File, UploadFile
from pathlib import Path
from tempfile import NamedTemporaryFile
import shutil
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


app = FastAPI()
# for calling js under 'static/'
app.mount("/static", StaticFiles(directory="static"), name="static")

# for rendering index.html under 'templates/'
templates = Jinja2Templates(directory="templates")


@app.post("/api")
def api(video: UploadFile = File(...)):
    tmp_path = save_upload_file_tmp(video)
    tmp_path = str(tmp_path)

    data = save_all_frames(tmp_path)

    return {"art": data}


@app.get("/")
def index(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("index.html", {"request": request})
