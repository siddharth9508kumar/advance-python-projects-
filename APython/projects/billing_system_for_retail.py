class billing_system:
    def __init__(self):
        self.items = {}
        self.total = 0
    def scan_item(self, item_name, price):
        self.items[item_name] = price
        self.total += price
        print(f'Item "{item_name}" scanned with price ${price:.2f}. Total is now ${self.total:.2f}.')
    def apply_discount(self, discount_percentage):
        discount_amount = self.total * (discount_percentage / 100)
        self.total -= discount_amount
        print(f'Discount of {discount_percentage}% applied. Total is now ${self.total:.2f}.')
    def gernate_receipt(self):
        print("\n--- Receipt ---")
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}")
        print(f"Total: ${self.total:.2f}")
        print("Thank you for shopping with us!")
    def record_payment(self, amount_paid):
        if amount_paid >= self.total:
            change = amount_paid - self.total
            print(f"Payment of ${amount_paid:.2f} received. Change: ${change:.2f}.")
            self.total = 0  # Reset total after payment
            self.items.clear()  # Clear items after payment
        else:
            print(f"Payment of ${amount_paid:.2f} is insufficient. Total is ${self.total:.2f}.")


billing_system = billing_system()

while True:
    action = input("Enter '1' to scan an item, '2' to apply a discount, '3' to generate a receipt, '4' to record payment, or '5' to exit: ")
    if action == "1":
        item_name = input("Enter the name of the item: ")
        price = float(input("Enter the price of the item: "))
        billing_system.scan_item(item_name, price)
    elif action == "2":
        discount_percentage = float(input("Enter the discount percentage: "))
        billing_system.apply_discount(discount_percentage)
    elif action == "3":
        billing_system.gernate_receipt()
    elif action == "4":
        amount_paid = float(input("Enter the amount paid by the customer: "))
        billing_system.record_payment(amount_paid)
    elif action == "5":
        print("Exiting the billing system. Have a great day!")
        break
    else:
        print("Invalid action. Please use '1', '2', '3', '4', or '5'.")