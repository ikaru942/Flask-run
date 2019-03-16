from flask import Flask, render_template

course_list = []
course_list = dict()
course_list["title"] = "Software Engineering"
course_list["code"] = "CUS 1166"
course_list["info"] = "Monday, Thurssday, 15:25 - 16:50"
course_list["description"] = "In this course students will learn to build software systems"
course_list.append(course_info)
course_list = dict()
course_list ["title"] = "Data Mining and Predictive Modeling"
course_list["code"] = "CUS 615"
course_list["info"] = "Thursday, 15:25 - 16:50"
course_list["description"] = "In this course, we cover both the theory and advancd practice"
course_list.ppend(course_info)

app = Flask(__name__)
