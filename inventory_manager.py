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

def update_quantity(inventory):
    view_inventory(inventory)
    
    item_num = int(input("Enter the item number to update: "))
    if item_num > len(inventory) or item_num < 1:
        print("Invalid item number.")
        return
    
    item_amount = input("Enter the new quantity: ")
    try:
        item_amount = int(item_amount)
        if item_amount < 0:
            print("Quantity must be a nonnegative whole number.")
            return
    except ValueError:
        print("Quantity must be a nonnegative whole number.")
        return

    inventory[item_num-1]['Quantity'] = item_amount
    print("Item quantity updated successfully.")


def remove_item(inventory):
    view_inventory(inventory)
    
    item_num = int(input("Enter the item number to remove: "))
    if item_num > len(inventory) or item_num < 1:
        print("Invalid item number.")
        return
    
    
    print(f"Item removed: {inventory.pop(item_num-1)['Name']}")

def search_inventory(inventory):
    search_term = input("Enter the item name to search for: ")
    
    if search_term == "":
        print("Search term cannot be empty.")
        return
    
    found_items = []
    
    # already made the function wihtout seperate branch on accident
    for item in inventory:
        split_name = item['Name'].split()
        for word in split_name:
            if search_term.lower() == word.lower():
                found_items.append(item)
                break
    
    if len(found_items) == 0:
        print("No inventory items matched your search.")
        return
    elif len(found_items) > 1:
        print("Multiple items matched your search:")

        for item in found_items:
            print(f"{item['Name']} | {item['Category']} | {item['Quantity']}")


def display_summary(inventory):
    unique_items = len(inventory)
    total_quantity = sum(item['Quantity'] for item in inventory)
    low_stock_items = 0
    
    for item in inventory:
        if item['Quantity'] < 5:
            low_stock_items += 1
    
    print(f"Inventory Summary")
    print(f"Unique Items: {unique_items}")
    print(f"Total Quantity: {total_quantity}")
    print(f"Low-stock Items: {low_stock_items}")
    
    print("\nItems by category:")
    category_dict = {}
    for item in inventory:
        if item['Category'].lower() in category_dict:
            category_dict[item['Category'].lower()] += 1
        else:
            category_dict[item['Category'].lower()] = 1
            
    for category, count in category_dict.items():
        print(f"{category}: {count}")



def main():
    inventory = load_inventory(INVENTORY_FILE)



if __name__ == "__main__":
    main()