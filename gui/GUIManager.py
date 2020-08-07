import tkinter as tk

class GUIManager:
    def __init__(self, rowsNum, manager, itemFrame):
        self.rowsNum = rowsNum
        self.manager = manager
        self.itemFrame = itemFrame
        self.rows = list()
        self.rowNames = list()
        self.prices = False

        childrenDict = dict(itemFrame.children)
        for w in childrenDict:
            itemFrame.children[w].destroy()

        for x in range(0, rowsNum):
            row = tk.Frame(self.itemFrame, width=700, height=75, bg="yellow")
            row.pack()
            self.rows.insert(len(self.rows), row)
            self.rowNames.append(list())

    def addItem(self, row, name):
        b = tk.Button(self.rows[row], command= self.itemButtonHandler(name), text=name, width=8, height=4)
        b.pack(side=tk.LEFT)
        self.rowNames[row].append((b, name))

    def itemButtonHandler(self, name):
        def func():
            self.manager.addItem(name)

        return func

    def showPrices(self):
        for row in self.rows:
            for btext in row.children:
                button = row.children[btext]
                text = self.getTextOfButton(button)
                
                if not self.prices:
                    button.configure(text =  text + "\n$15.50")

                else:
                    button.configure(text =  text.split("\n")[0])
                
        self.prices = not self.prices
    
    def getTextOfButton(self, b):
        for row in self.rowNames:
            for buttonTuple in row:
                if buttonTuple[0] == b:
                    return buttonTuple[1]