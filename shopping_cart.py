
from products import Products

class ShoppingCart:

    def __init__(self, products):
        self.products = products

    def add (self, product):
        self.products.append(products)

    def remove(self, product):
        self.products.remove(products)

    def before_tax_total(self):
        before_tax = 0
        for product in self.products:
            before_tax += products.base_price
        return before_tax

    def after_tax_total(self):
        after_tax = 0
        for product in self.prodcuts:
            after_tax += products.price()
        return after_tax
