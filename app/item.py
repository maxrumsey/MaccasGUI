class Item():
    def __init__(self, name, number, price, size):
        self.name = name
        self.amount = number
        self.price = price
        self.size = size
        self.promoNum = 0
        self.setAmount(number)

    def setAmount(self, number):
        self.amount = number
        self.total = number * self.price - self.promoNum * self.price
    
    def promo(self):
        self.promoNum += 1