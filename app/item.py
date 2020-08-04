class Item():
    def __init__(self, name, number, price):
        self.name = name
        self.amount = number
        self.price = price
        self.total = number * price

    def setAmount(self, number):
        self.amount = number
        self.total = number * self.price