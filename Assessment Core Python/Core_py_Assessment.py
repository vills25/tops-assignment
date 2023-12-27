
def add_student(students, roll_id):
    student_details = {}
    serial_number = input("Enter a serial number: ")
    first_name = input("Enter a First name: ")
    last_name = input("Enter a Last name: ")
    contact_number = input("Enter a contact number: ")
    subject = input("Enter a Subject: ")
    marks = input("Enter Marks: ")
    fees = input("Enter Fees: ")

    while not contact_number.isdigit():
        print("Invalid contact number! Please enter a valid number.")
        contact_number = input("Enter a contact number: ")

    student_details['Serial Number'] = serial_number
    student_details['First Name'] = first_name
    student_details['Last Name'] = last_name
    student_details['Contact Number'] = contact_number
    student_details['Subject'] = subject
    student_details['Marks'] = marks
    student_details['Fees'] = fees

    students[roll_id] = student_details
    print("Student added successfully!")
    return student_details


def remove_student(students, roll_id):
    if roll_id in students:
        del students[roll_id]
        print(f"Student with ID {roll_id} removed successfully!")
    else:
        print("Student does not exist!")


def view_all_students(students):
    if students:
        for roll_id, student_info in students.items():
            print(f"ID: {roll_id}, Name: {student_info['First Name']} {student_info['Last Name']}")
    else:
        print("No students found!")


def view_specific_student(students, roll_id):
    if roll_id in students:
        print(f"Student Information for ID {roll_id}:")
        print(students[roll_id])
    else:
        print("Student does not exist!")


def get_students_details(students):
    students_details_dict = {}
    for roll_id, student_info in students.items():
        student_details = {
            'fname': student_info['First Name'],
            'lname': student_info['Last Name'],
            'contact': student_info['Contact Number'],
            'subject': {},
            'faculty': student_info.get('Faculty', '')  # Assuming a faculty field is available
        }

        subject = student_info.get('Subject', '')
        marks = student_info.get('Marks', '')
        fees = student_info.get('Fees', '')

        if subject and marks and fees:
            student_details['subject'][subject] = {'marks': marks, 'fees': fees}

        roll_id = int(roll_id)
        students_details_dict[roll_id] = student_details

    return students_details_dict

students = {}  # Nested dictionary to store student information

while True:
    print("\nSelect a user type:")
    print("press 1 for Counsellor")
    print("press 2 for Faculty")
    print("press 3 for Student")
    roll_id = input("Enter a role id: ")

    if roll_id == '1':  # For Counsellor

        print("\n1. Add student")
        print("2. Remove student")
        print("3. View all students")
        print("4. View Specific Student")
        choice = input("Enter choice by counsellor: ")

        if choice == '1':
            if roll_id in students:
                print("Student with this ID already exists.")
            else:
                student_details = add_student(students, roll_id)
        elif choice == '2':
            remove_student(students, roll_id)
        elif choice == '3':
            view_all_students(students)
        elif choice == '4':
            view_specific_student(students, roll_id)
        else:
            print("Invalid choice!")

    elif roll_id == '2':  # For Faculty
        print("\nFaculty Menu:")
        print("1. Add Marks to Student")
        print("2. View All Students")
        faculty_choice = input("Enter choice by faculty: ")

        if faculty_choice == '1':
            roll_id = input("Enter the roll id to add marks: ")
            if roll_id in students:
                subject = input("Enter the subject: ")
                marks = input("Enter marks: ")
                if marks not in students[roll_id]:
                    students[roll_id][marks] = {}
                students[roll_id][marks][subject] = marks
                print("Marks added successfully!")
            else:
                print("Student with given ID does not exist.")
        elif faculty_choice == '2':
            view_all_students(students)
        else:
            print("Invalid choice!")

    elif roll_id == '3':  # For Student
        print("\nStudent Menu:")
        print("1. View My Grades")
        print("2. View My Fees Details")
        student_choice = input("Enter choice by student: ")

        if student_choice == '1':
            roll_id = input("Enter your roll id: ")
            view_specific_student(students, roll_id)
        elif student_choice == '2':
            roll_id = input("Enter your roll id: ")
            view_specific_student(students, roll_id)
        else:
            print("Invalid choice!")

        more_operations = input("\nDo you want to perform more operations? (Y/n): ")
        if more_operations.lower() != 'y':
            break