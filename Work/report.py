# report.py
#
# Exercise 2.4

import csv
import numpy as np
import fileparse

def read_portfolio(portfolio_file):
    '''
    Read in a csv to a portfolio dict
    '''
    with open(portfolio_file) as file:
        portfolio = fileparse.parse_csv(file, select=["name", "shares", "price"], types=[str,int,float])
    return portfolio

def read_prices(prices_file):
    '''
    Read in a price list and return a price dict
    '''
    with open(prices_file) as file:
        price_list = fileparse.parse_csv(file, types=[str,float], has_headers=False)
        prices = dict(price_list)
    return prices

def make_report(stocks, prices): # takes a list of stocks and a dict of prices and outputs a formatted report
    '''
    Write a report table of shares, prices and change in price
    '''
    report = []
    for row in stocks:
        name = row["name"]
        shares = row["shares"]
        price = prices[name]
        change = price - row["price"]
        report.append((name, shares, price, change))
    return report

def portfolio_report(portfolio_file, prices_file):
    '''
    Print out full report with table of shares, price and change, and the current total value and change
    '''
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    total_in_shares = 0 
    for company in portfolio:
        value = company["shares"] * company["price"]
        total_in_shares += value
    updated_total = 0
    for company in portfolio:
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

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        portfolio_report(sys.argv[1], sys.argv[2])
    else:
        portfolio_report("Data/portfolio.csv", "Data/prices.csv")