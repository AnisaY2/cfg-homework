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

        self.total_items = {}   # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):             # add a new item to the items we already have (update method)
        self.total_items.update({item: price})
        print(item, price)

    def remove_item(self, item):                 # take an item away from the items we already have (pop method)
        self.total_items.pop(item)
        print(self.total_items)

    def apply_discount(self, discount):          # apply unknown discount amount
        self.discount = discount
        discount_decimal = discount / 100
        discounted_total = sum(self.total_items.values()) * (1 - discount_decimal)
        print(discounted_total)                  # need it to be to 2dp

    def get_total(self):                         # all the item prices added up (sum method)
        self.total_price = sum(self.total_items.values())
        print(self.total_price)

    def show_items(self):                        # return all the items currently in the dictionary total_items
        print(self.total_items)

    def reset_register(self):                    # remove everything from total_items and set it all back to zero
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0


# EXAMPLE code run:
customer = CashRegister()
customer.add_item("Bag", 2.50)
customer.add_item("Jumper", 8.99)
customer.add_item("Socks", 3.00)

customer.remove_item("Bag")

customer.apply_discount(15)

customer.get_total()

customer.show_items()

customer.reset_register()


