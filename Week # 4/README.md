**Project Name**: 
----------------
   Inventory Management System (IMS)

**Project Introduction**:
------------------------
This project implements a basic inventory management system for food items. 
It allows users to add, edit, delete, search, and display information about food items in a CSV file.

**Tech Stack**:
----------------
**Programming Language:** Python 3

 **Libraries**:

> **csv:** Used for reading from and writing to CSV files.
> **datetime**: Used for working with dates.
> **os**: Used for interacting with the operating system (error handling).
>**tabulate**: Used for creating formatted tables from data.

**Concepts**:

> **Object-Oriented Programming (OOP)**: Uses classes to represent food items and inventory management functionalities.
> **File I/O:** Reads from and writes data to CSV files.
> **Error Handling**: Handles potential errors that may occur during file operations or user input.

 **Key Features:**
--------------
> **Add**__ food items to the inventory with details like name, category, quantity, price, barcode, and expiry date.
>** Edit**__ existing food items in the inventory.
> **Delete**__ food items from the inventory.
>** Display**__ the entire inventory in a tabular format.
> **Search**__ for food items based on various criteria like name, category, quantity, price, barcode, and expiry date.

 **How Does it Work?**
--------------------
1- The system uses a _CSV file_ to store inventory data.

2- Users interact with the system through a _command-line interface._

3- The _app.py_ script provides the main entry point for the application.
> It greets the user and gets their name.
> It presents a menu of options for adding, editing, deleting, searching, or displaying inventory items.
> It delegates tasks to the appropriate classes in the _IMS_package directory_.

4- The _IMS_package_ directory contains the core functionalities of the system.
>> The _inventory.py_ script manages the overall inventory.
   > It interacts with the _CSV_ file using the filing.py class.
   > It provides methods for adding, editing, deleting, searching, and displaying inventory items.
>> The _filing.py_ script handles CSV file operations.
   > It provides methods for creating, reading, updating, and writing to the CSV file.
>> The _food_items.p_y script defines a class FoodItems to represent individual food items in the inventory.
   > It stores attributes like name, category, quantity, price, barcode, and expiry date.

 **Running the System**
-----------------------
> Save the code snippets provided above in separate Python files (e.g., app.py, filing.py, inventory.py, food_items.py).
> Ensure you have the required Python libraries (csv, datetime, optionally tabulate) installed using pip install csv datetime tabulate.
> Run the app.py script using python app.py.
> Follow the on-screen instructions to interact with the inventory management system.