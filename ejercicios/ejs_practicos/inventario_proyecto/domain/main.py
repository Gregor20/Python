from product import *
from inventory import Inventory
from store import Store
from fabrica import CleaningProductFactory, ClothingProductFactory

clothing_products = ClothingProductFactory()
cleaning_products = CleaningProductFactory()

Hat = clothing_products.create_product()
print(Hat.get_category())
print(Hat)
Hat.name = "Gorro"
Hat.price = 10
Hat.weight = 0.3
Hat.add_stock(25)
print(Hat)





# hats = ClothingProduct("Hat", 12, 0.2, 24)
# socks = ClothingProduct("Socks", 10, 0.4, 12)
# trousers = ClothingProduct("Trousers", 10, 0.4, 12)

# my_store = Store()

# my_store.inventory.add_product(hats)

# my_store.restock_product(hats.id, 20)
# my_store.show_inventory()

# my_store.sell_product(12, 46)
# my_store.show_inventory()
