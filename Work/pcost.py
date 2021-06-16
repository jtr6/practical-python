# pcost.py
#
# Exercise 1.27

import report

def portfolio_cost(filename):
    '''
    Return total cost of the portfolio
    '''
    cost = 0
    portfolio = report.read_portfolio(filename)
    for company in portfolio:
        num_shares = company["shares"]
        share_price = company["price"]
        tot_price = num_shares*share_price
        cost += tot_price
    return(cost)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)
