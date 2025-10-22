from product import *
from inventory import Inventory
from store import Store
from fabrica import CleaningProductFactory, ClothingProductFactory

clothing_products = ClothingProductFactory()
cleaning_products = CleaningProductFactory()

Hats = clothing_products.create_product("Gorro", 10, 0.3, 25)
print(Hats)
Hats.add_stock(20)
print(Hats)
Hats.sell(12)
print(Hats)
Hats.sell(34)
print(Hats)



# hats = ClothingProduct("Hat", 12, 0.2, 24)
# socks = ClothingProduct("Socks", 10, 0.4, 12)
# trousers = ClothingProduct("Trousers", 10, 0.4, 12)

# my_store = Store()

# my_store.inventory.add_product(hats)

# my_store.restock_product(hats.id, 20)
# my_store.show_inventory()

# my_store.sell_product(12, 46)
# my_store.show_inventory()
