from mongoengine import connect

from .utilis import get_settings


def connect_to_database():
    settings = get_settings()

    if settings.DEBUG:
        print("connected to production server")
        connect(db=settings.DB_NAME, host=settings.PROD_DB_HOST)
    if not settings.DEBUG:
        print("connected to local server")
        connect(db=settings.DB_NAME, host=settings.DB_HOST, port=settings.DB_PORT)
