from fastapi import FastAPI
from fastapi import APIRouter
from app.models.blog import Blog

blog_api = APIRouter()

@blog_api.get("/landing-page")
async def get_notes():
    # await Blog.create(title="asdfasdfasdfasdf")
    blog = Blog.get(id=1)
    print(dir(blog))
    return {"hello": 'asdfasdf'}
