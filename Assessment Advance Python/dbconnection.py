import mysql.connector
from datetime import date

# Establishing connection to the MySQL database
db = mysql.connector.connect(host='127.0.0.1', username='root', password='root', database='pharmacy_assessment')
cursor = db.cursor()

# Function to create necessary tables in the database if they don't exist
def create_tables():
    
    # Creating table for users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            sr_no INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255),
            role VARCHAR(50)
        )
    """)
    # Creating table for medicines
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicines (
            sr_no INT AUTO_INCREMENT PRIMARY KEY,
            medicine_name VARCHAR(255),
            quantity INT,
            added_date DATE,
            added_by VARCHAR(255),
            price FLOAT
        )
    """)
    # Creating table for managers
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS managers (
            sr_no INT AUTO_INCREMENT PRIMARY KEY,
            manager_name VARCHAR(255),
            pharmacy_name VARCHAR(255)
        )
    """)

#Function to register admin users in the database
def admin_register():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    cursor.execute("""
        INSERT INTO users (username, password, role) VALUES (%s, %s, 'admin')
    """, (username, password))
    db.commit()
    print("Admin registration successful.")

# Function to validate admin login
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    cursor.execute("""
        SELECT * FROM users WHERE username = %s AND password = %s AND role = 'admin'
  myvenv  """, (username, password))
  
    result = cursor.fetchone()
    return result    

# Function to view all managers in the database
def view_all_managers():
    cursor.execute("SELECT * FROM managers")
    managers = cursor.fetchall()

    print("All Managers:")
    print("ID\tManager Name\tPharmacy Name")
    for manager in managers:
        print(f"{manager[0]}\t{manager[1]}\t\t{manager[2]}")

# Function to view all medicines in the inventory
def view_all_medicines():
    cursor.execute("SELECT * FROM medicines")
    medicines = cursor.fetchall()

    print("Medicine Inventory:")
    print("ID\tName\t\tQuantity\tAdded Date\tAdded By\tPrice")
    for medicine in medicines:
        print(f"{medicine[0]}\t{medicine[1]}\t{medicine[2]}\t\t{medicine[3]}\t{medicine[4]}\t\t{medicine[5]}")

# Function to register pharmacy managers in the database
def manager_register():
    username = input("Enter manager username: ")
    password = input("Enter manager password: ")
    pharmacy_name = input("Enter pharmacy name: ")

    cursor.execute("""
        INSERT INTO managers (manager_name, pharmacy_name) VALUES (%s, %s)
    """, (username, pharmacy_name)) 
    db.commit()
    print("Manager registration successful.")

# Function to add a new medicine to the inventory
def add_medicine():
    name = input("Enter medicine name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    added_date = date.today().strftime("%Y-%m-%d")
    added_by = "Admin" 

    cursor.execute("""
        INSERT INTO medicines (medicine_name, quantity, added_date, added_by, price) VALUES (%s, %s, %s, %s, %s)
    """, (name, quantity, added_date, added_by, price))

    db.commit()
    print("Medicine added successfully.")

# Function to delete a medicine from the inventory
def delete_medicine():
    view_all_medicines()
    medicine_id = int(input("Enter the ID of the medicine to delete: "))
    confirm = input("Are you sure you want to delete this medicine? (Y/N): ").upper()

    if confirm == 'Y':
        cursor.execute("DELETE FROM medicines WHERE sr_no = %s", (medicine_id,))
        db.commit()
        print("Medicine deleted successfully.")
    else:
        print("Deletion canceled.")


# Function to validate manager login
def manager_login():
    username = input("Enter manager username: ")
    password = input("Enter manager password: ")

    cursor.execute("""
        SELECT * FROM users WHERE username = %s AND password = %s AND role = 'manager'
    """, (username, password))

    result = cursor.fetchone()
    return result

# Admin menu handling various admin operations
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Register Admin")
        print("2. View All Managers")
        print("3. View All Medicines")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            admin_register()
            print("Admin registration confirmed.")
        elif choice == '2':
            view_all_managers()
        elif choice == '3':
            view_all_medicines()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Manager menu handling various manager operations
def manager_menu():
    while True:
        print("\nPharmacy Manager Menu:")
        print("1. Register Manager")
        print("2. Login")
        print("3. Add Medicine")
        print("4. View Medicine")
        print("5. Delete Medicine")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manager_register()
            print("Manager registration confirmed.")
        elif choice == '2':
            manager_data = manager_login()
            if manager_data:
                print("Login successful.")
                while True:
                    print("\nManager Actions:")
                    print("1. Add Medicine")
                    print("2. View Medicine")
                    print("3. Delete Medicine")
                    print("4. Logout")
                    action = input("Enter your action: ")

                    if action == '1':
                        add_medicine()
                    elif action == '2':
                        view_all_medicines()
                    elif action == '3': 
                        delete_medicine()
                    elif action == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid action. Please try again.")
            else:
                print("Invalid username or password.")
        elif choice == '3':
            add_medicine()
            print("Medicine added.")
        elif choice == '4':
            view_all_medicines()
        elif choice == '5':
            delete_medicine()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

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
