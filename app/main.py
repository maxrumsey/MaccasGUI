import sys
import tkinter as tk
from app import item
from app import payment
from app import dayMeta
sys.path.append('..')

# pylint: disable=import-error
from gui import base
from gui.cats import coffee
from gui.cats import burger

sizeEnum = [
    ("Small", 0.9),
    ("Medium", 1),
    ("Large", 1.2)
]

class Main:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1163x800")
        self.window.minsize(1163, 800)
        self.window.maxsize(1163, 800)
        self.itemSize = 1
        self.numberInput = ""
        self.order = []
        self.orderList = None
        self.gui = None
        self.paymentWindow = None
        self.orderDetailTable = {}
        self.dayMeta = dayMeta.DayMeta(self)
        self.total = 0
        self.takeOut = False

    def start(self):
        base.mainGUI(self.window, self)
        self.setCat("Coffee")
        self.window.mainloop()

    def setCat(self, type):
        if type == "Coffee":
            coffee.set(self, self.window.children['frameInput'].children['leftFrame'].children['itemBoard'])
        elif type == "Lunch":
            burger.set(self, self.window.children['frameInput'].children['leftFrame'].children['itemBoard'])
        elif type == "Dessert":
            print(1)
        elif type == "Condiments":
            print(1)
        else:
            print("Unknown Type: " + str(type))

    def addItem(self, name):
        if not name:
            return
        
        initItem = item.Item(name, 1, 15.50 * sizeEnum[self.itemSize][1], sizeEnum[self.itemSize][0])

        self.itemSize = 1

        number = 1
        numberSet = False
        if self.numberInput != "":
            number = int(self.numberInput)
            initItem.setAmount(number)
            self.numberInput = ""
            numberSet = True
        
        cursorIndex = self.orderList.curselection()

        found = False
        for inx, val in enumerate(self.order):
            if (val.name == initItem.name and
                val.size == initItem.size and
                val.price == initItem.price):
                found = True
                if (len(cursorIndex) != 0 and
                    numberSet == True and
                    cursorIndex[0] == inx):
                    if (initItem.amount == 0):
                        self.order.pop(inx)
                    else:
                        val.setAmount(initItem.amount)

                    break

                else:
                    initItem.setAmount(initItem.amount + val.amount)

                self.order.remove(val)
                if (initItem.amount != 0):
                    self.order.insert(inx, initItem)
                break
            
        if (not found and 
            initItem.amount != 0):
            self.order.append(initItem) 
        
        self.buildItemsList()
        
    def buildItemsList(self):
        self.orderList.delete(0, tk.END)
        for item in self.order:
            txt = "{amount} {size} {name} == {price:0.2f}"
            self.orderList.insert(tk.END, txt.format(amount=item.amount,size=item.size, name=item.name, price=item.total))
        
        if (self.takeOut == True):
            self.orderList.insert(tk.END, "---Take Out---")
                    
        self.orderList.selection_set(0)

        subtotal = self.getTotal()
        GST = (subtotal / .9) * .1
        surcharge = 0
        if (self.takeOut == True):
            surcharge = (subtotal + GST) * 0.05
        self.total = subtotal + GST + surcharge

        self.setOrderTable("SubTotal", "${0:0.2f}".format(subtotal))
        self.setOrderTable("Surcharge", "${0:0.2f}".format(surcharge))
        self.setOrderTable("GST", "${0:0.2f}".format(GST))
        self.setOrderTable("Order #", self.dayMeta.getOrderNum())
        self.setOrderTable("Total", "${0:0.2f}".format(self.total))
        self.setOrderTable("Daily Total", "${0:0.2f}".format(self.dayMeta.dailyTotal))

    def setOrderTable(self, key, value):
        self.orderDetailTable[key].delete(0, tk.END)
        self.orderDetailTable[key].insert(0, value)

    def voidItem(self, index):
        self.order.pop(index)
    
    def voidItemPress(self):
        listBox = self.orderList
        if (len(listBox.curselection()) == 0):
            return

        index = listBox.curselection()[0]
        if (self.takeOut == True and index == len(self.order)):
            self.takeOut = False
            self.buildItemsList()
            return

        if index != None:
            order = self.order[index]
            amount = order.amount

            if amount > 1:
                order.setAmount(amount-1)

            else:
                self.order.pop(index)

            self.buildItemsList()

            listBox.selection_clear(first=True)
            listBox.selection_set(index)
    
    def pay(self):
        if len(self.order) == 0:
            return
        self.paymentWindow = payment.PaymentWindow(self, self.window.children['framePayment'])
        self.buildItemsList()
        
    def getTotal(self):
        total = 0
        for order in self.order:
            total += order.total

        return total

    def finishOrder(self):
        self.dayMeta.orderNumber += 1
        self.dayMeta.dailyTotal += self.total
        self.order = []
        self.itemSize = 1
        self.buildItemsList()
    
    def closePayment(self):
        _widgets = self.paymentWindow.frame.winfo_children()
        for i in _widgets:
            if i.winfo_children():
                i.destroy()
        self.paymentWindow.frame.pack_forget()
        self.paymentWindow.showMain()
        self.paymentWindow = None