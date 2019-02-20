
from products import Product

class ShoppingCart:

    def __init__(self):
        self.products = []

    def add_item (self, products):
        self.products.append(products)

    def remove_item(self, products):
        self.products.remove(products)

    def before_tax_total(self):
        result = 0
        for product in self.products:
            result += products.base_price
        return result

    def after_tax_total(self):
        result = 0
        for product in self.products:
            result += products.base_price + products.base_price * products.tax_rate
        return result


# bananas = Product('bananas', 0.25)
# hot_sauce = Product('Franks', 4.99, 0.13)
# whiskey = Product('crown-royal', 25.00)
shopping_cart = ShoppingCart()
shopping_cart.add_item(Product('bananas', 0.25))
shopping_cart.add_item(Product('Franks', 4.99, 0.13))
shopping_cart.add_item(Product('crown-royal', 25.00, 0.25))
