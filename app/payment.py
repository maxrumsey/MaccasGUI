import sys
sys.path.append('..')
from gui import paymentGUI

class PaymentWindow:
    def __init__(self, manager, frame):
        self.manager = manager
        self.frame = frame

        self.hideMain()
        self.gui = paymentGUI.GUI(frame, self)
        self.tendered = 0
        self.total = manager.getTotal()
        self.frozen = False
        self.keyPadInput = ""
        self.remaining = self.total
        self.buildKeyPadScreen()

    def registerKeyPad(self, widget):
        self.keyPadText = widget

    def hideMain(self):
        self.manager.window.children['frameInput'].pack_forget()

    def tender(self, amount):
        if self.frozen:
            return

        self.tendered += amount

        if self.tendered >= self.total:
            self.openDrawer()

        self.remaining = self.total - self.tendered

        if self.remaining < 0:
            self.remaining = 0

        self.buildKeyPadScreen()

    def openDrawer(self):
        self.frozen = True
        self.changeLabel.configure(text="Change:\n${0:.2f}".format(self.tendered - self.total))
        self.receiptLabel.configure(text="Sales Receipt:\nTODO")
    
    def buildKeyPadScreen(self):
        self.keyPadText.configure(text=
            "Tendered: ${0:.2f}\nRemaining: ${1:.2f}\n Entered: {2}".format(
            self.tendered, self.remaining, self.keyPadInput)
        )
    
    def cancel(self):
        if self.frozen:
            return

        self.keyPadInput = ""
        self.buildKeyPadScreen()

    def enter(self):
        if self.frozen:
            self.manager.finishOrder()
            self.manager.closePayment()
        if len(self.keyPadInput) == 0:
            self.tender(self.total)
        else:
            amount = 0

            try:
                amount = float(self.keyPadInput)
            except ValueError:
                return

            self.keyPadInput = ""
            self.tender(amount)
    
    def modify(self):
        print(1)
            


    

