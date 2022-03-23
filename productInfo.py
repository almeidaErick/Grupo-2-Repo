class Product:

    def __init__(self, product, price, description,currency):
        self.product = product
        self.price = price
        self.description = description
        self.currency = currency

    def __str__(self):
        # STEVEN
        return f"producto:{self.product}, precio:{self.price}, descripcion:{self.description}, currency:{self.currency}"

    def to_dict(self):
        # complete this
        # JORGE
        return {"product":self.product,"price":self.price,"description":self.description,"currency":self.currency}
