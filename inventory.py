from colorama import Fore, Back, Style
from item import Item
import re


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
    def __init__(self, worksheet):
        self.worksheet = worksheet
        self.items = []

    @staticmethod
    def get_valid_int(prompt):
        """Ask repeatedly until a valid number is entered."""
        while True:
            try:
                value = int(input(prompt).strip())
                if value < 0:
                    print(Fore.RED + "Negative numbers are not allowed!"
                          + Style.RESET_ALL)
                    print("Please enter a positive number.")
                    continue
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
        """Check duplicates: The Item ID must be unique"""
        while True:
            id = self.get_valid_int("Enter item ID: ")
            if any(item.id == id for item in self.items):
                print(Fore.RED + f"Error: ID {id} already exists.")
                print("Please use a unique ID." + Style.RESET_ALL)
                continue
            return id

    def get_name(self):
        """
        Apply diffent checks on name input:
          -Empty input check
          -Input must contain at least 3 letters (not just symbols or digits)
          -The total length (3-15 characters)
          -Duplicates: The Item Name must be unique
        """
        while True:
            name = input("Enter item name:").strip()
            # Checks for empty input
            if not name:
                print(Fore.RED + "Error: Name cannot be empty."
                      + Style.RESET_ALL)
                continue
            # Combined length and letter count check
            letter_count = len(re.findall(r"[A-Za-z]", name))
            if len(name) < 3 or len(name) > 15 or letter_count < 3:
                if len(name) < 3 or len(name) > 15:
                    print(Fore.RED +
                          "Error: Name must be between 3 - 15 characters long."
                          + Style.RESET_ALL)
                if letter_count < 3:
                    print(Fore.RED +
                          "Error: Name must contain at least 3 letters."
                          + Style.RESET_ALL)
                continue
            # Checks for duplicates
            if any(item.name.lower() == name.lower() for item in self.items):
                print(Fore.RED + f"Error: '{name}' already exists.")
                print("Please use a different name." + Style.RESET_ALL)
                continue
            return name

    def add_item(self):
        """ Add new Items to the inventory """
        id = self.get_id()
        name = self.get_name()
        quantity = self.get_valid_int("Enter item quantity: ")
        price = self.get_valid_float("Enter item price: $")

        new_item = Item(id, name, quantity, price)
        print(new_item)
        self.items.append(new_item)
        self.save_to_sheet(new_item)
        print(Fore.GREEN + "\n Item added successfully!" + Style.RESET_ALL)

    def display_item(self):
        """Display all items in the inventory list, sorted by ID"""
        if not self.items:
            print(Fore.YELLOW + "\n empty inventory!" + Style.RESET_ALL)
            return

        # Sorting the list of dictionaries by the 'id' key
        sorted_items = sorted(self.items, key=lambda item: item.id)

        print("Loading items....\n")
        print(Back.MAGENTA + "=" * 12 + "INVENTORY LIST" + "=" * 12)
        print(Style.RESET_ALL)
        print("-" * 38)
        print(f"{'ID':<2} | {'Name':<10} | {'Qty':>4} | {'Price':>5}")
        print("-" * 38)
        for i, item in enumerate(sorted_items, start=1):
            print(item)
            print("-" * 38)
        print(Fore.GREEN + " End of inventory list\n" + Style.RESET_ALL)

    @check_inventory_not_empty
    def delete_item(self, id):
        """Delete the chosen Item """
        for item in self.items:
            if item.id == id:
                delete = input(
                    f"Are you sure you want to delete item {id} ? (y/n:)"
                    ).strip().lower()
                if delete == "y":
                    self.items.remove(item)
                    print(Fore.GREEN + f" item {id} deleted successfully.")
                    print(Style.RESET_ALL)
                    return
                elif delete == "n":
                    print(Fore.YELLOW + " Deletion cancelled.")
                    print(Style.RESET_ALL)
                    return
                else:
                    print(Fore.RED + " Invalid input. Deletion cancelled.")
                    print(Style.RESET_ALL)
                    return
        print(Fore.RED + f" {id} not found." + Style.RESET_ALL)

    @check_inventory_not_empty
    def update_item(self):
        """Update an existing item"""
        try:
            item_id = int(input("Enter ID to update: ").strip())
        except ValueError:
            print(Fore.RED + "Invalid ID!")
            print("Please enter a number." + Style.RESET_ALL)
            return

        for item in self.items:
            if item.id == item_id:
                print("Please inter the new item")
                new_name = self.get_name()
                new_qty = self.get_valid_int("Enter the new Quantity: ")
                new_price = self.get_valid_float("Enter the new Price: ")
                item.name = new_name
                item.price = new_price
                item.quantity = new_qty
                print("\nItem updating...\n")
                print(Fore.GREEN + "Item updated successfully!")
                print(Style.RESET_ALL)
                return
        print(Fore.RED + "Item not found." + Style.RESET_ALL)

    def save_to_sheet(self, item):
        """
        Saves a new item to the Google Sheet.
        """
        try:
            self.worksheet.append_row([
                item.id,
                item.name,
                item.quantity,
                item.price
            ])
            print(Fore.GREEN + "Item successfully saved to Google Sheet!"
                  + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error saving to Google Sheet: {e}"
                  + Style.RESET_ALL)
