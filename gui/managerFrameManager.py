import tkinter as tk


def buildEntry(row, col, width, text, owner):
    b = tk.Entry(owner, text='', width=width)
    b.insert(tk.END, text)
    b.grid(row=row, column=col)

def base(managerFrame, manager):

    leftFrame = tk.Frame(managerFrame, width=400, height=1000, name="leftFrame")
    leftFrame.pack(side=tk.LEFT)

    rightFrame = tk.Frame(managerFrame, width=800, height=1000, name="leftInput")
    rightFrame.pack(side=tk.LEFT, anchor='nw')

    tk.Button(leftFrame, text="Return", width=45, height=8, command=manager.returnMain).pack()
    tk.Button(leftFrame, text="Test", width=45, height=8, command=manager.test).pack()

    items = manager.manager.prices
    metaList = manager.manager.dayMeta.log
    i = 0

    buildEntry(i, 0, 45, "Item Name", rightFrame)
    buildEntry(i, 1, 10, "Small", rightFrame)
    buildEntry(i, 2, 10, "Medium", rightFrame)
    buildEntry(i, 3, 10, "Large", rightFrame)

    for item in items:
        i += 1

        buildEntry(i, 0, 45, item, rightFrame)
        buildEntry(i, 1, 10, metaList[item][0], rightFrame)
        buildEntry(i, 2, 10, metaList[item][1], rightFrame)
        buildEntry(i, 3, 10, metaList[item][2], rightFrame)



    




