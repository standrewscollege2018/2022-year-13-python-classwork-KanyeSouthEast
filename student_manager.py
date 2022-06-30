''' using a csv file to display hundreds of users'''
class Student:
    '''defines student class'''
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
            

def generate_students():
    '''import students from csv file'''
    
    import csv
    
    with open('myRandomStudents.csv', newline='') as csvfile:
        
        filereader = csv.reader(csvfile)
        
        for line in filereader:
            
            classes = []
            i=3
            while i in range (3,8):
                if line[i] not in all_classes:
                    all_classes.append(line[i])
                classes.append(line[i])
                i +=1
                
            Student(line[0], int(line[1]), int(line[2]), classes)
            
def class_search():
    ''' this function gets the user to enter a lacc code (eg. MAT) and return
    the list of students enrolled in the class and number of results'''
    
    print("select the class:")
    for c in range(len(all_classes)):
        print(f"{c+1}. {all_classes[c]}")
    
    selection = int(input("Class number: "))
    count = 0
    
    for s in student_list:
        if all_classes[selection-1] in s.get_classes():
            count += 1
            print(s.get_name())
            
    print(f"{count} sutdents found")
    
    
def add_student():
    '''function enables us to add a new student'''
    name= input("name: ")
    age = int(input("age: "))
    phone_number = int(input("phone number: "))
    input_classes = True 
    classes = []
    print("\n Input classes type quit when finished")
    while input_classes == True:
        cl = input("enter class codes")
        
        if cl =="quit":
            input_classes = False
            
        else:
            classes.append(cl)
            
    Student(name,age,phone_number, classes)
    display_student(name)
    print("duck")
            
def delete_student(name):
    '''function to delete a student'''
    
    for s in student_list:
        if s.get_name ==name:
            index = student_list.index(s)
            del student_list[index]
            print(f"{name} deleted")
            
        else:
            print("no matching students found")
    
    
    
    
all_classes = []
            
generate_students()
            
            
run_program = True
while run_program:
    print("1. Add student\n2. Class lists\n 3. Search for student\n4. display all students\n5. delete student")
    selection = int(input())
    
    if selection ==1:
        add_student()
        
    elif selection ==2:
        class_search()
    elif selection ==3:
        name = input("Enter name: ")
        display_student(name)
    elif selection ==4:
        display_students()
    elif selection ==5:
        
        counter =0
        for s in student_list:
            counter += 1
            
            print(f"{counter}. {s.get_name()}")        
        name = input("Enter name: ")
        delete_student(name)
    else:
        run_program = False
        
        

#class_search()
#display_students()

#student_name = input("Enter name of student:")


#add_student()


