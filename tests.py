def show_menu():
    menu_options = ["Search","Add book", "Edit book", "Delete Book", "Exit"]
    counter = 1
    for item in menu_options:
        print(f"{counter}. {item}")
        counter += 1

show_menu()