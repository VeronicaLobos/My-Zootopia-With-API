import load_animals_data

ANIMALS_DATA = load_animals_data.animals_data_list


def get_animal_info(data):
    """
   :param data:
   :return: A list of tuples
   """
    animal_info_list = []
    for animal in data:
        name = f"Name: {animal['name']}\n"
        diet = f"Diet: {animal['characteristics'].get('diet')}\n"
        location = f"Location: {animal['locations'][0]}\n"
        type = f"Type: {animal['characteristics'].get('type')}\n\n"

        animal_info = (name, diet, location)
        if type is not None:
            animal_info += (type,) #new to think a bit more about this

        animal_info_list.append(animal_info)

    print(animal_info_list)


get_animal_info(ANIMALS_DATA)
