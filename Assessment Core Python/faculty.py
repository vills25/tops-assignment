from counsellor import view_all_students,students
from log import log_file

def faculty_menu():
    while True :
        print("\nFaculty Menu:")
        print("1. Add Marks to Student")
        print("2. View All Students")
        faculty_choice = int(input("Enter choice by faculty: "))

        if faculty_choice == '1':
            roll_id = int(input("Enter the roll id to add marks: "))
            if roll_id in students:
                subject = input("Enter the subject: ")
                marks = int(input("Enter marks: "))

                if 'Subject' not in students[roll_id]:
                    students[roll_id]['Marks'] = {}

                students[roll_id]['Marks'][subject] = marks
                print("Marks added successfully!")
                log_file (f"Faculty added marks to Roll id {roll_id}")
            else:
                print("Student with given ID does not exist.")
        elif faculty_choice == '2':
            view_all_students(students)
        else:
            print("Invalid choice!")
            
        ch = input("Do you want to perform more operations? (y/N): ")
        if ch.lower() == "n":
            break
        else:
            continue
        
def view_all_students(students):
    if students:
        for roll_id, student_info in students.items():
            print(f"ID: {roll_id}, Name: {student_info['First Name']} {student_info['Last Name']}")
    else:
        print("No students found!")        