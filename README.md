# [my_inventory_manager](https://my-inventory-manager-17f3f6d5a838.herokuapp.com)

Developer: Chahinez Boutemine ([Scaphix](https://www.github.com/Scaphix))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Scaphix/my_inventory_manager)](https://www.github.com/Scaphix/my_inventory_manager/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Scaphix/my_inventory_manager)](https://www.github.com/Scaphix/my_inventory_manager/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Scaphix/my_inventory_manager)](https://www.github.com/Scaphix/my_inventory_manager)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://my-inventory-manager-17f3f6d5a838.herokuapp.com)

The Inventory Management Tool is a simple, Python-based command-line application designed to help small businesses keep track of their stock efficiently. It allows users to add, update, delete, and display items with clear, color-coded feedback in the terminal. The idea for this project came from my own experience working in my family’s business, where I realized we lacked an organized way to manage inventory. I always wanted to create a tool that could make this process easier, and learning Python gave me the opportunity to finally build it myself.


![screenshot](documentation/mockup.png)


## UX


**Purpose**
- Provide users with a simple and effective way to track inventory levels and manage products directly from the terminal.
- Help small business owners maintain accurate records of their stock, reduce manual errors, and make informed decisions about restocking or pricing.
- Offer a practical learning experience for understanding how programming concepts can be applied to real-world business problems.

**Primary User Needs**
- Easily add, update, delete, and view items in the inventory.
- Keep track of product quantities and prices with minimal technical knowledge.
- Store data safely for later use, with the option to extend the system to save data to a file or connect to Google Sheets.
- Receive clear and user-friendly feedback through color-coded messages in the terminal.

**Business Goals**
- Offer a lightweight, reliable, and cost-free tool to manage inventory without requiring advanced software.
- Help businesses save time, avoid stock shortages or overstocking, and maintain up-to-date records.
- Support better organization and customer satisfaction by ensuring that stock information is always accurate and easy to access.


## Wireframes

To follow best practice, a flowchart was created to showcase the progression of the Python app.
I've used [Lucidchart](https://www.lucidchart.com/pages/examples/flowchart-maker) to design my app flowchart.

![screenshot](documentation/flowchart.png)

## User Stories


| Target | Expectation | Outcome |
| --- | --- | --- |
| As a user | I would like to input the number of each sandwich type sold during the day | so that I can track daily sales accurately. |
| As a user | I would like to view a breakdown of total sandwich sales by type | so that I can easily see which sandwiches are the most and least popular. |
| As a user | I would like the application to calculate the total sandwiches sold for the day | so that I don’t have to do manual sums. |
| As a user | I would like to see a trend of sandwich sales over time (e.g., week, month) | so that I can identify which sandwiches are consistently popular. |
| As a user | I would like the application to suggest an estimated number of each sandwich type to make for the next day, based on past sales data | so that I can minimize waste and shortages. |
| As a user | I would like the app to categorize sandwiches by type (e.g., vegetarian, meat, cheese) | so that I can track popularity within different dietary categories. |
| As a user | I would like to input sales quickly with minimal typing | so that I can focus on running the shop instead of logging data. |
| As a user | I would like the app to be intuitive and easy to use | so that I can start tracking sales without needing extensive training. |

## Features


### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Data Input Validation | The program validates user input by ensuring the data is exactly six comma-separated numbers before continuing. | ![screenshot](documentation/features/data-validation.png) |
| API Update | Sales, surplus, and stock data are updated in the relevant Google Sheets worksheet using gspread functionality. | ![screenshot](documentation/features/api-update.png) |
| Surplus Calculation | Calculates surplus by comparing the latest stock and sales data to identify potential waste or shortages. | ![screenshot](documentation/features/surplus-calculation.png) |
| Last 5 Sales Entries | Retrieves the last five sales entries from the "sales" worksheet for calculating stock averages. | ![screenshot](documentation/features/latest-entries.png) |
| Stock Calculation | Computes stock based on the last 5 sales entries, adding 10% to the average to ensure adequate future stock. | ![screenshot](documentation/features/stock-calculation.png) |
| Sales Data Automation | Automates the entire process of retrieving, validating, and updating sales, surplus, and stock data in Google Sheets. | ![screenshot](documentation/features/sales-data.png) |

### Future Features


- **User Authentication and Role Management**: Implement a login system with roles (e.g., admin, employee) to restrict data access based on user roles.
- **Data Visualization**: Add charts and graphs to visually represent sales trends, stock levels, and surplus/waste over time.
- **Real-time Data Sync**: Integrate real-time syncing of sales and stock data across multiple devices to support live updates.
- **Automated Restocking Alerts**: Notify users when stock levels fall below a certain threshold, prompting restock orders.
- **Predictive Analytics**: Use historical sales data to predict future demand, helping to optimize stock levels and minimize waste.
- **Multilingual Support**: Add support for multiple languages to make the app more accessible to a global audience.
- **Mobile App Integration**: Develop a mobile version of the app for easier data input and stock management on the go.
- **Reporting and Exporting**: Generate and export detailed reports in PDF or CSV format for deeper analysis of sales, surplus, and stock data.
- **Inventory Management**: Include functionality to track supplier information, order inventory, and manage costs directly within the app.
- **Customer Feedback Integration**: Allow customers to leave feedback on sold items, giving insight into sales performance and customer satisfaction.
- **Customizable Dashboards**: Provide users with the ability to customize their dashboard, selecting which data points and metrics they want to monitor.
- **Historical Data Comparison**: Implement functionality to compare current sales and stock data with data from the same period in previous years.
- **Seasonal Adjustment Recommendations**: Analyze sales patterns and suggest stock adjustments for holidays or other seasonal trends.
- **API Integration**: Provide an API for integrating with other third-party services, such as point-of-sale systems or accounting software.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Lucidchart-grey?logo=lucid&logoColor=F97B2C)](https://www.lucidchart.com) | Flow diagrams for mapping the app's logic. |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |


## Database Design

### Data Model

#### Flowchart


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
    as well as saving and loading them (eventually from JSON or Google Sheets).

    This separation of logic (Inventory vs. Item) makes the program
    easier to maintain and scale.

    Attributes:
        items (list): A list that stores all Item objects in the inventory.
    """
    def __init__(self):
        self.items = []
```

The primary functions used on this application are:

- `get_sales_data()`
    - Get sales figures input from the user.
- `validate_data()`
    - Converts all string values into integers.
- `update_worksheet()`
    - Update the relevant worksheet with the data provided.
- `calculate_surplus_data()`
    - Compare sales with stock and calculate the surplus for each item type.
- `get_last_5_entries_sales()`
    - Collects columns of data from sales worksheet.
- `calculate_stock_data()`
    -  Calculate the average stock for each item type, adding 10%.
- `main()`
    - Run all program functions.

#### Imports

I've used the following Python packages and external imports.

- `gspread`: used with the Google Sheets API
- `google.oauth2.service_account`: used for the Google Sheets API credentials
- `os`: used for adding a `clear()` function
- `colorama`: used for including color in the terminal
- `random`: used to get a random choice from a list

## Agile Development Process

### GitHub Projects


[GitHub Projects](https://www.github.com/Scaphix/my_inventory_manager/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.


### Must Have (MVP)
- [As a user, I want to search for a title so that I can find relevant information.](https://github.com/larevolucia/reeltracker_cli/issues/3)

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/Scaphix/my_inventory_manager/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/Scaphix/my_inventory_manager?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/Scaphix/my_inventory_manager/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/Scaphix/my_inventory_manager?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/Scaphix/my_inventory_manager/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Bugs

**Bug 1**:

**Description**: I deployed the project to Heroku without including all required dependencies in the requirements.txt file. 

**Correction**: This caused an error where Heroku could not recognize the 'colorama' module. 
Added the missing dependencies to fix the deployment issue.


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
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: node index.js > Procfile`

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The Python terminal window should now be connected and deployed to Heroku!



### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/Scaphix/my_inventory_manager).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/Scaphix/my_inventory_manager.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/Scaphix/my_inventory_manager)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/Scaphix/my_inventory_manager).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!


## Credits


### Content


| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [Love Sandwiches](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Real Python](https://realpython.com/python-quiz-application) | Inspiration for a quiz app |
| [BroCode](https://www.youtube.com/watch?v=ag8NtD1e0Kc) | Inspiration for hangman game |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [Colorama](https://www.youtube.com/watch?v=u51Zjlnui4Y) | Adding color in Python |
| [StackOverflow](https://stackoverflow.com/a/50921841) | Clear screen in Python |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

| Source | Notes |
| --- | --- |
| [ASCII Art Archive](https://www.asciiart.eu) | Pre-defined ASCII art |
| [TEXT-IMAGE](https://www.text-image.com) | Converting an image to ASCII art |
| [Patorjk](https://patorjk.com/software/taag) | Converting text to ASCII art |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.


https://developers.google.com/workspace/sheets/api/quickstart/python