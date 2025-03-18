# pcost.py
#
# Exercise 1.27

# import csv 
    # file = open('Data/portfolio.csv')
    # rows = csv.reader(file)
import sys

def portfolio_cost(filename):
    cost = 0
    with open(filename,'rt') as file:
        data=file.read()
        headers = next(file)
        for line in file:
            print(line)
    
        cost = cost + (int(line[1]) * float(line[2]))

    # file.close()

# REDO THE FUNCTION

    


