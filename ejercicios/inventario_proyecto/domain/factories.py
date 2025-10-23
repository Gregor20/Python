from abc import ABC, abstractmethod
from products import ClothingProduct, CleaningProduct

class Factory(ABC):
    @abstractmethod
    def create_product(self, name: str, price: float, weight: float, stock: int):
        pass

class CleaningProductFactory(Factory):
    def create_product(self, name, price, weight, stock):
        return CleaningProduct(name, price, weight, stock)
    
class ClothingProductFactory(Factory):
    def create_product(self, name, price, weight, stock, size):
        return ClothingProduct(name, price, weight, stock, size)