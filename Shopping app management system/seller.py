from user import User
from product import Product

class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []

    def add_product(self, marketplace, name, price, stock):
        product = Product(name, price, stock, self)
        marketplace.add_product(product)
        self.products.append(product)
        print(f"✅ Product '{name}' added with stock {stock}")
