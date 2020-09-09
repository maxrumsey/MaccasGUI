"""

Starts the program"""

import tkinter as tk
import csv
from app import main

window = tk.Tk()

prices = {}

with open('config.csv') as configCSV:
    csv_reader = csv.reader(configCSV, delimiter=',')
    LINE_COUNT = 0
    for row in csv_reader:
        LINE_COUNT += 1
        if LINE_COUNT != 1:
            prices[row[0]] = (float(row[1]))


main = main.Main(window, prices)
main.start()
