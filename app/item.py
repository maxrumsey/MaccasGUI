class Item():
    def __init__(self, name, number, price):
        self.name = name
        self.amount = number
        self.price = price

    def setAmount(self, number):
        self.amount = number