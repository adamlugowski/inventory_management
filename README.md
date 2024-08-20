Task: Inventory Management System
Objective:
Create a simple command-line inventory management system in Python. This system will allow you to add, remove, and view items in an inventory.

Requirements:

Item Management:

You should be able to add an item with a name and quantity.
You should be able to remove an item by its name (if it exists) or update the quantity of an existing item.
You should be able to view all items and their quantities.
Commands:

add <item_name> <quantity>: Adds an item with the specified quantity. If the item already exists, increase its quantity.
remove <item_name> <quantity>: Removes a specified quantity of an item. If the quantity to remove is greater than the current quantity, remove the item entirely.
view: Displays all items and their quantities.
exit: Exits the program.
Storage:

Use a Python dictionary to store the items where the key is the item name and the value is the quantity.
Validation:

Ensure that the quantity is a positive integer.
Handle cases where an item to be removed does not exist or the quantity to be removed is invalid.
