# Greyson Denison-Fischer
#
# HW01 Inventory Manager

INVENTORY_FILE = "inventory.txt"


def display_menu():
    print("Inventory Manager\n\n1. View inventory\n2. Add an item\n3. Update an item quantity\n4. Remove an item\n5. Search inventory\n6. View inventory summary\n7. Exit")

def load_inventory(filename):
    inventory = []
    
    file = open(filename, 'r')
    
    for line in file:
        item = line.split('|')
        inventory.append(dict(Name=item[0], Category=item[1], Quantity=int(item[2])))
        
    file.close()
    
    return inventory

def save_inventory(inventory, filename):
    file = open(filename, 'w')
    
    for item in inventory:
        file.write(f"{item['Name']}|{item['Category']}|{item['Quantity']}\n")
    
    file.close()
    
    


def main():
    inventory = load_inventory(INVENTORY_FILE)



if __name__ == "__main__":
    main()