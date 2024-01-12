from dbconnection import db, cursor
from admin import view_all_medicines
from datetime import date

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

# Function to validate manager login
def manager_login():
    username = input("Enter manager username: ")
    password = input("Enter manager password: ")

    cursor.execute("""
        SELECT * FROM users WHERE username = %s AND password = %s AND role = 'manager'
    """, (username, password))

    result = cursor.fetchone()
    return result

# Function to add a new medicine to the inventory
def add_medicine():
    name = input("Enter medicine name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    added_date = date.today().strftime("%Y-%m-%d")
    added_by = "Manager" 

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