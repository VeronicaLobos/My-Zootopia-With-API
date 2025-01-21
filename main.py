import json

def replace_animals_info_html(old_string, html_template, new_html_file_name, txt_file):
    """
    Reads a html template and a txt, replaces a string from the template
    (old_string) with the contents from the txt
    Returns/overwrites a new html file with the changes
    """
    with open(txt_file, "r") as handle:
        replacement_text = handle.read()

    with open(html_template, "r") as handle:
        html_content = handle.read()

    new_html_file = html_content.replace(old_string, replacement_text)

    with open(new_html_file_name, 'w') as handle:
        handle.write(new_html_file)


def write_animals_data(string):
    """
    Writes a html formated string and
    returns it as a txt file
    """
    with open("replacement_text.txt", "w") as file:
        file.write(string)


def get_animal_info_cards(data):
    """
   From a list of dictionaries, gets certain non-None values
   Returns a html formated string for each dictionary (each as a card)
   """
    output = ""
    for animal in data:
        name = animal['name']
        diet = animal['characteristics'].get('diet')
        location = animal['locations'][0]
        type = animal['characteristics'].get('type')

        #animals_string += f"Name: {name}\nDiet: {diet}\nLocation: {location}\n"
        #if type is not None:
        #    animals_string += f"Type: {type}\n"
        #animals_string += "\n"

        output += f"<li class='cards__item'>Name: {name}<br/>\nDiet: {diet}<br/>\nLocation: {location}<br/>\n"
        if type is not None:
            output += f"Type: {type}<br/>\n"
        output += "</li>\n"

    return output


def load_animal_data(file_path):
    """
    Loads a JSON file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    ANIMALS_DATA = load_animal_data('animals_data.json') # as a list of dictionaries
    animals_info_cards = get_animal_info_cards(ANIMALS_DATA)
    write_animals_data(animals_info_cards)
    string_to_be_replaced = "__REPLACE_ANIMALS_INFO__" # it would be better as user input but hardcoded it is
    new_html_file_name = "animals.html" # as a variable in main in case I need to change the name again
    replace_animals_info_html(string_to_be_replaced, "animals_template.html", new_html_file_name,"replacement_text.txt")


if __name__ == "__main__":
    main()
