# pcost.py
#
# Exercise 1.27

cost = 0

with open("Data/portfolio.csv", "rt") as f:
    headers = next(f)
    print(headers)
    for line in f:
        row = line.split(',')
        num_shares = int(row[1])
        share_price = float(row[2])
        tot_price = num_shares*share_price
        cost += tot_price

print(f'Total price: ${cost}')