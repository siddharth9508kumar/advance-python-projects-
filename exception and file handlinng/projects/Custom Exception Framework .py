#5.Custom Exception Framework Create your own custom exceptions for a specific application (like an Inventory 
# Management System). 
class InventoryError(Exception):
    """Base class for inventory-related exceptions."""
    pass
class OutOfStockError(InventoryError):
    """Raised when an item is out of stock."""
    def __init__(self, item):
        self.item = item
        super().__init__(f"Item '{item}' is out of stock.")
class InvalidItemError(InventoryError):
    """Raised when an invalid item is encountered."""
    def __init__(self, item):
        self.item = item
        super().__init__(f"Item '{item}' is invalid.")
class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {"item1": 10, "item2": 5}

    def check_stock(self, item):
        if item not in self.inventory:
            raise InvalidItemError(item)
        if self.inventory[item] <= 0:
            raise OutOfStockError(item)
        return self.inventory[item]
# test the inventory management system
if __name__ == "__main__":
    inventory_system = InventoryManagementSystem()
    try:
        print("Checking stock...")
        item = input("Enter item name to check stock: ")
        stock = inventory_system.check_stock(item)
        print(f"Stock for '{item}': {stock}")
    except InventoryError as e:
        print(e)

        