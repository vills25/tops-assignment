from dbconnection import db, cursor

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
    """, (username, password))
  
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