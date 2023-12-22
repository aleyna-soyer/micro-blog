from functools import wraps
from flask_bcrypt import Bcrypt
from flask import Flask, jsonify, make_response,render_template, request
from mongoengine import connect, disconnect
from dotenv import load_dotenv
from post import Post
from user import User
import os
import json 
import jwt

app=Flask(__name__)
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
connect(host=mongo_uri)
bcrypt = Bcrypt(app)
secret_key = os.getenv("SECRET_KEY")

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

    if not user or not bcrypt.check_password_hash(user.password, password):
        return make_response("Wrong username or password", 401)

    token = jwt.encode({'username': user.username}, secret_key)
    return jsonify({'token': token})
     
@app.route("/")
def homePage():
    return "My Blog Page"
if __name__=="__main__":
    app.run(debug=True)