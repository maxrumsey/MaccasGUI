import tkinter as tk

def base(inputFrame, manager):

    def numButClick(b):
        def func():
            manager.numberInput += str(b)

        return func

    def catChange(type):
        def func():
            manager.setCat(type)

        return func

    infoBoard = tk.Frame(inputFrame, width=800, height=100, name="infoBoard", bg="red")
    infoBoard.pack()

    tk.Label(infoBoard, text="Maxim Rumsey").pack()

    numberInput = tk.Frame(inputFrame, width=800, height=100, name="numberInput", bg="blue")
    numberInput.pack()

    orderCategories = tk.Frame(inputFrame, width=800, height=100, name="orderCat", bg="yellow")
    orderCategories.pack()

    # Food Categories
    tk.Button(orderCategories, command=catChange("Coffee"), text="Coffee", width=8, height=4).pack(side=tk.LEFT)
    tk.Button(orderCategories, command=catChange("Lunch"), text="Lunch", width=8, height=4).pack(side=tk.LEFT)
    tk.Button(orderCategories, command=catChange("Dessert"), text="Dessert", width=8, height=4).pack(side=tk.LEFT)
    tk.Button(orderCategories, command=catChange("Condiments"), text="Condiments", width=8, height=4).pack(side=tk.LEFT)
    for x in range(0, 5):
        tk.Button(orderCategories, text="", width=8, height=4).pack(side=tk.LEFT)

    tk.Button(orderCategories, width=8, height=4, text="Void Line").pack(side=tk.LEFT)

    for x in range(0,10):
        tk.Button(numberInput, command=numButClick(x), text=str(x), width=8, height=4).pack(side=tk.LEFT)
    
    leftFrame = tk.Frame(inputFrame, width=800, height=225, name="leftFrame")
    leftFrame.pack(side=tk.TOP)

    itemBoard = tk.Frame(leftFrame, width=700, height=225, name="itemBoard", bg="yellow")
    itemBoard.pack(side=tk.LEFT)

    specialBoard = tk.Frame(leftFrame, width=100, height=500, name="specialBoard", bg="blue")
    specialBoard.pack(side=tk.RIGHT)

    # Special Categories
    tk.Button(specialBoard, width=8, height=4, text="Promo\nItem").pack()
    tk.Button(specialBoard, width=8, height=4, text="Clear\nChoice").pack()
    tk.Button(specialBoard, width=8, height=4, text="Special\nFunction").pack()


    sizeBoard = tk.Frame(inputFrame, width=800, height=200, name="sizeBoard", bg="blue")
    sizeBoard.pack()

    # Size Categories
    tk.Button(sizeBoard, width=8, height=4, text="Small").pack(side=tk.LEFT)
    tk.Button(sizeBoard, width=8, height=4, text="Medium").pack(side=tk.LEFT)
    tk.Button(sizeBoard, width=8, height=4, text="Large").pack(side=tk.LEFT)
    for x in range(0, 3):
        tk.Button(sizeBoard, text="", width=8, height=4).pack(side=tk.LEFT)
    tk.Button(sizeBoard, width=8, height=4, text="Show\nPrices").pack(side=tk.LEFT)
    tk.Button(sizeBoard, width=8, height=4, text="Manager", highlightbackground="red", fg="green").pack(side=tk.LEFT)
    tk.Button(sizeBoard, width=16, height=4, text="Take\nOut", highlightbackground="red", fg="green").pack(side=tk.LEFT)




