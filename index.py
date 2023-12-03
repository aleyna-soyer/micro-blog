from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def homePage():
    return "My Blog Page"
if __name__=="__main__":
    app.run(debug=True)