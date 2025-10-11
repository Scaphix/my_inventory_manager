import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style
from inventory import Inventory


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('inventory')

# sales = SHEET.worksheet('sheet')
# data = sales.get_all_values()

# print(data)


inventory = Inventory()


def main():
    """
    Welcome Message
    """
    # Clear the console when the program starts
    print("\033c", end="")
    print(Back.BLUE + "\n Welcome to the Inventory Managment tool\n"
          + Style.RESET_ALL
          )
    print(
            "This tool helps you easily manage your stock-"
            "add, view, update, or delete items using their ID.\n"
            "Follow the prompts on screen to perform any action "
            "and keep your inventory up to date.\n"
            )
    print("-" * 40)


def tasks_list():
    """Display the menu and handle user input"""
    program_running = True
    while program_running:
        print("\nPlease select one of the following tasks:")
        print("-" * 38)
        print(Fore.BLUE + Style.BRIGHT + """
        [1] Add item
        [2] Update item
        [3] Display item
        [4] Delete item
        [5] EXIT\n""" + Style.RESET_ALL)
        selected_task = Inventory.get_valid_int("Select task: ")
        print(f"your selection is: {selected_task}")
        go_on = my_task(selected_task)
        if not go_on:
            break


def my_task(selected_task):
    """
    Task or choice manager,
    each number chosen will excecute the corresponding method
    """
    if selected_task == 1:
        print("\033c", end="")
        print(Fore.BLUE + Style.BRIGHT + "\n--- Add a New Item ---"
              + Style.RESET_ALL)
        while True:
            inventory.add_item()
            more = input("Add another item? (y/n:) ").strip().lower()
            if more != "y":
                break

    elif selected_task == 2:
        print(Fore.BLUE + Style.BRIGHT + "\n--- Update an existing Item ---"
              + Style.RESET_ALL)
        inventory.update_item()

    elif selected_task == 3:
        print("\033c", end="")
        inventory.display_item()

    elif selected_task == 4:
        print(Fore.BLUE + Style.BRIGHT + "\n--- Delete an existing Item ---"
              + Style.RESET_ALL)
        print("Please enter the ID of the item to delete ")
        try:
            id_to_delete = int(input("Enter ID: ").strip())
            inventory.delete_item(id_to_delete)
        except ValueError:
            print(Fore.RED + "Invalid ID! Please enter a number.")
            print(Style.RESET_ALL)

    elif selected_task == 5:
        print(" Exiting the program .... Goodbye !")
        return False
    else:
        print(Fore.RED + "Invalid selection. Please choose 1-5."
              + Style.RESET_ALL)
    return True


"""
This loop introduces a main() entry point to ensure the welcome
message only runs when the script is executed directly,
improving clarity and structure:
main() runs once at program start
task_list() starts the interactive menu
"""
if __name__ == "__main__":
    main()
    tasks_list()
