from dbconnection import cursor

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