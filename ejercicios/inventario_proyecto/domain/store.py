from inventory import Inventory
from products import Product

class Store:
    def __init__(self):
        self.inventory = Inventory()
        self._sales_total = 0

    def add_product(self, new_product:Product):
        if new_product in self.inventory.product_collection:
            self.restock_product(new_product.id, new_product.stock)
        else:
            self.inventory.add_product(new_product)

    def restock_product(self, product_id, quantity):
        try:
            product = self.inventory.get_product(product_id)
            product.add_stock(quantity)
            print(f"Existing product, stock updated to {product._stock}")
        except TypeError:
            print(f"The ID: {product_id} does not match with any product")

    def sell_product(self, product_id, quantity):
        try:
            product = self.inventory.get_product(product_id)
            product.sell(quantity)
            self._sales_total += quantity
            print(f"Sold {quantity} units of {product.name}")
        except TypeError:                                                       # Id no existente
            print(f"Product with ID {product_id} does not exist")
        except ValueError as e:                                                 # stock insuficiente
            print(f"Cannot sell {quantity} units: {e}")

    def __repr__(self):
        return self.inventory