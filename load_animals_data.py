import json

def load_animal_data(file_path):
    """
    Loads a JSON file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data_list = load_animal_data('animals_data.json')