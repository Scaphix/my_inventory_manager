"""
Wecome function
"""
def tasks_list():
    print("Welcome to the Inventory Managment tool\n")
    print("Please select one of the following tasks:\n")
    print("[1] Add item")
    print("[2] Update item")
    print("[3] Display item")
    print("[4] Delete item")
    selected_task = input("Select task : ")
    print(f"your selection is: {selected_task}")
 
    return selected_task   


def my_task(selected_task):
    if selected_task == "1":
        add_item()

    elif selected_task == "2":
       update_item()

    elif selected_task == "3":
        display_item()

    elif selected_task == "4":
        delete_item()

    else:
        print("Invalid selection. Please choose 1-4.")


def add_item():
    print("Update Item to the list")
   

def update_item():
    print("Update Item to the list")


def display_item():
    print("display Item to the list")


def delete_item():
    print("delete Item to the list")


task = welcome_lines()

my_task(task)


