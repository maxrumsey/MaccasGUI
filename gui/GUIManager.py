import tkinter as tk

class GUIManager:
    def __init__(self, rowsNum, manager, itemFrame):
        self.rowsNum = rowsNum
        self.manager = manager
        self.itemFrame = itemFrame
        self.rows = list()

        childrenDict = dict(itemFrame.children)
        for w in childrenDict:
            itemFrame.children[w].destroy()

        for x in range(0, rowsNum):
            row = tk.Frame(self.itemFrame, width=700, height=75, bg="yellow")
            row.pack()
            self.rows.insert(len(self.rows), row)

    def addItem(self, row, name):
        tk.Button(self.rows[row], command= self.itemButtonHandler(name), text=name, width=8, height=4).pack(side=tk.LEFT)

    def itemButtonHandler(self, name):
        def func():
            self.manager.addItem(name)

        return func

    