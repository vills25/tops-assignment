# Write a program to demonstrate the student management system.

# users = []

# flag = True
# while(flag):
#     user = {}
#     yesNo = input("Enter y/n :")
#     if yesNo.lower() == 'y':
#         username = input("Username: ")
#         email = input("email: ")
#         password = input("password: ")
#         user['username'] = username
#         user['email'] = email
#         user['password'] = password
#         users.append(user)
#     else:
#         flag = False

# print(users)

#############################################

# while (1):
#     users = []
#     flag = True
#     user_info = {}
#     while(flag):
#         tf = input("Enter t or f")
#         if tf.lower() == 't':
#             username, email, password = input("Enter username,email,password : ").split(',')
#             user_info['username'] = username
#             user_info['email'] = email
#             user_info['password'] = password
#             users.append(user_info)
#         else:
#             flag = False
#     print(users)

# counsellor = {
#     '1. Add Student':[
#         'Serial Number'= input('Enter Serial Number: ')
#         input('Enter First Name: ')
#     ]
# }

##########################################################################################################################33

# This program demonstrates a student management system.

# # Define the student management system class.
# class StudentManagementSystem:

#     # Initialize the student management system.
#     def __init__(self):
#         self.students = {}

#     # Add a student to the system.
#     def add_student(self, student_id, first_name, last_name, contact_number):
#         # Validate the student information.
#         if not student_id.isdigit():
#             print("Invalid student ID.")
#             return
#         if not first_name.isalpha():
#             print("Invalid first name.")
#             return
#         if not last_name.isalpha():
#             print("Invalid last name.")
#             return
#         if not contact_number.isdigit():
#             print("Invalid contact number.")
#             return

#         # Add the student to the system.
#         self.students[student_id] = {
#             "first_name": first_name,
#             "last_name": last_name,
#             "contact_number": contact_number
#         }

#         # Print a confirmation message.
#         print("Student added successfully.")

#     # Remove a student from the system.
#     def remove_student(self, student_id):
#         # Validate the student ID.
#         if not student_id.isdigit():
#             print("Invalid student ID.")
#             return

#         # Check if the student exists in the system.
#         if student_id not in self.students:
#             print("Student does not exist.")
#             return

#         # Remove the student from the system.
#         del self.students[student_id]

#         # Print a confirmation message.
#         print("Student removed successfully.")

#     # View all students in the system.
#     def view_all_students(self):
#         # Print a header.
#         print("Student ID | First Name | Last Name | Contact Number")

#         # Iterate over the students and print their information.
#         for student_id, student in self.students.items():
#             print(f"{student_id} | {student['first_name']} | {student['last_name']} | {student['contact_number']}")

#     # View a specific student in the system.
#     def view_student(self, student_id):
#         # Validate the student ID.
#         if not student_id.isdigit():
#             print("Invalid student ID.")
#             return

#         # Check if the student exists in the system.
#         if student_id not in self.students:
#             print("Student does not exist.")
#             return

#         # Print the student's information.
#         student = self.students[student_id]
#         print(f"Student ID: {student_id}")
#         print(f"First Name: {student['first_name']}")
#         print(f"Last Name: {student['last_name']}")
#         print(f"Contact Number: {student['contact_number']}")

#     # Get the student management system menu.
#     def get_menu(self):
#         return """
#         Student Management System Menu

#         1. Add student
#         2. Remove student
#         3. View all students
#         4. View student
#         5. Exit

#         Enter your choice: """

#     # Run the student management system.
#     def run(self):
#         # Display the menu.
#         menu_choice = self.get_menu()

#         # Get the user's choice.
#         while menu_choice != "5":
#             if menu_choice == "1":
#                 self.add_student()
#             elif menu_choice == "2":
#                 self.remove_student()
#             elif menu_choice == "3":
#                 self.view_all_students()
#             elif menu_choice == "4":
#                 self.view_student()
#             else:
#                 print("Invalid choice.")

#             # Display the menu again.
#             menu_choice = self.get_menu()

# # Create a new student management system instance.
# student_management_system = StudentManagementSystem()

# # Run the student management system.
# student_management_system.run()

###################

# Student Management System
"""
Fields :- ['roll', 'name', 'age', 'email', 'phone']
1. Add New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Quit
"""

import csv
# Define global variables
student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'


def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found -----")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any key to continue")


def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")


def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")