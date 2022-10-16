# Due 16.10.22

"""
TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):

        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        self.total_items.update({item: price})
        print(f"The item {item} has been added.")

    def remove_item(self, item):
        self.total_items.pop(item)
        print(f"The item {item} has been removed. \nItems remaining: {self.total_items}")

    def apply_discount(self, discount):
        self.discount = discount
        print(f"{discount}% discount applied.")

    def get_total(self):
        self.total_price = sum(self.total_items.values())
        discount_decimal = self.discount / 100
        discounted_total = self.total_price * (1 - discount_decimal)
        print(f"Total Price (including any discount): £{discounted_total:.2f}")
        return discounted_total

    def show_items(self):
        print(f"Current items: {self.total_items}")

    def reset_register(self):
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0
        print("Cash register has been reset")


customer = CashRegister()

customer.add_item("Bag", 2.75)
customer.add_item("Jumper", 11.99)
customer.add_item("Socks", 3.50)
customer.remove_item("Bag")
customer.apply_discount(3.25)
customer.get_total()
customer.show_items()
customer.reset_register()
