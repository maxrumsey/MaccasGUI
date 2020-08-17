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
        self.keyPadText = None

    def hideMain(self):
        self.manager.window.children['frameInput'].pack_forget()

    def tender(self, amount):
        if self.frozen:
            return

        self.tendered += amount

        if self.tendered >= self.total:
            self.openDrawer()

    def openDrawer(self):
        self.frozen = True

    

