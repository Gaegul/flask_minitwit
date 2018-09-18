from datetime import timedelta


class Config:
    SERVICE_NAME = 'Minitwit'

    HOST =
    PORT = 3000
    DEBUG = True

    RUN_SETTINGS = {
        "host": HOST,
        "port": PORT,
        "debug": DEBUG
    }

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=3)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

