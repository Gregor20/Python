from product import Product
from inventory import Inventory
from store import Store

hats = Product("Hat", 12, 0.2, 24)
socks = Product("Socks", 10, 0.4, 12)
trousers = Product("Trousers", 10, 0.4, 12)

my_store = Store()

my_store.inventory.add_product(hats)

my_store.restock_product(hats.id, 20)
my_store.show_inventory()

my_store.sell_product(12, 46)
my_store.show_inventory()
