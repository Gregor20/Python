from abc import ABC, abstractmethod
from product import ClothingProduct, CleaningProduct

class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass

class ClothingProductFactory(Factory):
    def create_product(self):
        return ClothingProduct("New Clothing Product", 0, 0, 0)
    
class CleaningProductFactory(Factory):
    def create_product(self):
        return CleaningProduct("New Cleaning Product", 0, 0, 0)