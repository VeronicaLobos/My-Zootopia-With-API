import json

def replace_animals_info_html(old_string, html_file, txt_file):
    """
    Creates a new html file by copying a template, and modifying its contents
    with text from a txt file.
    """
    with open(txt_file, "r") as handle:
        replacement_text = handle.read()

    with open(html_file, "r") as handle:
        html_content = handle.read()

    replacement_text = replacement_text
    new_html_content = html_content.replace(old_string, replacement_text)

    with open("animals_template.html", 'w') as handle:
        handle.write(new_html_content)


def write_animals_data(string):
    """
    Writes a string into a .txt file
    """
    with open("replacement_text.txt", "w") as file:
        file.write("<p>" + string + "</p>")


def get_print_animal_info(data):
    """
   From a list of dictionaries, gets certain values,
   and prints a formated string for each dictionary.
   """
    animals_string = ""
    for animal in data:
        name = animal['name']
        diet = animal['characteristics'].get('diet')
        location = animal['locations'][0]
        type = animal['characteristics'].get('type')

        animals_string += f"Name: {name}Diet: {diet}\nLocation: {location}\n"
        if type is not None:
            animals_string += f"Type: {type}\n"
        animals_string += "\n"

    return animals_string


def load_animal_data(file_path):
    """
    Loads a JSON file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    ANIMALS_DATA = load_animal_data('animals_data.json')
    animals_info = get_print_animal_info(ANIMALS_DATA)
    write_animals_data(animals_info)
    string_to_be_replaced = "__REPLACE_ANIMALS_INFO__" #I'll hardcode it for now
    replace_animals_info_html(string_to_be_replaced, "old_animals_template.html", "replacement_text.txt")


if __name__ == "__main__":
    main()
