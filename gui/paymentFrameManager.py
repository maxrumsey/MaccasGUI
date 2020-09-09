"""Contains the payment frame input layout manager"""

import tkinter as tk

exact_change_text = (
    (20, 50),
    (5, 10),
    (1, 2)
)

keypad_text_arr = (
    (7, 8, 9),
    (4, 5, 6),
    (1, 2, 3),
    ("CANC", 0, ".", "ETR")
)

def base(payment_frame, payment_manager):
    """Creates the keypad frame and receipt label frame."""

    def exact_cash(amount):
        def func():
            payment_manager.tender(amount)

        return func

    def keypad_press(key):
        def func():
            if not payment_manager.frozen:
                if isinstance(key, int) or key == ".":
                    payment_manager.keypad_input += str(key)
                    payment_manager.build_keypad_screen()
                elif key == "CANC":
                    payment_manager.cancel()
            if key == "ETR":
                payment_manager.enter()

        return func

    # Main Frames
    keypad_frame = tk.Frame(payment_frame, width=400, name="keypadFrame")
    keypad_frame.pack(side=tk.LEFT)

    receipt_frame = tk.Frame(payment_frame, width=400, name="receiptFrame")
    receipt_frame.pack(side=tk.LEFT)

    # KeyPad
    for row in range(0, 3):
        exact_row = tk.Frame(keypad_frame, width=400)
        exact_row.pack()
        for col in range(0, 2):
            amount = exact_change_text[row][col]
            tk.Button(exact_row, text="$" + str(amount), height=5, width=18, command=exact_cash(amount)).pack(side=tk.LEFT)

    base_keypad_text = "Tendered: $0.00\nRemaining: $0.00\nEntered: "
    keypad_text = tk.Label(keypad_frame, text=base_keypad_text, font=("Helvetica", 20, "bold"), justify="left", anchor="w")
    keypad_text.pack(fill="both")

    payment_manager.register_keypad(keypad_text)

    for row in range(0, 4):
        row_frame = tk.Frame(keypad_frame)
        row_frame.pack()
        final = 3
        if row == 3:
            final = 4
        for col in range(0, final):
            text = keypad_text_arr[row][col]
            tk.Button(row_frame, text=str(text), height=6, width=int(36/final), command=keypad_press(text)).pack(side=tk.LEFT)

    # Receipt

    rec_label = tk.Label(receipt_frame, width=45, justify="left", anchor="nw", height=43)
    rec_label.pack()
    payment_manager.receipt_label = rec_label

    rec_modify = tk.Button(receipt_frame, text="Modify Order", width=45, height=5, command=payment_manager.modify)
    rec_modify.pack()
