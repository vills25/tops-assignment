from log import log_file
from counsellor import view_specific_student, students

def student_menu():
    while True:
        print("\nStudent Menu:")
        print("1. View My Grades")
        print("2. View My Fees Details")
        student_choice = input("Enter choice by student: ")

        if student_choice == '1':
            roll_id = input("Enter your roll id: ")
            view_specific_student(students, roll_id)
            log_file(f"Student With Roll id {roll_id} spotted.")
        elif student_choice == '2':
            roll_id = input("Enter your roll id: ")

            view_specific_student(students, roll_id)
        else:
          print("Invalid choice!")
            
        ch = input("do you want to perform more operations? y/N : ")
        if ch.lower() == "n":
            break
        else:
            continue