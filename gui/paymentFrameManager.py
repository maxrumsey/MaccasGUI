import tkinter as tk

exactChangeText = (
    (20, 50),
    (5, 10),
    (1, 2)
)

def base(paymentFrame, paymentManager):

    def exactCash(amount):
        def func():
            paymentManager.tender(amount)

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
            tk.Button(exactRow, text="$" + str(amount), command=exactCash(amount)).pack(side=tk.LEFT)
    
    keyPadText = tk.Label(keypadFrame, text="Tendered: $0.00\nRemaining: $0.00\nEntered: ")
    keyPadText.pack()

    paymentManager.keypadText = keyPadText

