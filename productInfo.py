class Product:

    def __init__(self, product, price):
        self.product = product
        self.price = price

    def __str__(self):
        # STEVEN
        return f"producto:{self.product}, precio:{self.price}"

    def to_dict(self):
        # complete this
        # JORGE
        return