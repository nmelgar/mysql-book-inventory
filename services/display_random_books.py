import sys
import os
import random

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.db_conn import get_db_connection


def display_random_books():
    booksdb = get_db_connection()
    dbcursor = booksdb.cursor()

    print(
        "\n\n|---------------------------------------------|\n|------------ Random Books -------------------|\n|---------------------------------------------|\n"
    )

    # Query to get 5 random books
    dbcursor.execute(
        "SELECT id, isbn13, title, author FROM books ORDER BY RAND() LIMIT 5"
    )
    books = dbcursor.fetchall()

    if books:
        print("\n|-- Here are 5 random books from the database --|\n")
        for id, book in enumerate(books, start=1):
            print(
                f"{id}. {book[2]} by {book[3]} (ISBN-13: {book[1]})"
            )  # Corrected indexes

        print("\nThese are amazing books!")
        print("\n")

    else:
        print("\nNo books found in the database.")

    dbcursor.close()
    booksdb.close()
