"""This module is responsible for creating the Order Input Frames"""

import tkinter as tk
import pwd
import os
from datetime import datetime

size_enum = (
    "Small",
    "Medium",
    "Large"
)

def base(input_frame, manager):
    """This function creates the order input frame, and related frames / features"""

    def num_button_click(button):
        def func():
            manager.number_input += str(button)

        return func

    def take_out():
        manager.take_out = True
        manager.build_items_list()

    info_board = tk.Frame(input_frame, width=800, height=100, name="infoBoard")
    info_board.pack()

    pad_amount = 50

    def get_username():
        return pwd.getpwuid(os.getuid())[0]

    tk.Label(info_board, text=get_username()).pack(side=tk.LEFT, padx=pad_amount)
    size_label = tk.Label(info_board, text="Size", name="size")
    size_label.pack(side=tk.LEFT, padx=pad_amount)

    amount_label = tk.Label(info_board, text="Amount", name="amount")
    amount_label.pack(side=tk.LEFT, padx=pad_amount)

    time_label = tk.Label(info_board, text="Time", name="time")
    time_label.pack(side=tk.LEFT, padx=pad_amount)

    def update_info():
        time = datetime.now()
        time_label.configure(text=str(time).split('.')[0])
        amount_label.configure(text=str(manager.number_input))
        size_label.configure(text=size_enum[manager.item_size])

        manager.window.after(200, update_info)

    update_info()

    number_input = tk.Frame(input_frame, width=800, height=100, name="numberInput", bg="blue")
    number_input.pack()

    for number in range(0,10):
        tk.Button(number_input, command=num_button_click(number), text=str(number), width=8, height=4).pack(side=tk.LEFT)

    left_frame = tk.Frame(input_frame, width=800, height=225, name="leftFrame")
    left_frame.pack(side=tk.TOP)

    item_board = tk.Frame(left_frame, width=700, height=225, name="itemBoard", bg="yellow")
    item_board.pack(side=tk.LEFT)

    special_board = tk.Frame(left_frame, width=100, height=500, name="specialBoard", bg="blue")
    special_board.pack(side=tk.RIGHT)

    # Special Categories
    tk.Button(special_board, width=8, height=4, text="Promo\nItem", command=manager.promo).pack()
    tk.Button(special_board, width=8, height=4, text="Void Line", command=manager.void_item_press).pack()
    tk.Button(special_board, width=8, height=4, text="Take Out", command=take_out).pack()


    size_board = tk.Frame(input_frame, width=800, height=200, name="sizeBoard", bg="blue")
    size_board.pack()


    def get_show_prices_button():
        manager.gui.show_prices()

    def set_size(level):
        def func():
            manager.item_size = level

        return func

    # Size Categories
    tk.Button(size_board, width=16, height=4, text="Small", command=set_size(0)).pack(side=tk.LEFT)
    tk.Button(size_board, width=16, height=4, text="Medium", command=set_size(1)).pack(side=tk.LEFT)
    tk.Button(size_board, width=16, height=4, text="Large", command=set_size(2)).pack(side=tk.LEFT)

    tk.Button(size_board, width=8, height=4, text="Show\nPrices", command=get_show_prices_button).pack(side=tk.LEFT)
    tk.Button(size_board, width=10, height=4, text="Manager", highlightbackground="red", fg="green", command=manager.manager).pack(side=tk.LEFT)
    tk.Button(size_board, width=16, height=4, text="Pay", command=manager.pay, highlightbackground="red", fg="green").pack(side=tk.LEFT)
