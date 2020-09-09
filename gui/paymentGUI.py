"""This contains the Payment GUI controller class"""

from gui import paymentFrameManager

class GUI:
    """This class controls the payment Frame"""

    def __init__(self, frame, manager):
        self.frame = frame
        self.manager = manager

        paymentFrameManager.base(frame, manager)

        frame.pack()
