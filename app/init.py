from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.settings import settings
from app.models.blog import Blog
from app.api.blog import blog_api
from app.home import landing_page


def create_app() -> FastAPI:
    api = FastAPI(docs_url="/docs", title=settings.APP_NAME, version=settings.APP_VERSION)

    register_tortoise(
        api,
        db_url=build_db_uri(
            user=settings.POSTGRESQL_USERNAME,
            password=settings.POSTGRESQL_PASSWORD,
            host=settings.POSTGRESQL_HOST,
            db=settings.POSTGRESQL_DATABASE
        ),
        modules={'models': ['app.models.blog', ]},
        generate_schemas=True,
        add_exception_handlers=True
    )

    register_views(api)

    return api

def register_views(api: FastAPI):
    api.include_router(blog_api, prefix="/api/v1", tags=["blog-api", ])
    api.include_router(landing_page, tags=["landing-page", ])


def build_db_uri(user, password, host, db):
    uri = f"postgres://{user}:{password}@{host}:5432/{db}"
    return uri
