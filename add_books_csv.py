import db_conn

dbcursor = db_conn.booksdb.cursor()

# display available tables
# dbcursor.execute("SHOW TABLES")
# for x in dbcursor:
#     print(x)

sql = "INSERT INTO books (isbn13, isbn10, title, author) VALUES (%s, %s, %s, %s)"
val = ("test", "test", "test", "test")
dbcursor.execute(sql, val)

db_conn.booksdb.commit()

print(dbcursor.rowcount, "record inserted.")
