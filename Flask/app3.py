from flask import flask

app = Flask(__name__)



@app.route("/")
def index():
    return "Hello"
#Note that the template variable <string:course> is passed as a keyword argumentself.
# to the decorated funtion 'welcome'. Thus the function welcome MUST define a variable.
#if someone enters /welcome then execute the code below.
@app.route("/welcome/<string:course>")
def welcome(course):
    #coure = course.capitalize()  Use {} to format strings
    return f"Welcome to {course}"

# Note that the route defines two parameters
# - Note route returns html page.
@app.route("/welcome/string:course>/<int:size>/<int:color>")
def welcome_h(coursee, size, color):
    colors = {'red', 'green', 'blue', 'yello', 'gray', 'lime'}
    return(f"<h(size) style+'color:{colors[color]})>Welcome to {course} <h{size}>")
