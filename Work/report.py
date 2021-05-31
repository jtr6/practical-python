# report.py
#
# Exercise 2.4

import csv
import numpy as np


def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict({"name": row[0], "shares": int(row[1]), "price": float(row[2])})
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    prices = dict({})
    with open(filename, "r") as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) > 0:
                prices[f"{row[0]}"] = float(row[1])
        return prices

portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

total_in_shares = 0

for company in portfolio:
    value = company["shares"] * company["price"]
    total_in_shares += value

updated_total = 0
for company, new in zip(portfolio, prices):
    name = company["name"]
    value = company["shares"] * prices[name]
    updated_total += value

change = round(updated_total - total_in_shares, 2)

print("Total cost: \t $", round(total_in_shares,2))
print("Current value: \t $", round(updated_total,2))


if change > 0:
    print(f"Congratulations, you have made ${change}")

if change < 0:
    print(f"Unfortunately you have lost ${np.abs(change)}")

else:
    print("Your stock has neither gained nor lost value")
