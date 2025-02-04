import db_conn


def action_input():
    """Based on user's choice determine what to do"""
    user_input = input("What would you like to do? (Choose a number) ")
    return user_input


def menu_items():
    """Display menu of available options for the system"""


def main():
    """The main entry point of the program."""
    # connection to db
    dbcursor = db_conn.booksdb.cursor()

    # print welcome message
    print(
        "\n|---------------------------------------------|\n|--- Welcome to the book management system ---|\n|---------------------------------------------|"
    )

    action_input()


if __name__ == "__main__":
    main()
