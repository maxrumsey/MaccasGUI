import sys
import tkinter as tk
from app import item
from app import payment
from app import manager
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
    def __init__(self, window, prices):
        self.prices = prices
        self.window = window
        self.window.geometry("1163x730")
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
        coffee.set(self, self.window.children['frameInput'].children['leftFrame'].children['itemBoard'])
        self.window.mainloop()

    def addItem(self, name):
        if not name:
            return
        
        initItem = item.Item(name, 1, self.prices[name] * sizeEnum[self.itemSize][1], sizeEnum[self.itemSize][0], self.itemSize)

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
    
    def getTotals(self):
        subtotal = self.getTotal()
        GST = (subtotal / .9) * .1
        surcharge = 0
        if (self.takeOut == True):
            surcharge = (subtotal + GST) * 0.05
        self.total = self.round_to(subtotal + GST + surcharge, 0.05)

        return (subtotal, GST, surcharge, self.total)

    def round_to(self, n, precision):
        correction = 0.5 if n >= 0 else -0.5
        return int( n/precision+correction ) * precision

    def buildItemsList(self):
        self.orderList.delete(0, tk.END)
        for item in self.order:
            txt = "{amount} {size} {name} == {price:0.2f}"
            self.orderList.insert(tk.END, txt.format(amount=item.amount,size=item.size, name=item.name, price=item.total))
        
        if (self.takeOut == True):
            self.orderList.insert(tk.END, "---Take Out---")
                    
        self.orderList.selection_set(0)

        totals = self.getTotals()

        self.setOrderTable("SubTotal", "${0:0.2f}".format(totals[0]))
        self.setOrderTable("Surcharge", "${0:0.2f}".format(totals[2]))
        self.setOrderTable("GST", "${0:0.2f}".format(totals[1]))
        self.setOrderTable("Order #", self.dayMeta.getOrderNum())
        self.setOrderTable("Total", "${0:0.2f}".format(totals[3]))
        self.setOrderTable("Daily Total", "${0:0.2f}".format(self.dayMeta.dailyTotal))

    def setOrderTable(self, key, value):
        self.orderDetailTable[key].delete(0, tk.END)
        self.orderDetailTable[key].insert(0, value)

    def voidItem(self, index):
        self.order.pop(index)
    
    def voidItemPress(self):
        listBox = self.orderList
        self.numberInput = ""
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
    
    def manager(self):
        self.managerWindow = manager.ManagerWindow(self, self.window.children['frameManager'])
        
    def getTotal(self):
        total = 0
        for order in self.order:
            total += order.total

        return total

    def finishOrder(self):
        gst = self.getTotals()[1]
        if (self.takeOut):
            self.dayMeta.takeaway += 1
        else:
            self.dayMeta.dinein += 1
        
        self.dayMeta.gst += gst


        for item in self.order:
            self.dayMeta.log[item.name][item.sizeInt] += item.amount
        self.dayMeta.orderNumber += 1
        self.dayMeta.dailyTotal += self.total
        self.order = []
        self.itemSize = 1
        self.takeOut = False
        self.buildItemsList()
    
    def closePayment(self):
        _widgets = self.paymentWindow.frame.winfo_children()
        for i in _widgets:
            if i.winfo_children():
                i.destroy()
        self.paymentWindow.frame.pack_forget()
        self.paymentWindow.showMain()
        self.paymentWindow = None

    def promo(self):
        listBox = self.orderList

        if (len(listBox.curselection()) == 0):
            return


        index = listBox.curselection()[0]

        if (len(self.order) == index):
            return

        item = self.order[index]
        item.promo()
        self.buildItemsList()
