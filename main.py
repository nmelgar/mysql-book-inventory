import db.db_conn as db_conn
import menu.menu as menu
import menu.action_input as action_input
import services.take_action as take_action


def main():
    """The main entry point of the program."""
    # print welcome message
    print(
        "\n\n|---------------------------------------------|\n|--- Welcome to the book management system ---|\n|---------------------------------------------|\n"
    )
    run = True
    while run:
        # display main menu
        menu.show_menu()
        # users input for actions
        action_number = action_input.action_input()
        # take_action.take_action(action_number)
        # stop the program when user chooses 5
        run = take_action.take_action(action_number)


if __name__ == "__main__":
    main()
