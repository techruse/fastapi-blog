from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

landing_page = APIRouter()
templates = Jinja2Templates("app/templates")

@landing_page.get("/", include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

