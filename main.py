import load_animals_data

ANIMALS_DATA = load_animals_data.animals_data_list


def get_print_animal_info(data):
    """
   From a list of dictionaries, gets certain values,
   and prints a formated string for each dictionary.
   """
    for animal in data:
        name = animal['name']
        diet = animal['characteristics'].get('diet')
        location = animal['locations'][0]
        type = animal['characteristics'].get('type')

        animal_info = f"Name: {name}\nDiet: {diet}\nLocation: {location}\n"
        if type is not None:
            animal_info += f"Type: {type}\n"

        print(animal_info)

def main():
    get_print_animal_info(ANIMALS_DATA)

if __name__ == "__main__":
    main()
