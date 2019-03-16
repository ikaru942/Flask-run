from flask import flask

app = Flask(__name__)


@app.route("/")
def index():
    return rendur_template("index.html")

@app.route('/course', defults={'couse_id': 1})
@app.route('/course/<int:course_id>')
def course(course_id):
    return render_template("course_info_a.html", course_info=course_list[course_id-1])

if __name__ == "__main__":
    app.run()
