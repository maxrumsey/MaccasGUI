import sys
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

    def start(self):
        base.mainGUI(self.window, self)
        self.setCat("Coffee")
        self.window.mainloop()
        print(1)

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

