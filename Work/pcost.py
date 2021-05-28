# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(file):
    cost = 0

    with open(file, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                num_shares = int(row[1])
                share_price = float(row[2])
                tot_price = num_shares*share_price
            except ValueError:
                print("Some data missing, skipping row")
                tot_price = 0
            cost += tot_price
    return(cost)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
