#.E-Commerce Order Management Manage orders, returns, and refunds. 
#Handle cases like invalid coupon code, out-of-stock errors, invalid payment methods. 
class ECommerceOrderManagement:
    def __init__(self):
        self.orders = {}
        self.coupons = {"DISCOUNT10": 0.1, "DISCOUNT20": 0.2}
        self.stock = {"item1": 10, "item2": 5}

    def manage_oreders(self, order_id, item, quantity, coupon_code=None, payment_method=None):
        if item not in self.stock:
            raise ValueError("Item is out of stock")
        if quantity > self.stock[item]:
            raise ValueError("Not enough stock available")
        if coupon_code and coupon_code not in self.coupons:
            raise ValueError("Invalid coupon code")
        if payment_method not in ["credit_card", "paypal"]:
            raise ValueError("Invalid payment method")
        discount = self.coupons.get(coupon_code, 0)
        total_price = quantity * 100 * (1 - discount)  # Assuming each item costs 100
        self.orders[order_id] = {"item": item, "quantity": quantity, "total_price": total_price}
        self.stock[item] -= quantity
# test the e-commerce order management system
if __name__ == "__main__":
    order_management = ECommerceOrderManagement()
    try:
        print("Managing orders...")
        print("Enter order ID: ")
        order_id = input()
        print("Enter item name: ")
        item = input()
        print("Enter quantity: ")
        quantity = int(input())
        print("Enter coupon code (or press Enter to skip): ")
        coupon_code = input()
        if not coupon_code:
            coupon_code = None
        print("Enter payment method (credit_card/paypal): ")
        payment_method = input()
        order_management.manage_oreders(order_id, item, quantity, coupon_code, payment_method)
        print("Order managed successfully.")
    except ValueError as e:
        print(e)
        