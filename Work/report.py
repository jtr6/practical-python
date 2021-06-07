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


def make_report(stocks, prices): # takes a list of stocks and a dict of prices and outputs a formatted report
    report = []
    for row in stocks:
        name = row["name"]
        shares = row["shares"]
        price = prices[name]
        change = price - row["price"]
        report.append((name, shares, price, change))
    return report


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

report = make_report(portfolio, prices)

headers = ("Name", "Shares", "Price", "Change")
print("%10s %10s %10s %10s" % headers)
print(("-"*10 + " ") * len(headers))

for name, shares, price, change in report:
    price = f"${price:0.2f}" 
    print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")
