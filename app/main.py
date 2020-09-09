"""Main Manager

This contains the class responsible for handling the application.
"""

import sys
import tkinter as tk
from app import item
from app import payment
from app import manager
from app import day_meta
sys.path.append('..')

# pylint: disable=import-error wrong-import-position
from gui import base
from gui.cats import coffee

size_enum = [
    ("Small", 0.9),
    ("Medium", 1),
    ("Large", 1.2)
]

class Main:
    """This class handles all logic aspects of the application"""

    def __init__(self, window, prices):
        self.prices = prices
        self.window = window
        self.window.geometry("1163x730")
        self.item_size = 1
        self.number_input = ""
        self.order = []
        self.order_list = None
        self.gui = None
        self.payment_window = None
        self.manager_window = None
        self.order_detail_table = {}
        self.day_meta = day_meta.DayMeta(self)
        self.total = 0
        self.take_out = False

    def start(self):
        """Starts the Application, Loading Layouts"""

        base.main_gui(self.window, self)
        left_frame = self.window.children['frameInput'].children['leftFrame']
        coffee.build(self, left_frame.children['itemBoard'])
        self.window.mainloop()

    def add_item(self, name):
        """Adds item to the order list"""

        if not name:
            return

        price = self.prices[name] * size_enum[self.item_size][1]

        init_item = item.Item(name, 1, price, size_enum[self.item_size][0], self.item_size)

        self.item_size = 1

        number = 1
        number_set = False
        if self.number_input != "":
            number = int(self.number_input)
            init_item.set_amount(number)
            self.number_input = ""
            number_set = True

        cursor_index = self.order_list.curselection()

        found = False
        for inx, val in enumerate(self.order):
            if (val.name == init_item.name and
                    val.size == init_item.size and
                    val.price == init_item.price):
                found = True
                if (len(cursor_index) != 0 and
                        number_set and
                        cursor_index[0] == inx):
                    if init_item.amount == 0:
                        self.order.pop(inx)
                    else:
                        val.set_amount(init_item.amount)

                    break

                else:
                    init_item.set_amount(init_item.amount + val.amount)

                self.order.remove(val)
                if init_item.amount != 0:
                    self.order.insert(inx, init_item)

                break

        if (not found and
                init_item.amount != 0):
            self.order.append(init_item)

        self.build_items_list()

    def get_totals(self):
        """Returns numerical information about the order."""

        subtotal = self.get_subtotal()
        gst = subtotal * .1
        surcharge = 0
        if self.take_out:
            surcharge = (subtotal + gst) * 0.05

        self.total = self.round_to(subtotal + gst + surcharge, 0.05)

        return (subtotal, gst, surcharge, self.total)

    def round_to(self, amount, precision):
        """Rounds a numerical value to a value appropriate for monetary use"""

        correction = 0.5 if amount >= 0 else -0.5
        return int(amount/precision+correction) * precision

    def build_items_list(self):
        """Constructs the item list, and total box"""

        self.order_list.delete(0, tk.END)
        for item in self.order:
            txt = "{amount} {size} {name} == {price:0.2f}"
            final = txt.format(amount=item.amount, size=item.size, name=item.name, price=item.total)
            self.order_list.insert(tk.END, final)

        if self.take_out:
            self.order_list.insert(tk.END, "---Take Out---")

        self.order_list.selection_set(0)

        totals = self.get_totals()

        self.set_order_table("SubTotal", "${0:0.2f}".format(totals[0]))
        self.set_order_table("Surcharge", "${0:0.2f}".format(totals[2]))
        self.set_order_table("GST", "${0:0.2f}".format(totals[1]))
        self.set_order_table("Order #", self.day_meta.get_order_num())
        self.set_order_table("Total", "${0:0.2f}".format(totals[3]))
        self.set_order_table("Daily Total", "${0:0.2f}".format(self.day_meta.daily_total))

    def set_order_table(self, key, value):
        """Sets an entry in a TKinter table to a specific value"""

        self.order_detail_table[key].delete(0, tk.END)
        self.order_detail_table[key].insert(0, value)

    def void_item(self, index):
        """Pops the item from the order array"""

        self.order.pop(index)

    def void_item_press(self):
        """Handles the pressing of the void item button press"""

        list_box = self.order_list
        self.number_input = ""
        if len(list_box.curselection()) == 0:
            return

        index = list_box.curselection()[0]
        if (self.take_out and index == len(self.order)):
            self.take_out = False
            self.build_items_list()
            return

        if index is not None:
            order = self.order[index]
            amount = order.amount

            if amount > 1:
                order.set_amount(amount-1)

            else:
                self.order.pop(index)

            self.build_items_list()

            list_box.selection_clear(first=True)
            list_box.selection_set(index)

    def pay(self):
        """Handles the pressing of the Payment button"""

        if len(self.order) == 0:
            return
        self.payment_window = payment.PaymentWindow(self, self.window.children['framePayment'])
        self.build_items_list()

    def manager(self):
        """Handles the pressing of the manager window button"""

        self.manager_window = manager.ManagerWindow(self, self.window.children['frameManager'])

    def get_subtotal(self):
        """Calculates the order's subtotal"""

        total = 0
        for order in self.order:
            total += order.total

        return total

    def finish_order(self):
        """Removes all information about the current order, to start anew"""

        gst = self.get_totals()[1]
        if self.take_out:
            self.day_meta.takeaway += 1
        else:
            self.day_meta.dinein += 1

        self.day_meta.gst += gst


        for itemObj in self.order:
            self.day_meta.log[itemObj.name][itemObj.size_int] += itemObj.amount

        self.day_meta.order_number += 1
        self.day_meta.daily_total += self.total
        self.order = []
        self.item_size = 1
        self.take_out = False
        self.build_items_list()

    def close_payment(self):
        """Closes the Payment Window"""

        _widgets = self.payment_window.frame.winfo_children()
        for i in _widgets:
            if i.winfo_children():
                i.destroy()
        self.payment_window.frame.pack_forget()
        self.payment_window.show_main()
        self.payment_window = None

    def promo(self):
        """Handles the pressing of the promo button"""

        list_box = self.order_list

        if len(list_box.curselection()) == 0:
            return


        index = list_box.curselection()[0]

        if len(self.order) == index:
            return

        self.order[index].promo()
        self.build_items_list()
