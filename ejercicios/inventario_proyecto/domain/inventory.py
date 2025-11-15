from products import Product
from exceptions import ProductAlreadyExists, IdNotFoundError

class Inventory:
    def __init__(self):
        self.product_collection:dict[int, Product] = {}

    def add_product(self, product: Product):
        product_id = product.id
        if product_id in self.product_collection:
            raise ProductAlreadyExists("The product is already in the Inventory")
        self.product_collection[product_id] = product
        print(f"Producto '{product.name}' (ID: {product.id} añadido al inventario)")

    def remove_product(self, id: int):
        for item in self.product_collection:
            if item.id == id:
                self.product_collection.remove(item)
                print(f"The product {item.name} has been removed")
        raise IdNotFoundError(f"The id: {id} does not match with any product")

    def get_product(self, id: int):
        for item in self.product_collection:
            if item.id == id:
                return item
        raise IdNotFoundError(f"The id: {id} does not match with any product")
            
    def list_products(self):
        return self.product_collection
    
    def __repr__(self):
        lista_de_productos = [str(v) for v in self.product_collection.values()]
        productos_unidos = "\n".join(lista_de_productos)

        return f"All the products in the inventory:\n{productos_unidos}"
