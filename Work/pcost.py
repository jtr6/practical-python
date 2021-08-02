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
    cost = sum([s.cost() for s in portfolio])
    return(cost)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)
