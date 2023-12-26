from mongoengine import *

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)


