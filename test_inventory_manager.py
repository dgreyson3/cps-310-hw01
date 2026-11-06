import pytest

from inventory_manager import load_inventory, save_inventory, find_matching_items, remove_item_by_number


@pytest.fixture
def sample_inventory():
    """Return fresh sample data for each test."""
    return [
        {"Name": "Notebook", "Category": "School", "Quantity": 10},
        {"Name": "Pencil", "Category": "school", "Quantity": 4},
        {"Name": "Water Bottle", "Category": "Kitchen", "Quantity": 5},
        {"Name": "Coffee Mug", "Category": "Kitchen", "Quantity": 0},
    ]

def test_load_inventory_reads_file(tmp_path, sample_inventory):
    # Arrange
    inventory_path = tmp_path / "inventory.txt"
    inventory_path.write_text("Notebook|School|10\nPencil|school|4\nWater Bottle|Kitchen|5\nCoffee Mug|Kitchen|0\n")
    
    #Act
    result = load_inventory(inventory_path)
    
    #Assert
    assert result == sample_inventory
    
def test_load_inventory_converts_int(tmp_path):
    # Arrange
    inventory_path = tmp_path / "inventory.txt"
    inventory_path.write_text("Notebook|School|10\nPencil|school|4\nWater Bottle|Kitchen|5\nCoffee Mug|Kitchen|0\n")
    
    #Act
    result = load_inventory(inventory_path)
    
    #Assert
    assert len(result) == 4
    assert result[0]["Quantity"] == 10
    assert result[1]["Quantity"] == 4
    assert result[2]["Quantity"] == 5
    assert result[3]["Quantity"] == 0

    for item in result:
        assert type(item["Quantity"]) is int
        

def test_load_inventory_ignores_blank(tmp_path, sample_inventory):
    #Arrange
    inventory_path = tmp_path / "inventory.txt"
    inventory_path.write_text("Notebook|School|10\nPencil|school|4\nWater Bottle|Kitchen|5\n\n\n\nCoffee Mug|Kitchen|0\n")
    
    #Act
    result = load_inventory(inventory_path)
    
    #Assert
    assert result == sample_inventory
    
def test_load_inventory_missing_files(tmp_path):
    #Arrange
    inventory_path = tmp_path / "missing.txt"
    
    #Act
    result = load_inventory(inventory_path)
    
    # Assert
    assert result == []
    
    
def test_save_inventory_format(tmp_path, sample_inventory):
    #Arrange
    inventory_path = tmp_path / "inventory.txt"
    text = "Notebook|School|10\nPencil|school|4\nWater Bottle|Kitchen|5\nCoffee Mug|Kitchen|0\n"

    
    #Act
    save_inventory(sample_inventory, inventory_path)
    
    assert inventory_path.read_text() == text
    

def test_save_empty_inventory(tmp_path):
    #Arrange
    inventory_path = tmp_path / "inventory.txt"
    inventory_path.write_text("Notebook|School|10\nPencil|school|4\nWater Bottle|Kitchen|5\n\n\n\nCoffee Mug|Kitchen|0\n")

    #Act
    save_inventory([], inventory_path)
    
    #Assert
    assert inventory_path.read_text() == ""
    
def test_save_and_load_round_trip(tmp_path, sample_inventory):
    #Arrange
    inventory_path = tmp_path / "inventory.txt"

    #Act
    save_inventory(sample_inventory, inventory_path)
    result = load_inventory(inventory_path)

    #Assert
    assert result == sample_inventory
    
    
@pytest.mark.parametrize(
    "search_term, expected_names",
    [
        ("Notebook", ["Notebook"]),
        ("note", ["Notebook"]),
        ("NOTEBOOK", ["Notebook"]),
        ("o", ["Notebook", "Water Bottle", "Coffee Mug"]),
        ("Laptop", []),
    ],
    ids=["exact", "partial", "ignore-case", "multiple", "no-match"],
)

def test_search_returns_matching_items(sample_inventory, search_term, expected_names):
    #Arrange
    inventory = sample_inventory

    #Act
    result = find_matching_items(inventory, search_term)

    #Assert
    actual_names = []

    for item in result:
        actual_names.append(item["Name"])

    assert actual_names == expected_names

@pytest.mark.parametrize("search_term",["", "   "],ids=["empty", "whitespace"],)
def test_search_rejects_blank_term(sample_inventory, search_term):
    #Arrange
    inventory = sample_inventory

    #Act
    result = find_matching_items(inventory, search_term)

    #Assert
    assert result == "Search term cannot be empty."
    
@pytest.mark.parametrize(
    "item_number, expected_names",
    [
        (1, ["Pencil", "Water Bottle", "Coffee Mug"]),
        (2, ["Notebook", "Water Bottle", "Coffee Mug"]),
        (4, ["Notebook", "Pencil", "Water Bottle"]),
    ],
    ids=["first", "middle", "last"],
)
def test_remove_item(sample_inventory, item_number, expected_names):
    #Arrange
    inventory = sample_inventory

    #Act
    remove_item_by_number(inventory, item_number)

    #Assert
    actual_names = []
    for item in inventory:
        actual_names.append(item["Name"])

    assert actual_names == expected_names
    
    
@pytest.mark.parametrize("item_number",[0, -1, 5],ids=["zero", "negative", "too-large"],)
def test_remove_invalid_number(sample_inventory, item_number):
    #Arrange
    inventory = sample_inventory
    original_inventory = []
    for item in inventory:
        original_inventory.append(item.copy())

    #Act
    result = remove_item_by_number(inventory, item_number)

    #Assert
    assert result is None
    assert inventory == original_inventory