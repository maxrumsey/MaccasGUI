import tkinter as tk
from gui import inputFrameManager

def mainGUI(window, manager):
    # Base GUIs
    orderFrame = tk.Frame(window, width=400, height=1000, name="frameOrder", bg="red")
    orderFrame.pack(side=tk.LEFT)

    inputFrame = tk.Frame(window, width=800, height=1000, name="frameInput", bg="green")
    inputFrame.pack(side=tk.LEFT, anchor='nw')

    tk.Frame(window, width=800, height=1000, name="framePayment", bg="red")


    # Order Frames
    orderFrame.pack_propagate(0)

    manager.orderList = tk.Listbox(orderFrame, selectmode=tk.SINGLE, name='orderList', width=45, height=37)
    manager.orderList.pack()

    infoBox = tk.Frame(orderFrame, width=400)
    infoBox.pack()

    itemArray = [
        ("Order #", "00"),
        ("SubTotal", "$0.00"),
        ("GST", "$0.00"),
        ("Surcharge", "$0.00"),
        ("Total", "$0.00"),
        ("Daily Total", "$0.00")
    ]

    for i in range(6):
        for j in range(2):
            e = tk.Entry(infoBox)
            e.grid(row=i, column=j)
            e.insert(tk.END, itemArray[i][j])
            if (j == 1):
                manager.orderDetailTable[itemArray[i][0]] = e

    
    

    # Input Frames
    inputFrameManager.base(inputFrame, manager)


