import db.db_conn as db_conn
import menu.menu as menu


def action_input():
    """Based on user's choice determine what to do"""
    user_input = input("What would you like to do? (Choose a number) ")
    return user_input


def main():
    """The main entry point of the program."""
    # connection to db
    dbcursor = db_conn.booksdb.cursor()

    # print welcome message
    print(
        "\n\n|---------------------------------------------|\n|--- Welcome to the book management system ---|\n|---------------------------------------------|\n"
    )
    # display main menu
    menu.show_menu()
    action_input()


if __name__ == "__main__":
    main()
