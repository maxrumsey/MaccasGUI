"""This contains the Manager GUI Class"""

from gui import managerFrameManager

class GUI:
    """This calls the manager frame layout method, and creates the master frame"""
    # Class is somewhat useless, should be refactored out 8/9

    def __init__(self, frame, manager):
        self.frame = frame
        self.manager = manager

        managerFrameManager.base(frame, manager)

        frame.pack(anchor="nw")
