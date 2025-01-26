import json
import requests


URL = "https://api.api-ninjas.com/v1/animals?name=fox"


def replace_animals_info_html(old_string, html_template, new_html_file_name, new_string):
    """
    Reads a html template and a txt, replaces a string from the template
    (old_string) with the contents from the txt
    Returns/overwrites a new html file with the changes
    """
    with open(html_template, "r") as handle:
        html_content = handle.read()

    new_html_file = html_content.replace(old_string, new_string)

    with open(new_html_file_name, 'w') as handle:
        handle.write(new_html_file)


def get_animal_info_cards(data):
    """
    Gets certain non-None info from each animal dictionary in the data and
    calls serialize_animal to format the info for each animal as a html card
    Returns a string
    """
    serialized_animal_objects = ""
    for animal in data:
        name = animal['name']
        diet = animal['characteristics'].get('diet')
        location = animal['locations'][0]
        type_maybe = animal['characteristics'].get('type')

        animal_object = [name, diet, location, type_maybe]
        # felt very tempted of making a class Animal
        # but that isn't what this assignment asks

        serialized_animal_objects += serialize_animal_info(animal_object)

    return serialized_animal_objects


def serialize_animal_info(animal_object):
    """
    Serializes and returns an animal card from an animal object
    """
    animal_card = ""
    animal_card += ("<li class='cards__item'>\n"
                    f"\t\t\t\t<div class='card__title'>{animal_object[0]}</div>\n"
                    "\t\t\t\t<p class='card__text'>\n"
                    "\t\t\t\t\t<ul class='card__text'>\n"
                    f"\t\t\t\t\t\t<li class='card'><strong>Diet:</strong> {animal_object[1]}</li>\n"
                    f"\t\t\t\t\t\t<li class='card'><strong>Location:</strong> {animal_object[2]}</li>\n")
    if animal_object[3] is not None:
        animal_card += f"\t\t\t\t\t\t<li class='card'><strong>Type:</strong> {animal_object[3]}</li>\n"
    animal_card += ("\t\t\t\t\t</ul>\n"
                    "\t\t\t\t<p>\n"
                    "\t\t\t</li>\n"
                    "\t\t\t")

    return animal_card


def load_animal_data(file_path):
    """
    Loads a JSON file
    """
    with open(requests.get(URL).json(), "w") as handle:
        handle.write(file_path)


def main():
    animals_data = load_animal_data('animals_data.json') # as a list of dictionaries
    new_string = get_animal_info_cards(animals_data)
    string_to_be_replaced = "__REPLACE_ANIMALS_INFO__" # it would be better as user input but hardcoded it is
    new_html_file_name = "animals.html" # as a variable in main in case I need to change the name again
    replace_animals_info_html(string_to_be_replaced, "animals_template.html",
                              new_html_file_name, new_string)


if __name__ == "__main__":
    main()
