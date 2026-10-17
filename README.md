# Inventory Manager

## Project Description

A python program that manages inventory items and saves them in a text file.

## Current Features

- View, add, update, and remove items.
- Search item names by a whole word, ignoring capitalization.
- Reject duplicate names when adding items, ignoring capitalization.
- Check for empty names and categories and invalid or negative quantities when adding items.
- Show item count, total quantity, low-stock count, and item counts by category.
- Save inventory after menu options 1 through 6.

## Requirements

- Python 3.
- A terminal
- An `inventory.txt` file in the folder where you run the program.
- Permission to read and write that file.

No extra Python packages are needed.

## Project Files

| File                   | Description                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| `inventory_manager.py` | Contains the menu, inventory functions, and main program.                                           |
| `inventory.txt`        | Stores inventory data. Create this file before running; it was not included with the supplied code. |
| `README.md`            | Explains the project and how to use it.                                                             |

## Inventory Data Format

Each line in `inventory.txt` uses this format, with no header:

```text
Name|Category|Quantity
```

Example data:

```text
Pencil|School Supplies|10
Notebook|School Supplies|3
```

Use a nonnegative whole number for quantity. Do not use `|` inside names or categories or add blank lines. An empty file can be used to start with no items.

## Running the Program

1. Install Python 3.
2. Put `inventory_manager.py` in a project folder.
3. Create `inventory.txt` in that folder. Leave it empty or add data in the format above.
4. Open a terminal in that folder.
5. Run:

```bash
python inventory_manager.py
```

If your system uses `python3`, run:

```bash
python3 inventory_manager.py
```

6. Enter a menu number and follow the prompts.

## Menu Options

| Option | Action                                                             |
| ------ | ------------------------------------------------------------------ |
| 1      | View all inventory items.                                          |
| 2      | Add an item with a name, category, and quantity.                   |
| 3      | Select an item number and replace its quantity.                    |
| 4      | Select an item number to remove.                                   |
| 5      | Search for a whole word in item names.                             |
| 6      | View the inventory summary. Quantities below 5 count as low stock. |
| 7      | Exit the program.                                                  |

Category counts in the summary ignore capitalization and count item entries, not total units. Any menu input other than 1 through 6 exits the program.

## Sample Interaction

Starting with an empty `inventory.txt`:

```text
Inventory Manager

1. View inventory
2. Add an item
3. Update an item quantity
4. Remove an item
5. Search inventory
6. View inventory summary
7. Exit
Select an option: 2


Enter the item name: Pencil
Enter the category: School Supplies
Enter the quantity: 10
Item added successfully.
Inventory saved successfully.
```

The menu appears again. Choose option 1 to see:

```text
1. Pencil | School Supplies | 10
Inventory saved successfully.
```

## Testing Summary

Testing summary is listed within Testing.MD

## Known Limitations

- Saving overwrites the data file, and save errors are not handled.
- There is no undo or confirmation before removing an item.

## Possible Future Improvements

- Add automated tests.
