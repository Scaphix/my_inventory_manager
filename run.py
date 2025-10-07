from colorama import Fore, Back, Style

"""
Wecome function
"""


def tasks_list():
    program_running = True
    while program_running:
        print(Back.BLUE + "Welcome to the Inventory Managment tool")
        print(Style.RESET_ALL)
        print("---------------------------------------")
        print("Please select one of the following tasks:\n")
        print(Fore.MAGENTA + "[1] Add item")
        print("[2] Update item")
        print("[3] Display item")
        print("[4] Delete item")
        print("[5] EXIT\n")
        print(Style.RESET_ALL)
        selected_task = input("Select task : ")
        print(f"your selection is: {selected_task}")
        go_on = my_task(selected_task)
        if go_on is False:
            break


def my_task(selected_task):
    if selected_task == "1":
        add_item()

    elif selected_task == "2":
        update_item()

    elif selected_task == "3":
        display_item()

    elif selected_task == "4":
        delete_item()

    elif selected_task == "5":
        print(" Exiting the program .... Goodbye !")
        return False
    else:
        print("Invalid selection. Please choose 1-5.")
    return True


def add_item():
    my_file = []
    print("Add Item to the list")
    item = input("What is the name of the item: ")
    my_file.append(item)
    print(my_file)


def update_item():
    print("Update Item to the list")


def display_item():
    print("display Item to the list")


def delete_item():
    print("delete Item to the list")


task = tasks_list()