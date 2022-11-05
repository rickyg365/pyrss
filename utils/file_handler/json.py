import json
from typing import Any


def save_json(data: Any, filepath: str):
    with open(filepath, 'w') as save_file:
        json.dump(data, save_file, indent=4)

def load_json(filepath: str):
    with open(filepath, 'r') as load_file:
        return json.load(load_file)
