import services.add_book as add_book
import services.edit_book as edit_book
import services.delete_book as delete_book
import menu.action_input as action_input


def take_action(action_input):
    """This function will decide which action to perform based on users input"""
    if action_input == 1:
        add_book.add_book()
    elif action_input == 2:
        edit_book.edit_book()
    elif action_input == 3:
        delete_book.delete_book()
    elif action_input == 5:
        return False

    return True
