import tkinter as tk

class GUIManager:
    def __init__(self, rowsNum, manager, itemFrame):
        self.rowsNum = rowsNum
        self.manager = manager
        self.itemFrame = itemFrame
        self.rows = list()
        self.prices = False

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

    def showPrices(self):
        for row in self.rows:
            for btext in row.children:
                button = row.children[btext]
                if not self.prices:
                    button.text =  button.text + "\n$15.50"

                else:
                    button.text =  button.text.split("\n")[0]