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