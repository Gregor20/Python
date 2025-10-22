from product import *
from inventory import Inventory
from store import Store
from fabrica import *

clothing_product_factory = ClothingProductFactory()
cleaning_product_factory = CleaningProductFactory()

producto1 = cleaning_product_factory.create_product()
print(producto1)





# hats = ClothingProduct("Hat", 12, 0.2, 24)
# socks = ClothingProduct("Socks", 10, 0.4, 12)
# trousers = ClothingProduct("Trousers", 10, 0.4, 12)

# my_store = Store()

# my_store.inventory.add_product(hats)

# my_store.restock_product(hats.id, 20)
# my_store.show_inventory()

# my_store.sell_product(12, 46)
# my_store.show_inventory()
