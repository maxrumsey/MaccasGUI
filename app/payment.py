import sys
sys.path.append('..')
from gui import paymentGUI

class PaymentWindow:
    def __init__(self, manager, frame):
        self.manager = manager
        self.frame = frame

        self.hideMain()
        self.gui = paymentGUI.GUI(frame, self)

    def hideMain(self):
        self.manager.window.children['frameInput'].pack_forget()



