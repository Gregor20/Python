from product import Product

class Inventory:
    def __init__(self):
        self.product_collection:list[Product] = []

    def add_product(self, product: Product):
        for item in self.product_collection:
            if item.id == product.id:
                raise TypeError("The product is already in the Inventory")
        self.product_collection.append(product)

    def remove_product(self, id: int):
        for item in self.product_collection:
            if item.id == id:
                self.product_collection.remove(item)
                print(f"The product {item.name} has been removed")
        raise TypeError(f"The id: {id} does not match with any product")

    def get_product(self, id: int):
        for item in self.product_collection:
            if item.id == id:
                return item
        raise TypeError(f"The id: {id} does not match with any product")
            
    def list_products(self):
        return self.product_collection
    
    def __repr__(self):
        return(f"All the products in the inventory: {[p.name for p in self.product_collection]}")
