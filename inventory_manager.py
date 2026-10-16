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
    
    
def view_inventory(inventory):
    if len(inventory) == 0:
        print("No inventory items found.")
        return
    
    count = 1
    for item in inventory:
        print(f"{count}. {item['Name']} | {item['Category']} | {item['Quantity']}")
        count += 1
    

def add_item(inventory):
    name = input("Enter the item name: ")
    category = input("Enter the category: ")
    try:
        quantity = int(input("Enter the quantity: "))
    except ValueError:
        print("Quantity must be a nonnegative whole number.")
        return
    
    if(len(name) == 0):
        print("Item name cannot be empty.")
        return
    elif(len(category) == 0):
        print("Category cannot be empty.")
        return
    elif(quantity < 0):
        print("Quantity must be a nonnegative whole number.")
        return
    
    name = name.strip("|")
    category = category.strip("|")
    for item in inventory:
        if(item['Name'].lower() == name.lower()):
            print("Item already exists.")
            return
    inventory.append(dict(Name=name, Category=category, Quantity=quantity))
    print("Item added successfully.")



def main():
    inventory = load_inventory(INVENTORY_FILE)



if __name__ == "__main__":
    main()