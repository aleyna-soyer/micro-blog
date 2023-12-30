from mongoengine import *
from post import Post
from user import User

class Comment(Document):
    author = ReferenceField(User)
    post = ReferenceField(Post)
    text = StringField(required=True)