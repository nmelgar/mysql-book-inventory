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


mydb = get_db_connection()
mycursor = mydb.cursor()

# sql = "INSERT INTO books (isbn13, isbn10, title, author) VALUES (%s, %s, %s, %s)"
# val = ("test", "test", "test", "test")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

books_columns = [
    "isbn13",
    "isbn10",
    "subtitle",
    "author",
    "category",
    "thumbnail",
    "description",
    "published_year",
    "average_rating",
    "num_pages",
    "ratings_count",
]
