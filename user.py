from mongoengine import *

class User(Document):
    username = StringField(required=True, uniqe=True)
    password = StringField(required=True)


