
def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print("\nTotal number of items: " + str(item_total))

def add_to_inventory(inventory, added_itmes):
    for item in added_itmes:
        if item not in inventory:
            inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory




inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'gemstone', 'diamond', 'ruby', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)


