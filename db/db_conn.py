import mysql.connector
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db import db_info

# remote database
# booksdb = mysql.connector.connect(
#   host=db_info.HOST,
#   user=db_info.USER,
#   password=db_info.PASSWORD,
#   database="seilagun_books"
# )


# local database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user=db_info.LOCAL_USER,
        password=db_info.LOCAL_PASSWORD,
        database="books",
    )