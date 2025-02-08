import db.db_conn as db_conn
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# mydb = db_conn.get_db_connection()
# mycursor = mydb.cursor()

def add_book():
    print("add book")