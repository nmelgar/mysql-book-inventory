import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.db_conn import get_db_connection


def delete_book():
    booksdb = get_db_connection()
    dbcursor = booksdb.cursor()
    print(
        "\n\n|---------------------------------------------|\n|-------------- Delete Book ------------------|\n|---------------------------------------------|\n"
    )

    print("\n|-- Enter the ISBN of the book to delete --|")
    print("|------(R) = Required information ---------|")
    print("|------------------------------------------|")

    # ask user for isbn number
    isbn = input("Enter ISBN-13 or ISBN-10 of the book to delete (R): ")

    # check if book exists
    dbcursor.execute(
        "SELECT * FROM books WHERE isbn13 = %s OR isbn10 = %s", (isbn, isbn)
    )
    book = dbcursor.fetchone()

    if book:
        confirm = (
            input(
                f"Are you sure you want to delete '{book[3]}' by {book[5]}? (yes/no): "
            )
            .strip()
            .lower()
        )
        if confirm == "yes":
            dbcursor.execute(
                "DELETE FROM books WHERE isbn13 = %s OR isbn10 = %s", (isbn, isbn)
            )
            booksdb.commit()
            print("\nBook deleted successfully.")
        else:
            print("\nDeletion canceled.")
    else:
        print("\nNo book found with the given ISBN.")

    dbcursor.close()
    booksdb.close()
