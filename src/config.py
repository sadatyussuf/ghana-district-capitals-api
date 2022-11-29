from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DEBUG: bool

    class Config:
        env_file = ".env"


setting = Settings()
