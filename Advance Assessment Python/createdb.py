import dbconnection

db_name = input("Enter database name : ")
dbconnection.mycursor.execute(f'create database {db_name}')


