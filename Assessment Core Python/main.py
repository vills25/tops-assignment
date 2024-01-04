from log import log_file
from counsellor import counsellor_menu
from faculty import faculty_menu
from student import student_menu

def main_menu():
    while True:
        print("\nSelect a user type:")
        print("1 for Counsellor")
        print("2 for Faculty")
        print("3 for Student")
        print("4 to Exit") 
        roll_id = input("Enter a role id: ")

        if roll_id == '1':
            log_file("Counsellor logged in")
            counsellor_menu()
        elif roll_id == '2':
            log_file("Faculty logged in")
            faculty_menu()
        elif roll_id == '3':
            log_file("Student Activity")
            student_menu()
        elif roll_id == '4':
            log_file("Program Terminated")
            exit()
        else:   
            print("Invalid role ID. Please enter a valid option!")

# Calling Main function.
main_menu()