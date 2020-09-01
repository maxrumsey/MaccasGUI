from gui import managerFrameManager

class GUI:
    def __init__(self, frame, manager):
        self.frame = frame
        self.manager = manager
        
        managerFrameManager.base(frame, manager)

        frame.pack(anchor="nw")
        
    