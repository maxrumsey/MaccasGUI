import csv

class Tester:
    def __init__(self, manager, output):
        self.manager = manager
        self.bigManager = manager.manager
        self.order = []
        self.outputFileName = output
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
        self.orderLog = []

    def readCSV(self, fileName):
        with open(fileName, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.order.append(row)

    def round(self, input):
        return self.bigManager.round_to(input, 0.05)

    def writeCSV(self):
        with open(self.outputFileName, mode='w') as outputFile:
            outputWriter = csv.DictWriter(outputFile, fieldnames = "ORDER_ID,TYPE,ITEM_1,QTY_1,EXGST_1,ITEM_2,QTY_2,EXGST_2,ITEM_3,QTY_3,EXGST_3,ITEM_4,QTY_4,EXGST_4,CUPS,GST,TAX,ORDER_TOTAL,AMT_TENDERED,CHANGE".split(','))
            outputWriter.writeheader()
            for row in self.orderLog:
                outputWriter.writerow(row)
            outputWriter = csv.DictWriter(outputFile, fieldnames = "ORDERS_COUNT,DINE-IN,TAKE-AWAY,CAPPUCCINO_COUNT,ESPRESSO_COUNT,LATTE_COUNT,ICEDCOFFEE_COUNT,CUPS_COUNT,GST_TOTAL,DAILY_INCOME".split(','))
            outputWriter.writeheader()
            outputWriter.writerow(self.log)

    def loop(self):
        for order in self.order:
            self.log['ORDERS_COUNT'] += 1
            dinein = True
            if order['TYPE'] == "Dine-In":
                self.log['DINE-IN'] += 1
            else:
                dinein = False
                self.log['TAKE-AWAY'] += 1

            subtotal = 0
            cups = 0

            orderLogEntry = {
                "ORDER_ID": order['ORDER_ID'],
                "TYPE": ("Dine-In" if dinein == True else "Take-Away"),
                
            }

            for x in range(1, 5):
                name = order["ITEM_" + str(x)]

                if name == "":
                    continue

                amount = int(order["QTY_" + str(x)])

                self.log[name.replace(" ", "").upper() + "_COUNT"] += amount
                cups += amount
                

                price = self.manager.manager.prices[name] * amount
                subtotal += price

                orderLogEntry["ITEM_" + str(x)] = name
                orderLogEntry["QTY_" + str(x)] = amount
                orderLogEntry["EXGST_" + str(x)] = price


        
            GST = (subtotal) * .1
            surcharge = 0
            if (dinein == False):
                surcharge = (subtotal + GST) * 0.05

            total = self.round(subtotal + GST + surcharge)

            self.log['GST_TOTAL'] += self.round(GST)
            self.log['DAILY_INCOME'] += total
            self.log['CUPS_COUNT'] += cups

            orderLogEntry["CUPS"] = cups
            orderLogEntry["GST"] = "{:.2f}".format(GST)
            orderLogEntry["TAX"] = "{:.2f}".format(surcharge)
            orderLogEntry["ORDER_TOTAL"] = "{:.2f}".format(self.round(total))
            orderLogEntry["AMT_TENDERED"] = order["AMT_TENDERED"]
            orderLogEntry["CHANGE"] = "{:.2f}".format(float(order["AMT_TENDERED"]) - total)

            self.orderLog.append(orderLogEntry)
        self.writeCSV()
            



            

            
            

    
