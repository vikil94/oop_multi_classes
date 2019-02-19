class Products:

    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = base_price
        self.tax = tax_rate


    def __str__(self):
        return "This is your product: {}. The base price is: {}, the tax rate is: {:.2f}" .format(self.name, self.base_price, self.tax)

    def price(self, base_price, tax):
        price = base_price * tax
        total = price + base_price
        return total


product1 = Products("apple", 5, 0.25)
print(product1)
print("And the total price of this product is: {}".format(product1.price(50, 0.25)))
