from flask import flask

app = Flask(__name__)



@app.route("/")
def index():
    return "Hello World!!! What do you want?"

@app.route("/cus1166")
def cus1166():
    return "Hello, Welcome to CUS 1166!"

@app.route("/cus615")
def cus615():
    return "Hello, Welcome to CUS 615!"

#flask runself
