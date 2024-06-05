
def create_inventory(items):
    my_map=dict()
    for i in items:
        if i not in my_map:
            my_map[i]=1
        else:
            my_map[i]+=1
    return my_map

def add_items(inventory, items):
    for i in items:
        if i not in inventory:
            inventory[i]=1
        else:
            inventory[i]+=1
    return inventory

def decrement_items(inventory, items):
    for i in items:
        if i not in inventory:
            inventory[i]=1
        else:
            inventory[i]-=1
        if inventory[i]<=0:
            inventory[i]=0
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    list=[]
    for articulo, cantidad in inventory.items():
        if cantidad >0:
            list.append((articulo,cantidad))
    return list
