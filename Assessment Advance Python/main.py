from dbconnection import db, cursor
from tables import create_tables
from admin import admin_login, admin_menu, admin_register
from manager import manager_menu

# Main function controlling the flow of the program
def main():
    create_tables()

    while True:
        print("\nWelcome!")
        print("Select User Type:")
        print("1. Admin")
        print("2. Admin Register")
        print("3. Manager")
        print("4. Exit")
        user_type = input("Press '1' for Admin, '2' for Admin Register, '3' for Manager, '4' for Exit: ")

        if user_type == '1':
            admin_data = admin_login()
            if admin_data:
                print("Login successful.")
                admin_menu()
            else:
                print("Invalid admin credentials.Please try again!!")
        elif user_type == '2':
            admin_register()
        elif user_type == '3':
            manager_menu()    
        elif user_type == '4':
            break
        else:
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    try:
        main()
    finally:
        cursor.close()
        db.close()            