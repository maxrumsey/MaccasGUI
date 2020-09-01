import tkinter as tk
import csv
from app import main

window = tk.Tk()

prices = {}

with open('config.csv') as configCSV:
    csv_reader = csv.reader(configCSV, delimiter = ',')
    linecount = 0
    for row in csv_reader:
        linecount += 1
        if (linecount == 1):
            continue
        prices[row[0]] = (float(row[1]))


main = main.Main(window, prices)
main.start()



