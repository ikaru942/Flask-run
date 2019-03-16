#Importing Flask class from the flask module
from flask import flask

#Create an instance of Flassk class
app = Flask(__name__)

# This we define a new route
# - Flask is designed in terms of routesselfself.
# - Routes are part of the URL a client is requestingself.
# - When a user goes to the default route - this is the function I wnt to runself.
# - app.routh() is a decoratorself.

# when user types '/' it will do the method to print 'Hello World!!!'
@app.route("/")
def index():
    return "<h1 style='color:red'> Hello World!!! </h1><h2> Hello World!!! </h2><h3> Hello World!!! </h3>"

# through the commandline if the name is __name__ we want to take the take that instance and involove that run method of that class.
if __name__ == "__main__":
    app.run()


# flask runself # python app.py
