from peewee import *
from app.model import db


class User(Model):

    id = CharField(primary_key=True)
    pw = CharField(null=True)
    name = CharField(null=True)

    class Meta:
        database = db


db.create_tables(User)