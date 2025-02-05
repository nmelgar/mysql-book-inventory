import mysql.connector
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db import db_info


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user=db_info.LOCAL_USER,
        password=db_info.LOCAL_PASSWORD,
        database="books",
    )

print(get_db_connection())

mydb = get_db_connection()
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
