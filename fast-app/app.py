from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from time import sleep


class Item(BaseModel):
    num: int


app = FastAPI()
# for calling js under 'static/'
app.mount("/static", StaticFiles(directory="static"), name="static")
# for rendering index.html under 'templates/'
templates = Jinja2Templates(directory="templates")


@app.post("/api")
def api(video: UploadFile = File(...)):
    data = video.filename
    return {"art": data}


@app.get("/")
def index(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("index.html", {"request": request})
