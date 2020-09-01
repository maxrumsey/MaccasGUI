import tkinter as tk

exactChangeText = (
    (20, 50),
    (5, 10),
    (1, 2)
)

keyPadTextArr = (
    (7, 8, 9),
    (4, 5, 6),
    (1, 2, 3),
    ("CANC", 0, ".", "ETR")
)

def base(paymentFrame, paymentManager):

    def exactCash(amount):
        def func():
            paymentManager.tender(amount)

        return func

    def keyPadPress(x):
        def func():
            if paymentManager.frozen == False:
                if isinstance(x, int) or x == ".":
                    paymentManager.keyPadInput += str(x)
                    paymentManager.buildKeyPadScreen()
                elif x == "CANC":
                    paymentManager.cancel()
            if x == "ETR":
                paymentManager.enter()
                

        return func

    # Main Frames
    keypadFrame = tk.Frame(paymentFrame, width=400, name="keypadFrame")
    keypadFrame.pack(side=tk.LEFT)

    receiptFrame = tk.Frame(paymentFrame, width=400, name="receiptFrame")
    receiptFrame.pack(side=tk.LEFT)

    # KeyPad
    for row in range(0, 3):
        exactRow = tk.Frame(keypadFrame, width=400)
        exactRow.pack()
        for col in range(0, 2):
            amount = exactChangeText[row][col]
            tk.Button(exactRow, text="$" + str(amount), height=5, width=18, command=exactCash(amount)).pack(side=tk.LEFT)
    
    keyPadText = tk.Label(keypadFrame, text="Tendered: $0.00\nRemaining: $0.00\nEntered: ", font=("Helvetica", 20, "bold"), justify="left", anchor="w")
    keyPadText.pack(fill="both")

    paymentManager.registerKeyPad(keyPadText)

    for row in range(0, 4):
        rowFrame = tk.Frame(keypadFrame)
        rowFrame.pack()
        final = 3
        if row == 3:
            final = 4
        for col in range(0, final):
            text = keyPadTextArr[row][col]
            tk.Button(rowFrame, text=str(text), height=6, width=int(36/final), command=keyPadPress(text)).pack(side=tk.LEFT)
    
    # Receipt

    recLabel = tk.Label(receiptFrame,width=45, justify="left", anchor="nw", height=43)
    recLabel.pack()
    paymentManager.receiptLabel = recLabel

    recModify = tk.Button(receiptFrame, text="Modify Order", width=45, height=5, command=paymentManager.modify)
    recModify.pack()




