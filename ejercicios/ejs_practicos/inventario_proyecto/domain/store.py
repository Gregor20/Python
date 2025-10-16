from inventory import Inventory
from product import Product

class Store:
    def __init__(self):
        self.inventory = Inventory()
        self._sales_total = 0

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

        
    def show_inventory(self):
        print(self.inventory.list_products())