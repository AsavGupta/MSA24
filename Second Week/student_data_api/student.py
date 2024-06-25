#Create a Student class
class Student():

    #Define Constructor
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        #assing private class properties
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id_number = id_number

    #prints all student data
    def print_student_data(self):
        print(f'{self.__first_name} {self.__last_name}')
        print(f'{self.__major}: {self.__credit_hours} Credit Hours - GPA: {self. __gpa:.2f}')
        print(f'{self.__id_number}')

    #First Name
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self, new_first):
        if new_first == "":
            ('ERROR: New name must not be empty\n')
            return 
        else:
            self.__first_name = new_first

    #Last Name
    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, new_last):
        if new_last == "":
            ('ERROR: New name must not be empty\n')
            return 
        else:
            self.__last_name = new_last
    
    #Major
    def get_major(self):
        return self.__major
    
    def set_major(self, new_major):
        if new_major == "":
            ('ERROR: New major must not be empty\n')
            return 
        else:
            self.__major = new_major
    
    #Credit Hours
    def get_credit_hours(self):
        return self.__credit_hours
    
    def update_credit_hours(self, additional_hours):
            try:
                if additional_hours < 0:
                    print('ERROR: Enter a valid number of additional hours\n')
                else:
                    self.__credit_hours += int(additional_hours)
            except:
                print('ERROR: Enter a valid number of additional hours\n')

    #GPA
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, new_gpa):
        try:
            if new_gpa < 0:
                print('ERROR: Enter a valid gpa\n')
            else:
                self.__gpa = float(new_gpa)
        except:
            print('ERROR: Enter a valid gpa\n')
    
    def get_id_number(self):
        return self.__id_number
    
    def get_class_level(self):
        if self.__credit_hours > 90:
            return "Senior"
        elif self.__credit_hours > 60:
            return "Junior"
        elif self.__credit_hours > 30:
            return "Sophomore"
        else:
            return "Freshman"
    
    