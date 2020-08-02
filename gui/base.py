import tkinter as tk
from gui import inputFrameManager

def mainGUI(window, manager):
    # Base GUIs
    orderFrame = tk.Frame(window, width=400, height=1000, name="frameOrder", bg="red")
    orderFrame.pack(side=tk.LEFT)

    inputFrame = tk.Frame(window, width=800, height=1000, name="frameInput", bg="green")
    inputFrame.pack(side=tk.LEFT, anchor='nw')

    # Order Frames
    orderFrame.pack_propagate(0)

    tk.Label(orderFrame, bg="white",fg="black",text="test",font=("Calibri",15)).pack()

    # Input Frames
    inputFrameManager.base(inputFrame, manager)

