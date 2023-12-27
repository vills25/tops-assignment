class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get_name(self):
    return self.name

  def get_age(self):
    return self.age

  def get_grade(self):
    return self.grade

class StudentManagementSystem:
  def __init__(self):
    self.students = []

  def add_student(self, student):
    self.students.append(student)

  def get_students(self):
    return self.students

  def get_student_by_name(self, name):
    for student in self.students:
      if student.get_name() == name:
        return student
    return None

  def get_student_by_age(self, age):
    for student in self.students:
      if student.get_age() == age:
        return student
    return None

  def get_student_by_grade(self, grade):
    for student in self.students:
      if student.get_grade() == grade:
        return student
    return None

  def remove_student(self, student):
    self.students.remove(student)

  def update_student(self, student, new_name, new_age, new_grade):
    student.set_name(new_name)
    student.set_age(new_age)
    student.set_grade(new_grade)

def main():
  sms = StudentManagementSystem()

  # Add some students to the system
  sms.add_student(Student("John Doe", 15, "10th"))
  sms.add_student(Student("Jane Doe", 16, "11th"))
  sms.add_student(Student("Peter Parker", 17, "12th"))

  # Get all students in the system
  students = sms.get_students()

  # Print the names of all students
  for student in students:
    print(student.get_name())

if __name__ == "__main__":
  main()