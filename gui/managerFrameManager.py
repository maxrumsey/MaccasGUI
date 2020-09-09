"""This module manages all aspects of the Manager Menu GUI"""

import tkinter as tk


def build_entry(row, col, width, text, owner):
    """This adds a value to a Tkinter Table cell"""

    entry = tk.Entry(owner, text='', width=width)
    entry.insert(tk.END, text)
    entry.grid(row=row, column=col)

def base(manager_frame, manager):
    """This builds the manager frame menu"""

    left_frame = tk.Frame(manager_frame, width=400, height=1000, name="leftFrame")
    left_frame.pack(side=tk.LEFT)

    right_frame = tk.Frame(manager_frame, width=800, height=1000, name="leftInput")
    right_frame.pack(side=tk.LEFT, anchor='nw')

    tk.Button(left_frame, text="Return", width=45, height=8, command=manager.show_main).pack()
    tk.Button(left_frame, text="Test", width=45, height=8, command=manager.test).pack()

    items = manager.manager.prices
    day_meta = manager.manager.day_meta
    meta_list = day_meta.log
    i = 0

    build_entry(i, 0, 45, "Item Name", right_frame)
    build_entry(i, 1, 10, "Small", right_frame)
    build_entry(i, 2, 10, "Medium", right_frame)
    build_entry(i, 3, 10, "Large", right_frame)

    for item in items:
        i += 1

        build_entry(i, 0, 45, item, right_frame)
        build_entry(i, 1, 10, meta_list[item][0], right_frame)
        build_entry(i, 2, 10, meta_list[item][1], right_frame)
        build_entry(i, 3, 10, meta_list[item][2], right_frame)

    info_box = tk.Frame(left_frame)
    info_box.pack()

    small = 0
    medium = 0
    large = 0

    for item in meta_list:
        small += meta_list[item][0]
        medium += meta_list[item][1]
        large += meta_list[item][2]

    info_array = [
        ("DineIn Orders", "{:0>3d}".format(day_meta.dinein)),
        ("TakeAway Orders", "{:0>3d}".format(day_meta.takeaway)),
        ("Total Num", "{:0>3d}".format(day_meta.dinein + day_meta.takeaway)),
        ("Cups", "{:0>3d}|{:0>3d}|{:0>3d}".format(small, medium, large)),
        ("GST", "${:0.2f}".format(day_meta.gst)),
        ("Daily Total", "${:0.2f}".format(day_meta.daily_total))
    ]

    for i in range(6):
        for j in range(2):
            entry = tk.Entry(info_box, font='TkFixedFont', width=28)
            entry.grid(row=i, column=j)
            entry.insert(tk.END, info_array[i][j])
