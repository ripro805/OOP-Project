class Product:
    _id_counter = 1

    def __init__(self, name, price, stock, seller):
        self.id = Product._id_counter
        Product._id_counter += 1
        self.name = name
        self.price = price
        self.stock = stock
        self.seller = seller
