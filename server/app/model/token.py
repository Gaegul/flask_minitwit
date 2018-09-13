from peewee import *
from app.model import db


class Token(Model):
    access_token = CharField()

    refresh_token = CharField()

    class Meta:
        database = db
