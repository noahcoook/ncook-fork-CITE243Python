
def display_inventory(inventory):
    print("Inventory:")
    item_total = 0 #initializes item total
    for k, v in inventory.items(): #loops through inv, prints value, followed by key pair
        print(f'{v} {k}')
        item_total += v #each time item is counted, the total goes up
    print("\nTotal number of items: " + str(item_total))

def add_to_inventory(inventory, added_itmes):
    for item in added_itmes:
        if item not in inventory:
            inventory.setdefault(item, 0) #if theres a new item, it sets it as a dictionary entry with a value of 0
        inventory[item] += 1 #either ups value from 0 to 1, or just adds one to total in inv
    return inventory 




inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'gemstone', 'diamond', 'ruby', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)


