from log import log_file

students = {}

def add_student(students, roll_id):
    student_details = {}
    serial_number = input("Enter a serial number: ")
    first_name = input("Enter a First name: ")
    last_name = input("Enter a Last name: ")
    contact_number = input("Enter a contact number: ")
    while not contact_number.isdigit():
        print("Invalid contact number! Please enter a valid number.")
        contact_number = input("Enter a contact number: ")
            
    subjects = {}
    subjects_num = int(input("How many subjects do you want to add?: "))    
    for _ in range(subjects_num):
        subject = input("Enter subject name: ")
        marks = input("Enter Marks: ")
        fees = input("Enter Fees: ")
        faculty_name = input("Enter faculty name: ")
        subjects[subject] = {'marks': marks, 'fees': fees, 'faculty':faculty_name }
        
    student_details['Serial Number'] = serial_number  
    student_details['First Name'] = first_name
    student_details['Last Name'] = last_name
    student_details['Contact Number'] = contact_number
    student_details['Subjects'] = subjects
    
    students[roll_id] = student_details
    print(dict(student_details))
    log_file(f"Added student with ID {roll_id}")
    return student_details
    
def remove_student(students, roll_id):
    if roll_id in students:
        del students[roll_id]
        log_file(f"Removed student with ID {roll_id}")

        print(f"Student with ID {roll_id} removed successfully!")
    else:
        print("Student does not exist!")

def view_all_students(students):
    if students:
        print(dict(students))           
    else:
        print("No students found!")

def view_specific_student(students, roll_id):
    if roll_id in students:
        print(f"Student Information for ID {roll_id}:")
        print(students[roll_id])
    else:
        print("Student does not exist!")
        
def counsellor_menu():
    while True :
        print("\nCounsellor Menu:")
        print("1. Add student")
        print("2. Remove student")
        print("3. View all students")
        print("4. View Specific Student")
        choice = input("Enter choice by counsellor: ")

        if choice == '1':
            roll_id = input("Enter the roll id for the new student: ")
            if roll_id in students:
                print("Student with this ID already exists.")
            else:
                student_details = add_student(students, roll_id)
        elif choice == '2':
            roll_id = input("Enter the roll id to remove student: ")
            remove_student(students, roll_id)
        elif choice == '3':
            view_all_students(students)
        elif choice == '4':
            roll_id = input("Enter the roll id to view specific student: ")
            view_specific_student(students, roll_id)
        else:
            print("Invalid choice!")
            
        ch = input("do you want to perform more operations? y/N : ")
        if ch.lower() == "n":
            break
        else:
            continue            