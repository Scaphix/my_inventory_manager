from colorama import Fore, Back, Style
from item import Item


def check_inventory_not_empty(func):
    """Decorator to skip method if inventory is empty."""
    def wrapper(self, *args, **kwargs):
        if not self.items:
            print(Fore.YELLOW + "\n Empty inventory!" + Style.RESET_ALL)
            return
        return func(self, *args, **kwargs)
    return wrapper


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

    @staticmethod
    def get_valid_int(prompt):
        """Ask repeatedly until a valid number is entered."""
        while True:
            try:
                value = int(input(prompt).strip())
                return value
            except ValueError:
                print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
                print(" Please enter a number.")

    @staticmethod
    def get_valid_float(prompt):
        """Keep asking until a valid float is entered. For Price"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print(Fore.RED + "Please enter a valid number (e.g. 12.50).")
                print("e.g. 12.50" + Style.RESET_ALL)

    def get_id(self):
        while True:
            id = self.get_valid_int("Enter item ID: ")
            if any(item.id == id for item in self.items):
                print(Fore.RED + f"Error: ID {id} already exists.")
                print("Please use a unique ID." + Style.RESET_ALL)
                break
            return id

    def add_item(self):
        id = self.get_id()
        name = input("Enter item name: ")
        quantity = self.get_valid_int("Enter item quantity: ")
        price = self.get_valid_float("Enter item price: $")

        new_item = Item(id, name, quantity, price)
        self.items.append(new_item)
        print(Fore.GREEN + "\n Item added successfully!" + Style.RESET_ALL)

    @check_inventory_not_empty
    def display_item(self):
        """Display all items in the inventory list, sorted by ID"""
        if not self.items:
            print(Fore.YELLOW + "\n empty inventory!" + Style.RESET_ALL)
            return

        # Sorting the list of dictionaries by the 'id' key
        sorted_items = sorted(self.items, key=lambda item: item.id)

        print("Loading items....\n")
        print(Back.MAGENTA + "=" * 13 + "INVENTORY LIST" + "=" * 13)
        print(Style.RESET_ALL)
        print("-" * 40)
        for i, item in enumerate(sorted_items, start=1):
            print(item)
            print("-" * 40)
        print(Fore.GREEN + " End of inventory list\n" + Style.RESET_ALL)

    @check_inventory_not_empty
    def delete_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(Fore.GREEN + f" {name} deleted successfully.")
                print(Style.RESET_ALL)
                return
        print(Fore.RED + f" {name} not found." + Style.RESET_ALL)

    @check_inventory_not_empty
    def update_item(self):
        """Update an existing item"""
        item_id = input("Enter ID to update: ").strip()
        for item in self.items:
            if item.id == item_id:
                print("Please inter the new item")
                new_name = input("Enter the new Name: ")
                new_qty = Inventory.get_valid_int("Enter the new Quantity: ")
                new_price = Inventory.get_valid_int("Enter the new Price: ")
                item.name = new_name
                item.price = new_price
                item.quantity = new_qty
                print("\nItem updating...\n")
                print(Fore.GREEN + "Item updated successfully!")
                print(Style.RESET_ALL)
                return
        print(Fore.RED + "Item not found." + Style.RESET_ALL)
