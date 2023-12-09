import mysql.connector as connector

# Connect to MySQL database

def mysqlCursor():
    db = connector.connect(
        host="localhost",
        user="root",
        password="devilroot10",
        database="project"
    )
    cursor = db.cursor()
    return cursor, db

