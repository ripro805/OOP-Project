from user import Customer
from seller import Seller

class Marketplace:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []

    def register_customer(self, email, password):
        customer = Customer(email, password)
        self.customers.append(customer)
        print(f" Customer registered: {email}")
        return customer

    def register_seller(self, email, password):
        seller = Seller(email, password)
        self.sellers.append(seller)
        print(f" Seller registered: {email}")
        return seller

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, product_id):
        for product in self.products:
            if product.id == product_id and product.stock > 0:
                return product
        return None
