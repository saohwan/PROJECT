from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models.book import BookModel
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine


from app.models import mongodb


BASE_DIR = Path(__file__).resolve().parent  # 절대 경로 지정.


app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    book = BookModel(keyword="파이썬", publisher="BJPublic",
                     price=1200, image="me.png")
    print(await mongodb.engine.save(book))  # DB 에 저장
    return templates.TemplateResponse("./index.html", {"request": request, "title": "북북이"})


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):

    return templates.TemplateResponse("./index.html", {"request": request, "title": "북북이", "keyword": q})


@app.on_event("startup")  # app server.py 가 실행될때 같이 실행되는 함수.
def on_app_start():
    print("hello server")
    mongodb.connect()


@app.on_event("shutdown")
def on_app_shutdown():
    print("By Server")
    """after app shutdown"""
    mongodb.close()
