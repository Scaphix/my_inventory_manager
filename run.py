from colorama import Fore, Back, Style
from inventory import Inventory


inventory = Inventory()


def tasks_list():
    """Display the menu and handle user input"""
    program_running = True
    while program_running:
        print(Back.BLUE + "\n Welcome to the Inventory Managment tool\n")
        print(Style.RESET_ALL)
        print(
            "This tool helps you easily manage your stock-"
            "add, view, update, or delete items using their ID.\n"
            "Follow the prompts on screen to perform any action "
            "and keep your inventory up to date.\n"
            )
        print("-" * 40)
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
        print("\033c", end="")
        print(Fore.BLUE + Style.BRIGHT + "\n--- Add a New Item ---")
        print(Style.RESET_ALL)
        while True:
            inventory.add_item()
            more = input("Add another item? (y/n:) ").strip().lower()
            if more != "y":
                break

    elif selected_task == "2":
        inventory.update_item()

    elif selected_task == "3":
        print("\033c", end="")
        inventory.display_item()

    elif selected_task == "4":
        print("Please enter the name of the item to delete ")
        name_to_delete = input("Enter Name: ").strip()
        inventory.delete_item(name_to_delete)

    elif selected_task == "5":
        print(" Exiting the program .... Goodbye !")
        return False
    else:
        print("Invalid selection. Please choose 1-5.")
    return True


task = tasks_list()
