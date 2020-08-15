import tkinter as tk
from gui import inputFrameManager

def mainGUI(window, manager):
    # Base GUIs
    orderFrame = tk.Frame(window, width=400, height=1000, name="frameOrder", bg="red")
    orderFrame.pack(side=tk.LEFT)

    inputFrame = tk.Frame(window, width=800, height=1000, name="frameInput", bg="green")
    inputFrame.pack(side=tk.LEFT, anchor='nw')

    paymentFrame = tk.Frame(window, width=800, height=1000, name="framePayment", bg="red")


    # Order Frames
    orderFrame.pack_propagate(0)

    manager.orderList = tk.Listbox(orderFrame, selectmode=tk.SINGLE, name='orderList', width=45, height=47)
    manager.orderList.pack()

    # Input Frames
    inputFrameManager.base(inputFrame, manager)


