from peewee import *
from app.model import db
from datetime import datetime


class Post(Model):
    title = CharField(null=True)
    content = TextField(null=True)
    user = CharField(null=True)
    create_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
