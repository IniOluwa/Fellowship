# Python Shopping Cart

# ShoppingCart Class
class ShoppingCart(object):
    """docstring for ShoppingCart."""
    # ShoppingCart Constructor
    def __init__(self):
        super(ShoppingCart, self).__init__()
        self.total = 0
        self.items = {}

    # Add Item To Cart
    def add_item(self, item_name, quantity, price):
        self.total += price * quantity
        self.items[item_name] = quantity

    # Remove Item From Cart
    def remove_item(self, item_name, quantity, price):
        if quantity >= self.items[item_name]:
            del self.items[item_name]
        self.total -= price * quantity
        self.items[item_name] -= quantity

    # Checkout Items
    def checkout(self, cash_paid):
        if cash_paid < self.total:
            return "Cash paid not enough"
        return self.total


# Shop Class - A child class of ShoppingCart
class Shop(ShoppingCart):
    """docstring for Shop."""
    # Shop Constructor
    def __init__(self):
        super(Shop, self).__init__()
        self.quantity = 100

    # Deduct Quantity
    def remove_item(self):
        self.quantity -= 1

# Execution
cart = ShoppingCart()
sneakers = cart.add_item('AirMax', 2, 150)
macbooks = cart.add_item('MacBook Pro', 7, 1500)
tanktops = cart.add_item('Tanktop', 1, 30)
print cart.items
cart.remove_item('AirMax', 1, 150)
cart.remove_item('MacBook Pro', 2, 1500)
print cart.items
print cart.checkout(10000)
shop = Shop()
print shop.remove_item()
