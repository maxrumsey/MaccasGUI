"""Payment Window

This contains the class for handling the payment window.
"""

import sys
import tkinter as tk
sys.path.append('..')

# pylint: disable=import-error wrong-import-position
from gui import paymentGUI

class PaymentWindow:
    """This handles the payment window, and all of it's methods and events."""

    def __init__(self, manager, frame):
        self.manager = manager
        self.frame = frame
        self.keypad_text = None
        self.change_label = None
        self.receipt_label = None
        self.keypad_input = ""

        self.hide_main()
        self.gui = paymentGUI.GUI(frame, self)
        self.tendered = 0
        self.total = manager.total
        self.frozen = False
        self.remaining = self.total
        self.build_keypad_screen()

    def register_keypad(self, widget):
        """Initialises the keypad widget"""

        self.keypad_text = widget

    def hide_main(self):
        """Hides the main POS screen"""

        self.manager.window.children['frameInput'].pack_forget()

    def show_main(self):
        """Shows the main POS screen"""

        self.manager.window.children['frameInput'].pack(side=tk.LEFT, anchor='nw')

    def tender(self, amount):
        """Adds a set amount to the tendered cash pool"""

        if self.frozen:
            return

        self.tendered += amount

        if self.tendered >= self.total:
            self.open_drawer()

        self.remaining = self.total - self.tendered

        if self.remaining < 0:
            self.remaining = 0

        self.build_keypad_screen()

    def open_drawer(self):
        """Ends the entering of money, and performs calculations on change etc"""

        self.frozen = True
        #self.changeLabel.configure(text="Change:\n${0:.2f}".format(self.tendered - self.total))
        receipt = '''CAFE AU LAIT
=======================================
42 King Edward Rd, Osborne Park WA 6017
0416 376 667
Order Number: {ordernum}
=======================================
'''.format(ordernum=self.manager.day_meta.get_order_num())

        for item in self.manager.order:
            name_string = item.size + " " + item.name
            receipt += "{0:<2} {1:<20} == ${2:.2f}\n".format(item.amount, name_string, item.total)

        totals = self.manager.get_totals()

        receipt_footer = '''=======================================
SubTotal:  ${:.2f}
GST:       ${:.2f}
Surcharge: ${:.2f}
Total:     ${:.2f}

Tendered:  ${:.2f}
Change:    ${:.2f}
=======================================
Thanks for choosing Cafe Au Lait!'''

        change = self.tendered - self.total
        receipt += receipt_footer.format(totals[0], totals[1], totals[2], totals[3], self.tendered, change)
        self.receipt_label.configure(text=receipt, font='TkFixedFont')

    def build_keypad_screen(self):
        """Builds the keypad information window"""

        self.keypad_text.configure(text=
        "  Tendered: ${0:.2f}\n  Remaining: ${1:.2f}\n  Entered: {2}".format(
        self.tendered, self.remaining, self.keypad_input)
        )
    
    def cancel(self):
        """Voids the amount entered into the keypad"""

        if self.frozen:
            return

        self.keypad_input = ""
        self.build_keypad_screen()

    def enter(self):
        """Enters the amount entered into the keypad into the tendered pool"""

        if self.frozen:
            self.manager.finish_order()
            self.manager.close_payment()
        elif len(self.keypad_input) == 0:
            self.tender(self.total)
        else:
            amount = 0

            try:
                amount = float(self.keypad_input)
            except ValueError:
                return

            self.keypad_input = ""
            self.tender(amount)

    def modify(self):
        """Returns to the main POS screen without finalising the payment of the order"""

        if self.frozen:
            self.manager.finish_order()

        self.manager.close_payment()
