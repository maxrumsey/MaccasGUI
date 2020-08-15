from gui import paymentFrameManager

class GUI:
    def __init__(self, frame, manager):
        self.frame = frame
        self.manager = manager
        
        paymentFrameManager.base(frame, manager)
        
