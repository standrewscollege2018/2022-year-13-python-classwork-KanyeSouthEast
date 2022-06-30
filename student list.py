'''making stuff for a class '''

class Student:
    '''someythingg'''
    def __init__(self, name, age, phone_number, classes):
        #set name
        self._name = name
        
        #set age
        self._age = age
        
        #set phone number
        self._phone_number = phone_number
        self._classes = classes
        self._enrolled = True 
        
        #append the new student into the student_list
        student_list.append(self)        
    
    def get_name(self):
        ''' returns name '''
        return self._name
    
    def get_age(self):
        '''returns age'''
        return self._age

    def get_phone_number(self):
        '''return phone number'''
        return self._phone_number
    def get_enrolled(self):
        ''' Return student enrolment status'''
    
        return self._enrolled    
    
    def get_classes(self):
        
        class_list = ""
        for c in self._classes:
            class_list += c+ " "
        return class_list
        
    
    
#create student list
student_list = []




#create new student
Student("charliekeithbad.php",12, "0276555702", ["math", "DIGI"])
Student("ben shit himself in a shed",17, "0276555702", ["MATH", "ENG", "PHYS"])






def display_students():
    '''this function displays the students names'''

    for s in student_list:
        
        
        print(f"{s.get_name()}")


def display_student(name):
    '''displays name for entered student'''
    
    for s in student_list:
        if name in s.get_name():
            print("=" *30)
            print(f"Name: {s.get_name()}")
            print(f"Age: {s.get_age()}")
            print(f"Phone: {s.get_phone_number()}")
            print(f"Classes: {s.get_classes()}")
            print("=" * 30)
            print("")
            


display_students()       
            
student_name = input("enter name:")

display_student(student_name)