class DayMeta:
    def __init__(self, manager):
        self.manager = manager
        self.orderNumber = 1
        self.dailyTotal = 0
    
    def getOrderNum(self):
        return str(self.orderNumber)

    