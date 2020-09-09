"""Tester Class

This class handles testing of the program.
"""

import csv

class Tester:
    """This class is responsible for running test mode"""

    def __init__(self, manager, output):
        self.manager = manager
        self.big_manager = manager.manager
        self.order = []
        self.output_filename = output
        self.log = {
            "ORDERS_COUNT": 0,
            "DINE-IN": 0,
            "TAKE-AWAY": 0,
            "CAPPUCCINO_COUNT": 0,
            "ESPRESSO_COUNT": 0,
            "LATTE_COUNT": 0,
            "ICEDCOFFEE_COUNT": 0,
            "CUPS_COUNT": 0,
            "GST_TOTAL": 0,
            "DAILY_INCOME": 0
        }
        self.order_log = []

    def read_csv(self, file_name):
        """This function reads the CSV file and writes the rows to the order array"""

        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.order.append(row)

    def round(self, amount):
        """Rounds a float to 5 cents"""

        return self.big_manager.round_to(amount, 0.05)

    def writeCSV(self):
        """Writes the order information the the output CSV file"""

        with open(self.output_filename, mode='w') as output_file:
            order_output_str = "ORDER_ID,TYPE,ITEM_1,QTY_1,EXGST_1,ITEM_2,QTY_2,EXGST_2,ITEM_3,QTY_3,EXGST_3,ITEM_4,QTY_4,EXGST_4,CUPS,GST,TAX,ORDER_TOTAL,AMT_TENDERED,CHANGE"
            output_writer = csv.DictWriter(output_file, fieldnames=order_output_str.split(','))
            output_writer.writeheader()
            for row in self.order_log:
                output_writer.writerow(row)

            daily_total_str = "ORDERS_COUNT,DINE-IN,TAKE-AWAY,CAPPUCCINO_COUNT,ESPRESSO_COUNT,LATTE_COUNT,ICEDCOFFEE_COUNT,CUPS_COUNT,GST_TOTAL,DAILY_INCOME"
            output_writer = csv.DictWriter(output_file, fieldnames=daily_total_str.split(','))
            output_writer.writeheader()
            output_writer.writerow(self.log)

    def loop(self):
        """Loops through the orders and runs processes"""

        for order in self.order:
            self.log['ORDERS_COUNT'] += 1
            dine_in = True
            if order['TYPE'] == "Dine-In":
                self.log['DINE-IN'] += 1
            else:
                dine_in = False
                self.log['TAKE-AWAY'] += 1

            subtotal = 0
            cups = 0

            order_log_entry = {
                "ORDER_ID": order['ORDER_ID'],
                "TYPE": ("Dine-In" if dine_in else "Take-Away"),
            }

            for number in range(1, 5):
                name = order["ITEM_" + str(number)]

                if name != "":
                    amount = int(order["QTY_" + str(number)])

                    self.log[name.replace(" ", "").upper() + "_COUNT"] += amount
                    cups += amount

                    price = self.manager.manager.prices[name] * amount
                    subtotal += price

                    order_log_entry["ITEM_" + str(number)] = name
                    order_log_entry["QTY_" + str(number)] = amount
                    order_log_entry["EXGST_" + str(number)] = price

            gst = subtotal * .1
            surcharge = 0
            if not dine_in:
                surcharge = (subtotal + gst) * 0.05

            total = self.round(subtotal + gst + surcharge)

            self.log['GST_TOTAL'] += self.round(gst)
            self.log['DAILY_INCOME'] += total
            self.log['CUPS_COUNT'] += cups

            order_log_entry["CUPS"] = cups
            order_log_entry["GST"] = "{:.2f}".format(gst)
            order_log_entry["TAX"] = "{:.2f}".format(surcharge)
            order_log_entry["ORDER_TOTAL"] = "{:.2f}".format(self.round(total))
            order_log_entry["AMT_TENDERED"] = order["AMT_TENDERED"]
            order_log_entry["CHANGE"] = "{:.2f}".format(float(order["AMT_TENDERED"]) - total)

            self.order_log.append(order_log_entry)

        self.writeCSV()
