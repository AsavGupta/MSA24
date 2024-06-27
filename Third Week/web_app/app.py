#import modules
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set secret key to use when validating form data
app.config["SECRET_KEY"] = "YOURMOM"

#define constant value for url
URL = 'http://127.0.0.1:5000/api/students/all'

#function to request student data from the api
#Input: url
#Output: JSON student data
def get_student_data():
    #make a request
    response = requests.get(URL)
    
    #convert format to JSON
    response_json = response.json()
    
    return response_json

#function to return a unique list of majors
#Input: url
#Output: list of uniqe majors
def get_unique_majors():
    unique_major_list = []
    
    for student in get_student_data():
        if student['major'] not in unique_major_list:
            unique_major_list.append(student['major'])

    unique_major_list.sort()
    return unique_major_list

#create a route for the site index page that will dispay all student data
@app.route("/", methods=["GET"])
def index():
    #get the student data
    #make a request to the student data api url
    
    student_data = get_student_data()
    
    #send the student data to the index.html page
    return render_template('index.html', student_data = student_data)
    
@app.route("/majors", methods=["GET"])
def majors():
    #write code that gets a unique list of majors from student data
    major_list = get_unique_majors()

    return render_template('majors.html', major_list = major_list)

@app.route("/majors", methods=['POST'])
def majors_post():

    major_list = get_unique_majors()
    student_in_major_list = []

    #get the form data that was submitted
    current_major = request.form.get('major')
    #validate our form data. If invalid form data, then show error message
    if not current_major:
        flash("You must select a major")
    else:
        #Find Students with the slected major and return to the majors.html page
        #get student data
        student_list = get_student_data()
        #loop through list of students 
        for student in student_list:
            if student['major'] == current_major:
                student_in_major_list.append(student)

    return render_template('majors.html', major_list = major_list, student_in_major_list = student_in_major_list, current_major = current_major)

app.run(port=5005)
