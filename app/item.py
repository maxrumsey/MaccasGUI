class Item():
    def __init__(self, name, number, price, size, sizeInt):
        self.name = name
        self.amount = number
        self.price = price
        self.size = size
        self.promoNum = 0
        self.setAmount(number)
        self.sizeInt = sizeInt

    def setAmount(self, number):
        self.amount = number

        self.total = number * self.price - self.promoNum * self.price

        if (self.total < 0):
            self.total = 0
            return
    
    def promo(self):
        if (self.promoNum == self.amount):
            return

        self.promoNum += 1

        self.total = self.amount * self.price - self.promoNum * self.price