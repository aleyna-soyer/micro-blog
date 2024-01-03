from mongoengine import *

class BlockList(Document):
    jti = StringField(required=True)