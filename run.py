from colorama import Fore, Back, Style


def tasks_list():
    """Wecome function"""
    program_running = True
    while program_running:
        print(Back.BLUE + "\n Welcome to the Inventory Managment tool")
        print(Style.RESET_ALL)
        print("---------------------------------------")
        print("Please select one of the following tasks:\n")
        print(Fore.MAGENTA + "[1] Add item")
        print("[2] Update item")
        print("[3] Display item")
        print("[4] Delete item")
        print("[5] EXIT\n" + Style.RESET_ALL)
        selected_task = input("Select task : ")
        print(f"your selection is: {selected_task}")
        go_on = my_task(selected_task)
        if not go_on:
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
    items = []
    """Add a new item to the global list"""
    id = input("Enter item ID: ").strip()
    name = input("Enter item name: ").strip()
    description = input("Enter item description: ").strip()
    price = input("Enter item price: $").strip()

    my_item = [id, name, description, price]
    items.append(my_item)
    print(Fore.GREEN + "\n Item added successfully!" + Style.RESET_ALL)
    print(f"[{id}] - {name} - {description} - ${price}")


def update_item():
    print("Update Item to the list")


def display_item():
    print("display Item to the list")


def delete_item():
    print("delete Item to the list")


task = tasks_list()
