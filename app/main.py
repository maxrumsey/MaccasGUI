import sys
from app import item
sys.path.append('..')

# pylint: disable=import-error
from gui import base
from gui.cats import coffee

class Main:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1163x800")
        self.window.minsize(1163, 800)
        self.window.maxsize(1163, 800)
        self.itemSize = 1
        self.numberInput = ""
        self.order = []

    def start(self):
        base.mainGUI(self.window, self)
        self.setCat("Coffee")
        self.window.mainloop()

    def setCat(self, type):
        if type == "Coffee":
            coffee.set(self, self.window.children['frameInput'].children['leftFrame'].children['itemBoard'])
        elif type == "Lunch":
            print(1)
        elif type == "Dessert":
            print(1)
        elif type == "Condiments":
            print(1)
        else:
            print("Unknown Type: " + str(type))

    def addItem(self, name):
        initItem = item.Item(name, int(self.itemSize), 15.50)
        
        found = False
        for inx, val in enumerate(self.order):
            if (val.name == initItem.name):
                found = True
                initItem.setAmount(1 + val.amount)
                self.order.remove(val)
                self.order.insert(inx, initItem)
                break
            
        if not found:
            self.order.append(initItem) 
        
        
