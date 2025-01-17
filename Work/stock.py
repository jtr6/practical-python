# File to create class "Stock"

class Stock:
     
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, sales):
        self.shares -= sales

    def __repr__(self):
        return str(f'Stock{self.name, self.shares, self.price}')

class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)


