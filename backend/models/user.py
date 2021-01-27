from database.db import db


class User(db.Document):
    # pylint: disable=no-member
    id = db.IntField(required=True, primary_key=True)
    # pylint: disable=no-member
    username = db.StringField(required=True, unique=True, max_lenght=200)
    # pylint: disable=no-member
    password = db.StringField(required=True)

    meta = {'strict': False}