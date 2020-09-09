"""day_meta

This class is responsible for recording data about the business day
including the total GST collected and number of item sordered
"""

class DayMeta:
    """Submodule of main for storing information about the order"""

    def __init__(self, manager):
        self.manager = manager
        self.order_number = 1
        self.daily_total = 0
        self.dinein = 0
        self.takeaway = 0
        self.gst = 0
        self.log = {}

        for item in self.manager.prices:
            self.log[item] = [0, 0, 0]

    def get_order_num(self):
        """Returns the current order number in an string format"""

        return str(self.order_number)
