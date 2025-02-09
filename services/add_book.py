import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.db_conn import get_db_connection


def add_book():
    booksdb = get_db_connection()
    dbcursor = booksdb.cursor()
    print(
        "\n\n|---------------------------------------------|\n|---------------- Add Book -------------------|\n|---------------------------------------------|\n"
    )
    print("\n|-- Add the information for the book --|")
    print("|------(R) = Required information -----|")
    print("|--------------------------------------|")

    # information to be inserted
    book_name = input("Book name (R): ")
    isbn13 = input("ISBN13 (R): ")
    isbn10 = input("ISBN10 (R): ")
    author = input("Author (R): ")

    sql = "INSERT INTO books (isbn13, isbn10, title, author) VALUES (%s, %s, %s, %s)"
    val = (isbn13, isbn10, book_name, author)
    dbcursor.execute(sql, val)

    booksdb.commit()

    print(dbcursor.rowcount, "\nBook succesfully.")
