from peewee import *
from app.model import db


class Post(Model):

    title = CharField(null=True)
    content = TextField(null=True)
    user = CharField(null=True)

    class Meta:
        database = db
