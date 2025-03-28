import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.db_conn import get_db_connection

booksdb = get_db_connection()
dbcursor = booksdb.cursor()

sql = "INSERT INTO books (isbn13, isbn10, title, author) VALUES (%s, %s, %s, %s)"
val = ("test", "test", "test", "test")
dbcursor.execute(sql, val)

booksdb.commit()

print(dbcursor.rowcount, "record inserted.")
