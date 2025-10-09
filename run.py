from colorama import Fore, Back, Style
from inventory import Inventory

inventory = Inventory()


def tasks_list():
    """Display the menu and handle user input"""
    program_running = True
    while program_running:
        print(Back.BLUE + "\n Welcome to the Inventory Managment tool")
        print(Style.RESET_ALL)
        print("---------------------------------------")
        print("Please select one of the following tasks:\n")
        print(Fore.BLUE + Style.BRIGHT + "[1] Add item")
        print("[2] Update item")
        print("[3] Display item")
        print("[4] Delete item")
        print("[5] EXIT\n" + Style.RESET_ALL)
        selected_task = input("Select task : ").strip()
        print(f"your selection is: {selected_task}")
        go_on = my_task(selected_task)
        if not go_on:
            break


def my_task(selected_task):
    if selected_task == "1":
        while True:
            inventory.add_item()
            more = input("Add another item? (y/n:) ").strip().lower()
            if more != "y":
                break

    elif selected_task == "2":
        inventory.update_item()

    elif selected_task == "3":
        inventory.display_item()

    elif selected_task == "4":
        name = input("Which item do you want to remove? ")
        inventory.delete_item(name)

    elif selected_task == "5":
        print(" Exiting the program .... Goodbye !")
        return False
    else:
        print("Invalid selection. Please choose 1-5.")
    return True


task = tasks_list()
