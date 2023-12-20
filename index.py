from flask import Flask,render_template
from mongoengine import connect, disconnect
#from dotenv import load_dotenv
from post import Post
import os
import json 

app=Flask(__name__)

@app.route("/posts")
def list_posts():
    #load_dotenv()
    mongo_uri = os.getenv("MONGO_URI")
    connect(host=mongo_uri)

    all_posts = []
    for p in Post.objects():
        
        all_posts.append(p.to_json())
        disconnect()

    return json.dumps(all_posts)     

@app.route("/")
def homePage():
    return "My Blog Page"
if __name__=="__main__":
    app.run(debug=True)