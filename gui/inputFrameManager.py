import tkinter as tk

def base(inputFrame, manager):

    def numButClick(b):
        def func():
            manager.numberInput += str(b)

        return func

    def takeOut():
        manager.takeOut = True
        manager.buildItemsList()

    infoBoard = tk.Frame(inputFrame, width=800, height=100, name="infoBoard", bg="red")
    infoBoard.pack()

    tk.Label(infoBoard, text="Maxim Rumsey").pack()

    numberInput = tk.Frame(inputFrame, width=800, height=100, name="numberInput", bg="blue")
    numberInput.pack()

    for x in range(0,10):
        tk.Button(numberInput, command=numButClick(x), text=str(x), width=8, height=4).pack(side=tk.LEFT)
    
    leftFrame = tk.Frame(inputFrame, width=800, height=225, name="leftFrame")
    leftFrame.pack(side=tk.TOP)

    itemBoard = tk.Frame(leftFrame, width=700, height=225, name="itemBoard", bg="yellow")
    itemBoard.pack(side=tk.LEFT)

    specialBoard = tk.Frame(leftFrame, width=100, height=500, name="specialBoard", bg="blue")
    specialBoard.pack(side=tk.RIGHT)

    # Special Categories
    tk.Button(specialBoard, width=8, height=4, text="Promo\nItem", command=manager.promo).pack()
    tk.Button(specialBoard, width=8, height=4, text="Void Line", command=manager.voidItemPress).pack()
    tk.Button(specialBoard, width=8, height=4, text="Take Out", command=takeOut).pack()


    sizeBoard = tk.Frame(inputFrame, width=800, height=200, name="sizeBoard", bg="blue")
    sizeBoard.pack()


    def getShowPricesButton():
        manager.gui.showPrices()

    def setSize(level):
        def func():
            manager.itemSize = level

        return func

    # Size Categories
    tk.Button(sizeBoard, width=16, height=4, text="Small", command=setSize(0)).pack(side=tk.LEFT)
    tk.Button(sizeBoard, width=16, height=4, text="Medium", command=setSize(1)).pack(side=tk.LEFT)
    tk.Button(sizeBoard, width=16, height=4, text="Large", command=setSize(2)).pack(side=tk.LEFT)

    tk.Button(sizeBoard, width=8, height=4, text="Show\nPrices", command=getShowPricesButton).pack(side=tk.LEFT)
    tk.Button(sizeBoard, width=10, height=4, text="Manager", highlightbackground="red", fg="green", command=manager.manager).pack(side=tk.LEFT)
    tk.Button(sizeBoard, width=16, height=4, text="Pay", command=manager.pay, highlightbackground="red", fg="green").pack(side=tk.LEFT)


        

