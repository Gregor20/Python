from dataclasses import dataclass, field
from random import randint

# Regla general (pista):
# Property → atributos que quieres exponer de manera controlada (price, weight, etc.)
# Función → operaciones que modifican el estado del objeto o representan una acción del negocio (add_stock, sell, restock).

@dataclass
class Product:
    _name: str
    _price: float 
    _weight: float
    _stock: int
    _id: int = field(default_factory=lambda:randint(0, 1000))           # Al usar dataclases, los campos sin valores por defecto tienen que ir los primeros
                                                                        # Sino, no deja instanciar correctamente
    
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
        if new_stock <= 0:
            raise ValueError("No debe haber stock negativo")
        self._stock = new_stock

    @stock.deleter
    def stock(self):
        self._stock = None

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
        print(f"{quantity} products has been sold")
        


   

    

producto = Product("Gorra", 12, 0.2, 24)
print(producto)