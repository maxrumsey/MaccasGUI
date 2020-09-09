"""GUIManager

This contains the GUIManager class"""

import tkinter as tk

class GUIManager:
    """This class handles the item buttons, and their relevant actions"""

    def __init__(self, rows_num, manager, item_frame):
        self.rows_num = rows_num
        self.manager = manager
        self.item_frame = item_frame
        self.rows = list()
        self.row_names = list()
        self.prices = False

        children_dict = dict(item_frame.children)
        for child in children_dict:
            item_frame.children[child].destroy()

        for x in range(0, rows_num):
            row = tk.Frame(self.item_frame, width=700, height=75, bg="yellow")
            row.pack()
            self.rows.insert(len(self.rows), row)
            self.row_names.append(list())

    def add_item(self, row, name):
        """This method adds a button to the ordering frame"""

        b = tk.Button(self.rows[row], command= self.item_button_handler(name), text=name, width=8, height=4)
        b.pack(side=tk.LEFT)
        self.row_names[row].append((b, name))

    def item_button_handler(self, name):
        """This is a wrapper for the button press command function"""

        def func():
            self.manager.add_item(name)

        return func

    def show_prices(self):
        """This method toggles the 'Show Prices' mode of the POS"""

        for row in self.rows:
            for btext in row.children:
                button = row.children[btext]
                text = self.get_text_of_button(button)

                if text != "":
                    if not self.prices:
                        button.configure(text=text + "\n${0:.2f}".format(self.manager.prices[text]))

                    else:
                        button.configure(text=text.split("\n")[0])

        self.prices = not self.prices

    def get_text_of_button(self, button):
        """This returns the text of a certain button"""

        for row in self.row_names:
            for button_tuple in row:
                if button_tuple[0] == button:
                    return button_tuple[1]

        return ""
