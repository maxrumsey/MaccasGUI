"""Manager Window

This class is reponsible for handling all the logic for the manager window.
"""

import sys
import tkinter as tk
from app import test
sys.path.append('..')

# pylint: disable=import-error wrong-import-position
from gui import managerGUI

class ManagerWindow:
    """Responsible for handling the Manager Window."""

    def __init__(self, manager, frame):
        self.manager = manager
        self.frame = frame
        self.test_mod = None
        self.hide_main()
        self.gui = managerGUI.GUI(frame, self)

    def hide_main(self):
        """Hides the main POS window frame, so only the manager window is shown"""

        self.manager.window.children['frameInput'].pack_forget()
        self.manager.window.children['frameOrder'].pack_forget()

    def show_main(self):
        """Removes the manager window, and returns to the main POS window"""

        self.manager.window.children['frameOrder'].pack(side=tk.LEFT)
        self.manager.window.children['frameInput'].pack(side=tk.LEFT, anchor='nw')
        self.manager.window.children['frameManager'].pack_forget()

        for child in self.frame.winfo_children():
            child.destroy()

    def test(self):
        """Starts and runs the tester class"""

        self.test_mod = test.Tester(self, './order_out.csv')
        self.test_mod.read_csv('./order_in.csv')
        self.test_mod.loop()
