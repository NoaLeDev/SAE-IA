from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "C'est une API"

@app.route("/regression")
def regress(): 
    pass

