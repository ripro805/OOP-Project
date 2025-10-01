from abc import ABC

class User(ABC):
    def __init__(self, email, password):
        self.email = email
        self.password = password

class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.cart = {}  # product -> quantity

    def view_products(self, marketplace):
        print("\n===== Available Products =====")
        available = False
        for product in marketplace.products:
            if product.stock > 0:
                print(f"ID: {product.id} | {product.name} | Price: {product.price} | Stock: {product.stock}")
                available = True
        if not available:
            print("No products available right now.")

    def add_to_cart(self, marketplace, product_id, quantity):
        product = marketplace.find_product(product_id)
        if product:
            if product.stock >= quantity:
                # Reduce stock temporarily in marketplace to avoid over-ordering
                product.stock -= quantity
                if product in self.cart:
                    self.cart[product] += quantity
                else:
                    self.cart[product] = quantity
                print(f"Added {quantity} x {product.name} to cart")
            else:
                print(f"Only {product.stock} of {product.name} left in stock!")
        else:
            print("Product not found!")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("\n===== Your Cart =====")
        total = 0
        for product, qty in self.cart.items():
            price = product.price * qty
            total += price
            print(f"{product.name} | Price: {product.price} | Qty: {qty} | Total: {price}")
        print(f"🛒 Total Price: {total}")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Add products before checkout.")
            return
        total = sum(product.price * qty for product, qty in self.cart.items())
        print(f"\nCheckout successful! Total amount paid: {total}")
        self.cart.clear()  # empty the cart after checkout
