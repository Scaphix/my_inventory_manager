# [my_inventory_manager](https://my-inventory-manager-17f3f6d5a838.herokuapp.com)

Developer: Chahinez Boutemine ([Scaphix](https://www.github.com/Scaphix))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Scaphix/my_inventory_manager)](https://www.github.com/Scaphix/my_inventory_manager/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Scaphix/my_inventory_manager)](https://www.github.com/Scaphix/my_inventory_manager/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Scaphix/my_inventory_manager)](https://www.github.com/Scaphix/my_inventory_manager)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://my-inventory-manager-17f3f6d5a838.herokuapp.com)

The Inventory Management Tool is a simple, Python-based command-line application designed to help small businesses keep track of their stock efficiently. It allows users to add, update, delete, and display items with clear, color-coded feedback in the terminal. The idea for this project came from my own experience working in my family’s business, where I realized we lacked an organized way to manage inventory. I always wanted to create a tool that could make this process easier, and learning Python gave me the opportunity to finally build it myself.


![screenshot](document/mockup.png)


## UX


**Purpose**
- Provide users with a simple and effective way to track inventory levels and manage products directly from the terminal.
- Help small business owners maintain accurate records of their stock, reduce manual errors, and make informed decisions about restocking or pricing.


**Primary User Needs**
- Easily add, update, delete, and view items in the inventory.
- Keep track of product quantities and prices with minimal technical knowledge.
- Store data safely in Google Sheets for persistent storage and easy access across sessions.
- Receive clear and user-friendly feedback through color-coded messages in the terminal.

**Business Goals**
- Offer a lightweight, reliable, and cost-free tool to manage inventory without requiring advanced software.
- Help businesses save time, avoid stock shortages or overstocking, and maintain up-to-date records.
- Support better organization and customer satisfaction by ensuring that stock information is always accurate and easy to access.



## User Stories


| Target    | Expectation                                                                 | Outcome                                                                                |
| ----------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| As a user | I would like to add new items to my inventory with unique IDs and names     | so that I can track each product individually without confusion.                       |
| As a user | I would like to update existing items (name, quantity, price)               | so that I can keep my inventory information current as stock levels and prices change. |
| As a user | I would like to delete items from my inventory with a confirmation prompt   | so that I can remove discontinued products while avoiding accidental deletions.        |
| As a user | I would like to view all items in a sorted, formatted table                 | so that I can easily see my complete inventory at a glance.                            |
| As a user | I would like the application to validate my input (IDs, quantities, prices) | so that I don't accidentally enter invalid data that could corrupt my records.         |
| As a user | I would like to see color-coded feedback for success, errors, and warnings  | so that I can quickly understand the results of my actions.                            |
| As a user | I would like the app to prevent duplicate IDs and names                     | so that each item in my inventory is unique and identifiable.                          |
| As a user | I would like the app to be intuitive with a clear menu system               | so that I can manage my inventory without needing extensive training.                  |

## Features

### Existing Features


| Feature               | Notes                                                                                                                                                                     | Screenshot                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Add Item              | Users can add new items with unique ID and name validation. The system ensures no duplicate IDs or names exist and validates quantity (integer) and price (float) inputs. | ![screenshot](document/add-item.png)         |
| Update Item           | Allows users to modify existing items by ID, updating the name, quantity, and price. Validates all inputs and confirms updates with success messages.                     | ![screenshot](document/update_item.png)      |
| Display Items         | Shows all inventory items in a formatted table sorted by ID, displaying ID, name, quantity, and price in a clear, color-coded layout.                                     | ![screenshot](document/inventory.png)    |
| Delete Item           | Removes items from inventory by ID with a confirmation prompt (y/n) to prevent accidental deletion. Handles invalid responses gracefully.                                 | ![screenshot](document/delete-item.png)      |
| Input Validation      | Validates integer inputs (ID, quantity) and float inputs (price) with retry prompts. Ensures data integrity by rejecting invalid entries with clear error messages.       | ![screenshot](document/input-validation.png) |
| Color-coded Feedback  | Uses colorama to provide visual feedback: green for success, red for errors, yellow for warnings, blue for menu headers, and magenta for section headers.                 | ![screenshot](document/color-feedback.png)   |
| Empty Inventory Check | Decorator pattern prevents update and delete operations on empty inventory, displaying a friendly warning message instead.                                                | ![screenshot](document/empty-check.png)      |
| Menu System           | Interactive menu-driven interface with 5 options (Add, Update, Display, Delete, Exit) that loops until the user chooses to exit.                                          | ![screenshot](document/menu-system.png)      |
| Google Sheets Integration | Automatically loads inventory data from Google Sheets on startup and syncs all add, update, and delete operations to maintain persistent storage across sessions.      | ![screenshot](document/google-sheets.png)    |

### Future Features

- **User Authentication and Role Management**: Implement a login system with roles (e.g., admin, employee) to restrict data access based on user roles.
- **Data Visualization**: Add charts and graphs to visually represent stock levels, value trends, and inventory metrics over time.
- **Search and Filter**: Implement search functionality to find items by name, ID range, or price range, with filtering options.
- **Low Stock Alerts**: Notify users when stock levels fall below a defined threshold, prompting restock orders.
- **Bulk Operations**: Add ability to import/export multiple items at once via CSV files.
- **Transaction History**: Track all add/update/delete operations with timestamps for audit trails.
- **Reporting and Exporting**: Generate and export detailed inventory reports in PDF or CSV format.
- **Category Management**: Organize items into categories (e.g., electronics, food, clothing) for better organization.
- **Mobile App Integration**: Develop a mobile version of the app for easier inventory management on the go.
- **Multi-location Support**: Extend the system to track inventory across multiple warehouse or store locations.
- **Price History**: Track price changes over time to analyze pricing trends and profitability.


## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Google_Sheets-grey?logo=googlesheets&logoColor=34A853)](https://docs.google.com/spreadsheets) | Storing data from my Python app. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Lucidchart-grey?logo=lucid&logoColor=F97B2C)](https://www.lucidchart.com) | Flow diagrams for mapping the app's logic. |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |

## Database Design

### Data Model



#### Classes & Functions


To make the Inventory Management Tool more organised and scalable, I chose to implement an object-oriented structure using two main classes: Item and Inventory. The Item class represents individual products, each with its own attributes such as ID, name, quantity, and price. The Inventory class, on the other hand, manages a collection of these items and provides the functionality to add, display, update, or delete products.

By separating responsibilities, the Item class handles individual product data, while the Inventory class manages the overall collection and business logic.
This object-oriented approach allows me to extend the project later (e.g., connecting to a Google Sheet, adding invoices, or tracking quantities automatically) without rewriting the core functions


```python
class Item:
    """
    Represents a single product or entry in the inventory.

    The Item class is responsible for storing all the details about
    an individual product such as its ID, name, quantity, and price.
    It ensures that each item can be easily managed, updated, and displayed
    as part of the overall inventory.

    Attributes:
        id (str): A unique identifier for the item.
        name (str): The name of the product.
        quantity (int): The available stock quantity.
        price (float): The price per unit of the product.
    
    """
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
```


```python
class Inventory:
    """
    Manages a collection of items in the inventory.

    The Inventory class acts as a container and controller for all items.
    It allows adding, displaying, updating, and deleting products,
    as well as saving and loading them from Google Sheets.

    This separation of logic (Inventory vs. Item) makes the program
    easier to maintain and scale.

    Attributes:
        items (list): A list that stores all Item objects in the inventory.
        worksheet: The Google Sheets worksheet object for data persistence.
    """
    def __init__(self, worksheet):
        self.worksheet = worksheet
        self.items = []
```

The primary functions used on this application are:

- `add_item()`
  - Prompts user for item details (ID, name, quantity, price), adds a new Item object to the inventory list, and saves it to Google Sheets.
- `update_item()`
  - Allows user to modify an existing item's name, quantity, and price by searching for it by ID, then syncs changes to Google Sheets.
- `delete_item(id)`
  - Removes an item from the inventory by ID after user confirmation (y/n prompt) and deletes it from Google Sheets.
- `display_item()`
  - Displays all items in a formatted table sorted by ID, showing ID, name, quantity, and price.
- `get_valid_int(prompt)`
  - Static method that validates and returns integer input, re-prompting on invalid entries.
- `get_valid_float(prompt)`
  - Static method that validates and returns float input for price values.
- `get_id()`
  - Gets a unique item ID from the user, checking for duplicates in the existing inventory.
- `get_name()`
  - Gets a unique item name from the user with comprehensive validation: checks for empty input, ensures 3-15 characters with at least 3 letters using regex, and prevents duplicates (case-insensitive).
- `check_inventory_not_empty()`
  - Decorator function that prevents operations on empty inventory and displays a warning.
- `get_items()`
  - Loads existing inventory data from Google Sheets into the local inventory on program startup.
- `save_to_sheet(item)`
  - Saves a new item to the Google Sheets worksheet.
- `update_item_in_sheet(item_id, item)`
  - Updates an existing item in the Google Sheets worksheet by ID.
- `main()`
  - Displays the welcome message and program instructions when the application starts.
- `tasks_list()`
  - Displays the main menu and handles user task selection in a loop until exit.
- `my_task(selected_task)`
  - Executes the selected task (1-5) by calling the appropriate inventory method.

#### Imports

I've used the following Python packages and external imports.

- `gspread`: used for connecting to and interacting with Google Sheets API
- `google.oauth2.service_account`: used for authenticating with Google Sheets using service account credentials
- `colorama`: used for including color in the terminal (Fore, Back, Style)
- `re`: used for regex pattern matching in name validation
- `item`: local module containing the Item class definition
- `inventory`: local module containing the Inventory class and inventory management logic


## Testing

## Code Validation

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.


The final results are as follows:


| File  | Screenshot | Notes |
| ---  | --- | --- |
| [run.py](https://github.com/Scaphix/my_inventory_manager/blob/main/run.py) | ![screenshot](document/run-valid.png)  | No errors found |
| [inventory.py](https://github.com/Scaphix/my_inventory_manager/blob/main/inventory.py) | ![screenshot](document/inventory-valid.png)  | No errors found |
| [item.py](https://github.com/Scaphix/my_inventory_manager/blob/main/item.py) | ![screenshot](document/item-valid.png)  | No errors found |


## Bugs

**Bug 1**:
 ![](document/bug2.png)

**Description**: I deployed the project to Heroku without including all required dependencies in the requirements.txt file. This caused an error where Heroku could not recognize the module. 

**Correction**: I added the missing dependencies to fix the deployment issue.


**Bug 2**:

 ![](document/bug1.png)

**Description**: I called a method without passing any argument.

```python
    elif selected_task == "4":

        inventory.delete_item()
```
**Correction**:

```python
    elif selected_task == "4":

        name_to_delete = input(" Enter Name: ").strip()

        inventory.delete_item(name_to_delete)
```

**Bug 3**:

**Description**: The delete function was comparing string input with integer IDs, causing items to not be found. When adding items, IDs were stored as integers via `get_valid_int()`, but the delete function accepted input as a string without conversion.

**Correction**: Added type conversion in the delete task handler:

```python
    elif selected_task == "4":
        print("Please enter the id of the item to delete ")
        try:
            id_to_delete = int(input("Enter Id: ").strip())
            inventory.delete_item(id_to_delete)
        except ValueError:
            print(Fore.RED + "Invalid ID! Please enter a number.")
            print(Style.RESET_ALL)
```

**Bug 4**:

**Description**: When a user entered an invalid response (anything other than 'y' or 'n') at the delete confirmation prompt, the code did not return from the function. It would fall through the conditional and print "not found" even though the item was found.

**Correction**: Added an else clause to handle invalid confirmation input:

```python
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
```

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser. This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://my-inventory-manager-17f3f6d5a838.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of **KEY** to `PORT`, and the **VALUE** to `8000` then select **ADD**.
- If using any confidential credentials, such as **CREDS.JSON**, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important; select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [runtime.txt](runtime.txt)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: node index.js > Procfile`

The **[runtime.txt](runtime.txt)** file tells Heroku the specific version of Python to use when running your application.

- `python-3.12.2` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The Python terminal window should now be connected and deployed to Heroku!

### Google Sheets API

This application uses [Google Sheets](https://docs.google.com/spreadsheets) to handle a "makeshift" database on the live site.

To run your own version of this application, you will need to create your own Google Sheet with one sheet named `stock` in the following format:

| ID | Name | Quantity | Price | 
| --- | --- | --- | --- | 
| sample data | sample data | sample data | sample data |
| sample data | sample data | sample data | sample data | 
| sample data | sample data | sample data | sample data | 

A credentials file in `.JSON` format from the Google Cloud Platform is also mandatory:

[Google Cloud Platform](https://console.cloud.google.com)

1. From the dashboard click on "Select a project", and then the **NEW PROJECT** button.
2. Give the project a name, and then click **CREATE**.
3. Click **SELECT PROJECT** to get to the project page.
4. From the side-menu, select "APIs & Services", then select "Library".
5. Search for the "Google Drive API", select it, and then click on **ENABLE**.
6. Click on the **CREATE CREDENTIALS** button.
7. From the "Which API are you using?" dropdown menu, choose **Google Drive API**.
8. For the "What data will you be accessing?" question, select **Application Data**.
9. Click **Next**.
10. Enter a "Service Account" name, then click **Create**.
11. In the "Role" dropdown box, choose "Basic" > "Editor", then press **Continue**.
12. "Grant users access to this service account" can be left blank. Click **DONE**.
13. On the next page, click on the "Service Account" that has been created.
14. On the next page, click on the "Keys" tab.
15. Click on the "Add Key" dropdown, and select "Create New Key".
16. Select `JSON`, and then click **Create**. This will trigger the `.json` file with your API credentials in it to download to your machine locally.
17. For local deployment, this needs to be renamed to `creds.json`.
18. Repeat steps 4 & 5 above to add the "Google Sheets API".
19. Copy the `client_email` that is in the `creds.json` file.
20. Share your Google Sheet to the `client_email`, ensuring "Editing" is enabled.
21. Add the `creds.json` file to your `.gitignore` file, so as not to push your credentials to GitHub publicly.

### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.


#### How to Clone a repository

1. On GitHub, go to the repository for this project, [GitHub repository](https://www.github.com/Scaphix/my_inventory_manager).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Copy the URL for the repository.

    - To clone the repository using HTTPS, under "HTTPS", click the copy button.
    - To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click the copy button.
    - To clone a repository using GitHub CLI, click GitHub CLI, then click the copy button.

4. Open Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/Scaphix/my_inventory_manager.git`
7. Press Enter. Your local clone will be created.

![](document/clone-repo.png)

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/Scaphix/my_inventory_manager).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.

![](document/fork-repo.png)

3. Select the dropdown menu and click on owner for the forked repository.
4. Click Create fork.


## Credits


### Content


| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Love Sandwiches](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [Colorama](https://www.youtube.com/watch?v=u51Zjlnui4Y) | Adding color in Python |
| [StackOverflow](https://stackoverflow.com/a/50921841) | Clear screen in Python |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

I used the background image from the website below:

[Layout image](https://www.veeqo.com/gb/blog/inventory-shrinkage)


### Acknowledgements

- I would like to thank my Code Institute mentors, [Tim Nelson](https://www.github.com/TravelTimN) and [Iuliia Konovalova](https://github.com/IuliiaKonovalova) for their valuable guidance and constructive feedback for this project.

- I would like to thank the CI community, and especially [Kathrinmzl](https://github.com/kathrinmzl), for taking the time to review my project and offer thoughtful, detailed feedback.

- I would like to thank my husband for his kindness, help and unwavering support throughout the development of this project.