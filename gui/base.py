"""This module handles the creation of the base POS layout"""

import tkinter as tk
from gui import inputFrameManager

def main_gui(window, manager):
    """This function creates the top-most POS frames"""

    # Base GUIs
    order_frame = tk.Frame(window, width=400, height=1000, name="frameOrder")
    order_frame.pack(side=tk.LEFT)

    input_frame = tk.Frame(window, width=800, height=1000, name="frameInput")
    input_frame.pack(side=tk.LEFT, anchor='nw')

    tk.Frame(window, width=800, height=1000, name="framePayment")
    #"1163x730"
    tk.Frame(window, width=1163, height=730, name="frameManager")

    # Order Frames
    order_frame.pack_propagate(0)

    manager.order_list = tk.Listbox(order_frame, selectmode=tk.SINGLE, name='orderList', width=45, height=33)
    manager.order_list.pack()

    info_box = tk.Frame(order_frame)
    info_box.pack()

    item_array = [
        ("Order #", "00"),
        ("SubTotal", "$0.00"),
        ("GST", "$0.00"),
        ("Surcharge", "$0.00"),
        ("Total", "$0.00"),
        ("Daily Total", "$0.00")
    ]

    for i in range(6):
        for j in range(2):
            entry = tk.Entry(info_box)
            entry.grid(row=i, column=j)
            entry.insert(tk.END, item_array[i][j])

            if j == 1:
                manager.order_detail_table[item_array[i][0]] = entry

    # Input Frames
    inputFrameManager.base(input_frame, manager)
