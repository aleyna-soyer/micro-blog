from mongoengine import *

class User(Document):
    username = StringField(required=True, NotUniqueError=True)
    password = StringField(required=True)


