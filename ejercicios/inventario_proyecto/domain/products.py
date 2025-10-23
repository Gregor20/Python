from dataclasses import dataclass, field
from random import randint
from abc import ABC, abstractmethod

# Regla general (pista):
# Property → atributos que quieres exponer de manera controlada (price, weight, etc.)
# Función → operaciones que modifican el estado del objeto o representan una acción del negocio (add_stock, sell, restock).

@dataclass
class Product(ABC):
    _name: str
    _price: float 
    _weight: float
    _stock: int
    _id: int = field(default_factory = lambda:randint(0, 500), init=False)

    # Al usar dataclases, los campos sin valores por defecto tienen que ir los primeros. Sino no deja instanciar correctamente
                                                                        
    
    @property
    def name(self):                     # NOMBRE
        return self._name
    
    @name.setter
    def name(self, new_name:str):
        self._name = new_name

    @name.deleter
    def name(self):
        self._name = None

    @property
    def price(self):                    # PRECIO
        return self._price
    
    @price.setter
    def price(self, new_price:float):
        if new_price <= 0:
            raise ValueError("El valor debe ser mayor a 0")
        self._price = new_price

    @price.deleter
    def price(self):
        self._price = None

    @property
    def weight(self):                   # PESO
        return self._weight
    
    @weight.setter
    def weight(self, new_weight:float):
        if new_weight < 0:
            raise ValueError("No puede pesar 0 o menos")
        self._weight = new_weight

    @weight.deleter
    def weight(self):
        self._weight = None

    @property
    def stock(self):                    # STOCK
        return self._stock
    
    @stock.setter
    def stock(self, new_stock:int):
        if new_stock < 0:
            raise ValueError("No debe haber stock negativo")
        self._stock = new_stock

    @stock.deleter
    def stock(self):
        self._stock = None

    @property                           # ID
    def id(self):
        return self._id

    def add_stock(self, amount:int):
        if amount <= 0:
            raise ValueError("The amount must be at least 1")
        self._stock += amount

    def remove_stock(self, amount:int):
        if amount <= 0:
            raise ValueError("The stock has to be positive")
        if amount > self._stock:
            raise ValueError("There is no stock avaible")
        self._stock -= amount

    def sell(self, quantity:int):
        if quantity <= 0:
            raise ValueError("You can not sell 0 products")
        if quantity > self._stock:
            raise ValueError("There is no stock avaible")
        self._stock -= quantity

        verb = "has" if quantity == 1 else "have"
        print(f"{quantity} pcs of {self.name} {verb} been sold")

    def __repr__(self):
        return (f"Product ID: {self._id}, Name: {self._name}, Price: {self._price}, Stock: {self._stock}")
        
    @abstractmethod
    def get_category(self):
        pass

class CleaningProduct(Product):
    def get_category(self):
        return "Cleaning"

@dataclass  
class ClothingProduct(Product):
    _size: str
    _avaible_sizes: list = field(default_factory=lambda: ["XS", "S", "M", "L", "XL", "XXL"], init=False)

    # field() se usa en dataclasses para configurar atributos especiales.
    # - default_factory: permite usar valores mutables (listas, diccionarios, etc.) sin compartirlos entre instancias.
    # - init=False: excluye el atributo del constructor (__init__).
    # - repr, compare, metadata, etc. permiten controlar cómo el atributo se muestra o compara.

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size:str):
        good_new_size = new_size.upper().strip()            # strip() elimina espacios en blanco (u otros caracteres) al inicio y al final de la cadena.
        if good_new_size not in self._avaible_sizes:        
            raise ValueError("This size does not exist")
        else:
            self._size = good_new_size


    def __repr__(self):
        return super().__repr__() + f", Size: {self.size}"
    
    def __post_init__(self):
        self.size = self._size      # llama al setter para validar

    # __post_init__ es el lugar para “arreglar” o validar atributos que necesitan lógica extra.
    # Solo incluyes en él los atributos que lo requieren; no hay obligación de procesar todo.

    def get_category(self):
        return "Clothing"