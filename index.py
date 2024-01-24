
from datetime import timedelta
from functools import wraps
import time
from bson import ObjectId
from flask_bcrypt import Bcrypt
from flask import Flask, jsonify, make_response,render_template, request
from mongoengine import connect, disconnect
from dotenv import load_dotenv
from blockList import BlockList
from comment import Comment
from post import Post
from user import User
import os
import json 
import jwt
from flask_jwt_extended import JWTManager, create_access_token, get_jwt, get_jwt_identity, jwt_required
from flask_cors import CORS

app=Flask(__name__)
CORS(
    app,
    origins=[
        "http://localhost:8080",
    ],
)
load_dotenv()
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY", "SECRET_KEY")
mongo_uri = os.getenv("MONGO_URI")
connect(host=mongo_uri)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@jwt.user_identity_loader
def get_id_by_user(user):

    """Callback function to get the identity of the current user."""
    if isinstance(user, User):
        return str(user.id)
    
    return None

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):

    """Callback function to look up a user by identity in JWT data."""   
    identity = jwt_data["sub"]

    return User.objects.get(id=identity)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):

    jti = jwt_payload['jti']
    token = BlockList.objects(jti=jti).limit(1).first()
    return token != None

@app.route('/addcomment/<post_id>', methods=['POST'])
@jwt_required()
def addcomment(post_id):
    current_user_id = get_jwt_identity()
    if not current_user_id:
     return make_response("login to post a vote entry", 401) 
    
    text = request.json.get('text')

    post = Post.objects(id=post_id).first()
    if not post:
        return jsonify({"message": "Post not found"}), 404

    user = User.objects(id=current_user_id).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    comment = Comment(text=text, author=user, post=post)
    comment.save()

    return jsonify({"message": "Comment added"}), 200

@app.route('/getcomment/<post_id>', methods=['GET'])
def getcomment(post_id):
    post = Post.objects(id=post_id).first()

    if not post:
        return jsonify({'error': 'Post not found'})

    comments = Comment.objects(post=post)
    
    if comments:
        comment_list = [{'id': str(comment.id), 'comment': comment.text} for comment in comments]
        return jsonify({'comments': comment_list})
    else:
        return jsonify({'error': 'Comments not found'})


@app.route('/logout', methods=['DELETE'])
@jwt_required()
def logout():
      current_user_id = get_jwt_identity()
      if current_user_id!= None:
        jti = get_jwt()["jti"]
        blockedToken = BlockList(jti=jti) 
        blockedToken.save()
        return jsonify({'message': 'Logout success'})
      else:
        return make_response("Already logged out", 403)

@app.route('/updatepost/<post_id>', methods=['POST'])
@jwt_required()
def updatepost(post_id):
     
     current_user_id = get_jwt_identity()
     if not current_user_id:
        return make_response("login to post a update entry", 401)
     
     post = Post.objects.get(id=post_id, author=current_user_id)
    
     if post:
        updated_data = request.json
        post.title = updated_data.get('title', post.title)
        post.content = updated_data.get('content', post.content)
        post.date = time.time()
        post.save()
        return jsonify({'message': 'Post updated successfully'})
     else:
        return make_response("You don't have permission to update this post or post does not exist", 403)

@app.route('/deletepost/<post_id>', methods=['DELETE'])
@jwt_required()
def  deletepost(post_id):
     
     current_user_id = get_jwt_identity()
     if not current_user_id:
        return make_response("login to post a delete entry", 401)
     
     post = Post.objects.get(id=post_id, author=current_user_id)

     if post:
        post.delete()
        return jsonify({'message': 'Post deleted successfully'})
     else:
        return make_response("You don't have permission to delete this post or post does not exist", 403)

@app.route('/getpostbyauthor', methods=['GET'])
@jwt_required()
def getpostbyauthor():

    current_user_id = get_jwt_identity() 
    post = Post.objects(author=current_user_id)
    post_list = [{'id': str(post.id), 'title': post.title, 'content': post.content} for post in post]

    return jsonify({'posts': post_list})

@app.route('/getposts', methods=['GET'])
def getposts():

    posts = Post.objects().order_by('-date')
    post_list = [{'id': str(post.id), 'title': post.title, 'content': post.content} for post in posts]

    return jsonify({'posts': post_list})

@app.route('/getpost/<post_id>', methods=['GET'])
def getpost(post_id):

    post = Post.objects(id=post_id).first()
    if post:
        posts = {
                'id': str(post.id),
                'title': post.title,
                'content': post.content,
                'date': post.date,
                'author': post.author.username
                }
        return jsonify({'post': posts})
    else:
        return jsonify({'error': 'Post not found'}), 404


@app.route('/addpost', methods=['POST'])
@jwt_required()
def addpost():

    current_user_id = get_jwt_identity()
    print(current_user_id)
    if not current_user_id:
        return make_response("login to post a new entry", 401)
    
    user = User.objects.get(id=current_user_id)

    if request.method == 'POST':
        title = request.json.get('title')
        content = request.json.get('content')

        newPost = Post(
            title=title, content=content, 
            author=user, date=time.time() 
            )
        newPost.save()
        print(current_user_id)
        print(Post.author)
        
        return jsonify({'message': 'create post successfully'})

@app.route('/register', methods=['POST'])
def register(): 

    username = request.json.get('username')
    password = request.json.get('password')

    password = bcrypt.generate_password_hash(password).decode('utf-8')
    if username and password:                
        user = User(username=username, password=password)
        user.save()  

    else:
        return jsonify({'message': 'Fill in the required fields'} )
    
    return jsonify({'message': 'registered successfully'})

@app.route('/login', methods=['POST']) 
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.objects(username=username).first()
    # print(user)
    # print()
    # print(user.id)
    print(app.config["JWT_SECRET_KEY"])
    if not user or not bcrypt.check_password_hash(user.password, password):
        return make_response("Wrong username or password", 401)

    token = create_access_token(identity=user)
    return jsonify({'token': token})

@app.route("/")
def homePage():
    return "My Blog Page"
if __name__=="__main__":
    app.run(debug=True)