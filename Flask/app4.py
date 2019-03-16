from flask import flask

app = Flask(__name__)

#Things to note:
# - Flask looks for templates folder for the templates
# - I can pass parameters to the templateself.
# - I can obtain arguements from the request and pass as arguments to templates
# - Highlight linga2 templating language/
# Selarattion of UI and logic
# templates allow me to reuse template code.


#Demonstrate seperation of templates, basic
@app.route("/")
def index():
    return render_template("index.html")

#Seperation of UI
#Example of passing parameters to the template.
#the couse after the = refers to the course in welcome(course)
@app.route("/welcome/<string:course>")
def welcome(course)
    return render_template("index2.html", course = course)

#Example of codnitionl rendering in templates.
if the course is cus1166 or cus615 then will excute code
@app.route("/do/i/teach/string:course>")
def doiteach(course):
    doTeach = (course == "CUS1166") or (course == "CUS615")
    return render_template("index3.html", course = course, roster = roster)

#Example of loops in tmplates.
@app.route("/roster/<string:course>")
def roster(course):
    roster = [("John", "A"), ("Tom", "B"), ("Mary", "C"), ("Lucas", "B-"), ("Joan", "D")]
    return render_template("index.html", course = course, roster = roster)
