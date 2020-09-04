import sys
import tkinter as tk
from app import test
sys.path.append('..')
from gui import managerGUI

class ManagerWindow:
    def __init__(self, manager, frame):
        self.manager = manager
        self.frame = frame
        self.hideMain()
        self.gui = managerGUI.GUI(frame, self)
    
    def hideMain(self):
        self.manager.window.children['frameInput'].pack_forget()
        self.manager.window.children['frameOrder'].pack_forget()
    def showMain(self):
        self.manager.window.children['frameOrder'].pack(side=tk.LEFT)
        self.manager.window.children['frameInput'].pack(side=tk.LEFT, anchor='nw')
        self.manager.window.children['frameManager'].pack_forget()

        for child in self.frame.winfo_children():
            child.destroy()
        
        self.manager.closeManager()

    def returnMain(self):
        self.showMain()

    def test(self):
        self.testMod = test.Tester(self, './order_out.csv')
        self.testMod.readCSV('./daily_orders.csv')
        self.testMod.loop()