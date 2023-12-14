from mongoengine import *
from user import User

class Post(Document):
   title=StringField(required=True)
   content=StringField(required=True)
   author = ReferenceField(User)
   date=FloatField()

