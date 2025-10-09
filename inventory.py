from colorama import Fore, Back, Style
from item import Item


class Inventory:
    """
    Manages a collection of items in the inventory.

    The Inventory class acts as a container and controller for all items.
    It allows adding, displaying, updating, and deleting products,
    as well as saving and loading them (eventually from JSON or Google Sheets).

    This separation of logic (Inventory vs. Item) makes the program
    easier to maintain and scale.

    Attributes:
        items (list): A list that stores all Item objects in the inventory.
    """
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
            print(Fore.YELLOW + "\n empty inventory!" + Style.RESET_ALL)
            return

        # Sorting the list of dictionaries by the 'id' key
        sorted_items = sorted(self.items, key=lambda item: item.id)

        print("Loading items....\n")
        print(Back.MAGENTA + "=== INVENTORY LIST ===" + Style.RESET_ALL)
        print("-" * 40)
        for i, item in enumerate(sorted_items, start=1):
            print(item)
            print("-" * 40)
        print(Fore.GREEN + " End of inventory list\n" + Style.RESET_ALL)

    def delete_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(Fore.GREEN + f" {name} deleted successfully.")
                print(Style.RESET_ALL)
                return
        print(Fore.RED + f" {name} not found." + Style.RESET_ALL)
