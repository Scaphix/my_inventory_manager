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

    def __str__(self):
        return f"{self.name} | Qty: {self.quantity} | Price: ${self.price:.2f}"
