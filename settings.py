from typing import Set
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'Blog'
    APP_VERSION: str = '0.0.1'
    POSTGRESQL_USERNAME: str = 'postgres'
    POSTGRESQL_PASSWORD: str = 'postgres'
    POSTGRESQL_HOST: str = 'fapipostgres'
    POSTGRESQL_DATABASE: str = 'blog'


settings = Settings()
