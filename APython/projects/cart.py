class item():
    def __init__(self,*args):
        if len(args)==2:
            self.name = args[0]
            self.quantity = args[1]
        elif len(args)==1:
            self.name = args[0]
            self.quantity = int(input("Enter quantity to remove : "))
        else:
            raise ValueError("Pass exactly 2 or 3 arguments")


class cart():
    def __init__(self):
        self.items = [] 
    
    def add_item(self, new_item):
        for existing_item in self.items:
            if existing_item.name == new_item.name:
                existing_item.quantity += new_item.quantity
                return
        self.items.append(new_item)

    def remove_item(self, rem_item, quantity=1):
        for existing_item in self.items:
            if existing_item.name == rem_item.name:
                if existing_item.quantity <= quantity:
                    self.items.remove(existing_item)
                else:
                    existing_item.quantity -= quantity
                return
        print("404! item not found...")

    def display_cart(self):
        if not self.items:
            print("Cart is empty!")
            return
        print("\n--- Your Cart ---")
        for i in self.items:
            print(f"Name: {i.name}, Quantity: {i.quantity}")
        print("----------------\n")


my_cart = cart()

while True:
    action = int(input("""1. add item to cart
2. remove item from cart
3. display cart
4. exit
What you want to do : """))

    if action == 1:
        item_name = input("Enter item name: ")
        item_quantity = int(input("Enter item quantity: "))
        new_item = item(item_name, item_quantity)
        my_cart.add_item(new_item)
        my_cart.display_cart()
    elif action == 2:

        rem_item = item(input("Enter item name to remove: "))
        my_cart.remove_item(rem_item, rem_item.quantity)
        my_cart.display_cart()
    elif action == 3:
        my_cart.display_cart()
    elif action == 4:
        print("Goodbye!")
        break
    else: 
        print("Wrong input !!!")




















# items = [
#          {1:"shoes"},
#          {2:"water bottle"},
#          {3:"bag"},
#          {4:"cloth"},
#          {5:"notebook"},
#          {6:"cap"}
#          ]