import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="stone12",
    database="classicmodels",
    port=3306

)
if(connection.is_connected()):
    print("yipeee!!! DB is connected o!")
else:
    print("DB could not be connected")