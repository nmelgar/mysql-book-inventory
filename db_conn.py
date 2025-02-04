import mysql.connector
import db_info

booksdb = mysql.connector.connect(
  host=db_info.HOST,
  user=db_info.USER,
  password=db_info.PASSWORD,
  database="seilagun_books"
)

# print(booksdb)