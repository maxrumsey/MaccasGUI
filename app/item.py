"""Item

This class stores information about each item in the order
"""

class Item():
    """Contains information about each item in the order"""

    def __init__(self, name, number, price, size, size_int):
        self.name = name
        self.total = 0
        self.amount = number
        self.price = price
        self.size = size
        self.promo_num = 0
        self.set_amount(number)
        self.size_int = size_int

    def set_amount(self, number):
        """Changes the number of items present, in the Item class"""

        self.amount = number

        self.total = number * self.price - self.promo_num * self.price

        if self.total < 0:
            self.total = 0
            return

    def promo(self):
        """Increments the number of item's `promo-ed` by 1"""

        if self.promo_num == self.amount:
            return

        self.promo_num += 1

        self.total = self.amount * self.price - self.promo_num * self.price
