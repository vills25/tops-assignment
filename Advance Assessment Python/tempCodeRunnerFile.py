import mysql.connector
from datetime import date

db = mysql.connector.connect(host='127.0.0.1', username='root', password='root', database='pharmacy_assessment')
cursor = db.cursor()

def create_tables():
    cursor.execute("DROP TABLE IF EXISTS medicines")