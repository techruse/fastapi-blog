from typing import Set
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'Blog'
    APP_VERSION: str = '0.0.1'
    POSTGRESQL_USERNAME: str = 'guest'
    POSTGRESQL_PASSWORD: str = 'guest'
    POSTGRESQL_HOST: str = 'kpostgres'
    POSTGRESQL_DATABASE: str = 'blog'


settings = Settings()
