# 26. What is Instantiation in terms of OOP terminology? 

'''
Class -- A user-defined prototype for an object that defines a set of attributes that characterize any object of the class.
         The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
Class variable -- A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's
                  methods. Class variables are not used as frequently as instance variables are.
Data member -- A class variable or instance variable that holds data associated with a class and its objects.
Function overloading -- The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects 
                        or arguments involved.
Instance variable -- A variable that is defined inside a method and belongs only to the current instance of a class.
Inheritance -- The transfer of the characteristics of a class to other classes that are derived from it.
Instance -- An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
Instantiation -- The creation of an instance of a class.
Method -- A special kind of function that is defined in a class definition.
Object -- A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance 
          
          variables) and methods.
Operator overloading -- The assignment of more than one function to a particular operator.

'''  
##################################################################################################################################################
 
# 27. What is used to check whether an object o is an instance of class A ?
'''
isintance() function used to check whethere an object o is an instance of class A
'''
##################################################################################################################################################

# 28. What relationship is appropriate for Course and Faculty? 
"""
class Course:
    def info(self, student_name, course_name):
        print(f"Course: {course_name}, Student: {student_name}")
       
class Faculty(Course):
    def detail(self, faculty_name, branch):
        print(f"Faculty: {faculty_name}, Branch: {branch}")

d = Faculty()

student_name = input("Enter student's name: ")
course_name = input("Enter course name: ")
faculty_name = input("Enter faculty's name: ")
branch = input("Enter branch: ")

d.info(student_name, course_name)
d.detail(faculty_name, branch)
"""

##################################################################################################################################################

# 29. What relationship is appropriate for Student and Person? 

"""
class Person:
    def detail(self, p_name, age, city):
        print(f"Person name: {p_name}, Age: {age}, City: {city}")
        
class Student(Person):
    def info(self, student_name, student_age, education, person_age, city,p_name):
        self.detail(p_name, person_age, city)
        print(f"Student: {student_name}, Age: {student_age}, Education: {education}")

d = Student()

student_name = input("Enter student's name: ")
student_age = input("Enter student's age: ")
p_name = input("Enter person name: ")
person_age = input("Enter person's age: ")
city = input("Enter city: ")
education = input("Enter your Education: ")

d.info(student_name, student_age, education, person_age, city, p_name)
"""

##################################################################################################################################################
