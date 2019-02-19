
from product import Products

class ShoppingCart:

    def __init__(self, product):
        self.products = products

    def add (self, product):
        self.products.append(product)

    def remove(self, product):
        self.products.remove(product)    
