import mysql.connector

# Establishing connection to the MySQL database
db = mysql.connector.connect(host='127.0.0.1', username='root', password='root', database='pharmacy_assessment')
cursor = db.cursor()

