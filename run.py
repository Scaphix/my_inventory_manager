from colorama import Fore, Back, Style


class Item:
    """Represents a single item in the inventory."""
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price


class Inventory:
    """Manages a list of Item objects."""
    def __init__(self):
        self.items = []

    def add_item(self):
        id = input("Enter item ID: ").strip()
        name = input("Enter item name: ").strip()
        quantity = input("Enter item quantity: ").strip()
        price = input("Enter item price: $").strip()

        new_item = Item(id, name, quantity, price)
        self.items.append(new_item)
        print(Fore.GREEN + "\n Item added successfully!" + Style.RESET_ALL)
        
    def display_item(self):
        """Display all items in the inventory list, sorted by ID"""
        if not self.items:
            print(Fore.YELLOW + "\n No items in the inventory!" + Style.RESET_ALL)
            return

        # Sorting the list of dictionaries by the 'id' key
        sorted_items = sorted(self.items, key=lambda item: item.id)

        print("Loading items....\n")
        print(Back.CYAN + Fore.BLACK + "\n  Inventory List" + Style.RESET_ALL)
        print("-" * 40)
        for i, item in enumerate(sorted_items, start=1):
            print(Fore.MAGENTA + f"Item: {item.id}" + Style.RESET_ALL)
            print(f"  Name: {item.name}")
            print(f"  Quantity: {item.quantity}")
            print(f"  Price: ${item.price}")
            print("-" * 40)

        print(Fore.GREEN + " End of inventory list\n" + Style.RESET_ALL)


inventory = Inventory()


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
        while True:
            inventory.add_item()
            more = input("Add another item? (y/n:) ").strip().lower()
            if more != "y":
                break

    elif selected_task == "2":
        print("Update Item to the list")

    elif selected_task == "3":
        inventory.display_item()

    elif selected_task == "4":
        print("delete Item to the list")

    elif selected_task == "5":
        print(" Exiting the program .... Goodbye !")
        return False
    else:
        print("Invalid selection. Please choose 1-5.")
    return True


task = tasks_list()
