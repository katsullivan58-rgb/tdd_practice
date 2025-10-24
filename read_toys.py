import json
from typing import List
from item import Item

def read(filepath: str = 'toyinventory.json') -> List[Item]:
    """Reads the JSON file and returns a list of Item objects."""
    with open(filepath, 'r') as f:
        data = json.load(f)

    return [Item(d['name'], d['price'], d['count']) for d in data]
