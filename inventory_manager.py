# Greyson Denison-Fischer
#
# HW01 Inventory Manager

INVENTORY_FILE = "inventory.txt"


def display_menu():
    """Display the inventory manager menu options."""
    print("Inventory Manager\n\n1. View inventory\n2. Add an item\n3. Update an item quantity\n4. Remove an item\n5. Search inventory\n6. View inventory summary\n7. Exit")

def load_inventory(filename):
    """Load inventory items from a pipe-delimited file.

    Args:
        filename (str): Path to the inventory file.

    Returns:
        list[dict] or None: Inventory items containing Name, Category, and
            Quantity, or None if an error occurs.
    """
    inventory = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                
                item = line.split('|')
                inventory.append(dict(Name=item[0], Category=item[1], Quantity=int(item[2])))
            
    except FileNotFoundError:
        return []
    
    return inventory


def save_inventory(inventory, filename):
    """Save inventory items to a pipe-delimited file, overwriting its contents.

    Args:
        inventory (list[dict]): Inventory items to save.
        filename (str): Path to the destination file.
    """
    with open(filename, 'w') as file: 
        for item in inventory:
            file.write(f"{item['Name']}|{item['Category']}|{item['Quantity']}\n")
        file.close()
    
    
def view_inventory(inventory):
    """Display a numbered list of inventory items or a message if empty.

    Args:
        inventory (list[dict]): Inventory items to display.
    """
    if len(inventory) == 0:
        print("No inventory items found.")
        return
    
    count = 1
    for item in inventory:
        print(f"{count}. {item['Name']} | {item['Category']} | {item['Quantity']}")
        count += 1
    


def validate_new_item(inventory, name, category, quantity):
    """Return an error message, or None when the item is valid."""
    try:
        quantity = int(quantity)
    except ValueError:
        return "Quantity must be a nonnegative whole number."

    if name.strip() == "":
        return "Item name cannot be empty."
    elif category.strip() == "":
        return "Category cannot be empty."
    elif "|" in name:
        return "Item name cannot contain |."
    elif "|" in category:
        return "Category cannot contain |."
    elif quantity < 0:
        return "Quantity must be a nonnegative whole number."

    for item in inventory:
        if item["Name"].lower() == name.lower():
            return "Item already exists."

    return None

def add_item(inventory):
    """Prompt for and add an inventory item after validating the input.

    Reject empty names or categories, invalid or negative quantities, and
    duplicate item names using a case-insensitive comparison.

    Args:
        inventory (list[dict]): Inventory list to modify.
    """
    name = input("Enter the item name: ")
    category = input("Enter the category: ")
    try:
        quantity = int(input("Enter the quantity: "))
    except ValueError:
        print("Quantity must be a nonnegative whole number.")
        return
    
    result = validate_new_item(inventory, name, category, quantity)

    if result is not None:
        print(result)
        return

    inventory.append(dict(Name=name, Category=category, Quantity=quantity))
    print("Item added successfully.")

def update_item_quantity(inventory, item_number, new_quantity):
    if item_number < 1 or item_number > len(inventory):
        return "Invalid item number."

    if new_quantity < 0:
        return "Quantity must be a nonnegative whole number."

    inventory[item_number - 1]["Quantity"] = new_quantity
    return None

def update_quantity(inventory):
    """Prompt for an item number and update its quantity.

    Reject invalid item numbers and quantities that are not nonnegative
    whole numbers.

    Args:
        inventory (list[dict]): Inventory list to modify.
    """
    view_inventory(inventory)
    try:
        item_num = int(input("Enter the item number to update: "))
    except ValueError:
        print("Invalid Number")
        return
    
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

    
    result = update_item_quantity(inventory, item_num, item_amount)

    if result is None:
        print("Item quantity updated successfully.")
    else:
        print(result)

#AI GENERATED FUNCTION TESTED AND VERIFIED
def remove_item_by_number(inventory, item_number):
    """Remove an item by its displayed number."""
    if item_number < 1 or item_number > len(inventory):
        return None

    return inventory.pop(item_number - 1)

def remove_item(inventory):
    """Prompt for an item number and remove the corresponding item.

    Display an error message if the item number is invalid.

    Args:
        inventory (list[dict]): Inventory list to modify.
    """
    view_inventory(inventory)
    
    try:
        item_num = int(input("Enter the item number to remove: "))
    except ValueError:
        print("Invalid item number.")
        return
    
    removed_item = remove_item_by_number(inventory, item_num)

    if removed_item is None:
        print("Invalid item number.")
    else:
        print(f"Item removed: {removed_item['Name']}")


#added a helper function to make testing specific functionality easier
def find_matching_items(inventory, search_term):
    """Return partial name matches, ignoring capitalization."""
    search_term = search_term.strip()

    if search_term == "":
        return "Search term cannot be empty."

    found_items = []

    for item in inventory:
        if search_term.lower() in item["Name"].lower():
            found_items.append(item)

    return found_items

def search_inventory(inventory):
    """Search item names for a case-insensitive whole-word match.

    Prompt for a search term and reject an empty entry. Display matching
    items when multiple items match, or a message when none match.
    A single matching item is not displayed.

    Args:
        inventory (list[dict]): Inventory items to search.
    """
    search_term = input("Enter the item name to search for: ").strip()
    
    try:
        found_items = find_matching_items(inventory, search_term)
    except ValueError as error:
        print(error)
        return
    
    found_items = []
    
    # already made the function wihtout seperate branch on accident
    for item in inventory:
        if search_term.lower() in item['Name'].lower():
            found_items.append(item)
            break
    
    if len(found_items) == 0:
        print("No inventory items matched your search.")
        return
    elif len(found_items) > 1:
        print("Multiple items matched your search:")

        for item in found_items:
            print(f"{item['Name']} | {item['Category']} | {item['Quantity']}")
    else:
        item = found_items[0]
        print(f"{item['Name']} | {item['Category']} | {item['Quantity']}")
        


def display_summary(inventory):
    """Display item counts, total quantity, low stock, and category counts.

    Count items with quantities below five as low stock and group category
    names case-insensitively.

    Args:
        inventory (list[dict]): Inventory items to summarize.
    """
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
    """Load inventory and run the interactive inventory manager.

    Process menu options and save inventory after each option from 1 to 6.
    Exit if loading fails or the user enters any other option.
    """
    inventory = load_inventory(INVENTORY_FILE)
    
    start = True
    if inventory == None:
        start = False

    while start:
        display_menu()
        
        user_input = input("Select an option: ")
        
        print("\n")
        
        if user_input == "1":
            view_inventory(inventory)
        elif user_input == "2":
            add_item(inventory)
        elif user_input == "3":
            update_quantity(inventory)
        elif user_input == "4":
            remove_item(inventory)
        elif user_input == "5":
            search_inventory(inventory)
        elif user_input == "6":
            display_summary(inventory)
        elif user_input == "7":
            print("Goodbye! Program saving and closing. ")
            return
        else:
            print("Invalid menu choice. Please enter a number from 1 to 7.")
            continue
            
        save_inventory(inventory, INVENTORY_FILE)
        print("Inventory saved successfully.")
     

if __name__ == "__main__":
    main()