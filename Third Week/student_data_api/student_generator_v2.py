#get student class
import student
from datetime import datetime
"""
function to write error log file
Input: error message
Output: none
"""
def write_to_error_log(error_message):
    try:
        #open log file
        log_file = open("error_log.txt", 'a')

        #write error message to log file
        log_file.write(f'{datetime.now()}: {error_message}\n')

        #close log file 
        log_file.close()
    except Exception as err:
        print(err)

    return

def load_students(file_name):

    student_list = []

    #import student data
    student_file = open(f'{file_name}', 'r')

    #skip first line
    student_file.readline()

    line_number = 1
    #load each line
    for student_line in student_file:
        line_number +=1

        #split each line at the comma
        student_values = student_line.split(',')
        try:
            if len(student_values) != 6:
                raise Exception(f'There\'s an error at line {line_number}')
        except Exception as err:
            write_to_error_log(str(err))
            continue

        #get values
        try:
            first_name = student_values[0]
            last_name = student_values[1]
            major = student_values[2]
            credit_hours = int(student_values[3])
            gpa = float(student_values[4])
            id_number = int(student_values[5])
        except:
            write_to_error_log(f'There\'s an error at line {line_number}')

        #create instance
        new_student = student.Student(first_name, last_name, major, credit_hours, gpa, id_number)

        #add to an empty list
        student_list.append(new_student)

    #close file
    student_file.close() 

    #return list
    return student_list

#Input: list of student objects
#Output: lsit of student dictionaries
#create a function student_to_dictionary that creates a student dictionary for each student object 
def student_to_dictionary(list_of_students):
    #create empty list
    student_dictionary_list = []

    #loop through student list and assign values
    for student in list_of_students:
        new_student_dictonary = {
            "first name": student.get_first_name(),
            "last name": student.get_last_name(),
            "ID": student.get_id_number(),
            "major": student.get_major(),
            "gpa": student.get_gpa(),
            "class": student.get_class_level()
        }
        #append to list
        student_dictionary_list.append(new_student_dictonary)

    return student_dictionary_list

def get_student_dictionaries():  
    #call function
    student_list = load_students('students.csv')

    #Function to create a list of student dictionaries
    #transform a list of students into a list of student dictionaries
    student_dict_list = student_to_dictionary(student_list)

    return student_dict_list