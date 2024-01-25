from mongoengine import *
from user import User
from post import Post

class Vote(Document):
    user = ReferenceField(User)
    post = ReferenceField(Post)
    vote = StringField()
    
