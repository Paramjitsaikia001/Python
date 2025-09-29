# Create a class called order that stores items and prices . Use dunder function __gt__() to convey that order1>order2 if the price of order1 is greater than order 2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def showdetails(self):
        print("Product name:",self.item)
        print("USP:",self.price)

    def __gt__(self,odr):
        return self.price > odr.price
    
odr1=Order("Lays-Onion flavour",20)
odr1.showdetails()

odr2=Order("Cheese Cream Biscuit",35)
odr2.showdetails()

print(odr2>odr1)