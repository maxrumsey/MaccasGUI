class DayMeta:
    def __init__(self, manager):
        self.manager = manager
        self.orderNumber = 1
        self.dailyTotal = 0
        self.log = {}

        for item in self.manager.prices:
            self.log[item] = [0, 0, 0]
    
    def getOrderNum(self):
        return str(self.orderNumber)

    