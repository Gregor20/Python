from store import Store
from inventory import Inventory
from factories import CleaningProductFactory, ClothingProductFactory

clothing_products = ClothingProductFactory()
cleaning_products = CleaningProductFactory()

hats_xl = clothing_products.create_product("Gorro Supreme", 10, 0.3, 25, "xl      ")

vacuum_cleaner = cleaning_products.create_product("Bosch Flexxo Serie 4", 120, 15, 100)

inventory = Inventory()
my_store = Store(inventory)
my_store.inventory.add_product(vacuum_cleaner)
my_store.inventory.add_product(hats_xl)
print(my_store.inventory)







# hats = ClothingProduct("Hat", 12, 0.2, 24)
# socks = ClothingProduct("Socks", 10, 0.4, 12)
# trousers = ClothingProduct("Trousers", 10, 0.4, 12)

# my_store = Store()

# my_store.inventory.add_product(hats)

# my_store.restock_product(hats.id, 20)
# my_store.show_inventory()

# my_store.sell_product(12, 46)
# my_store.show_inventory()
