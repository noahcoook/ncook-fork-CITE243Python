
def display_inventory(inventory):
    #displays the item in invertory list
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items(): #loops through the dictionary and prints the key and value (k and v)
        print(f'{v} {k}') #prints the value and key in the format "value key"
        item_total += v #adds the value to the item_total variable
    print("\nTotal number of items: " + str(item_total)) #prints the total number of items in the inventory

def add_to_inventory(inventory, added_itmes): #takes dict, and list as parameters
    for item in added_itmes:
        if item not in inventory:
            inventory.setdefault(item, 0) #if loot item isnt in inventory, add to and convert to dict type with a value of 0
        inventory[item] += 1 #adds 1 to the value of the item in the inventory
    return inventory #returns the updated inventory




inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'gemstone', 'diamond', 'ruby', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin', 'gold coin']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)


