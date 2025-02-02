import json
import data_fetcher


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
    animal_card += (f"<li class='cards__item'>\n"
                    f"\t\t\t\t<div class='card__title'>{animal_object[0]}</div>\n"
                    f"\t\t\t\t<p class='card__text'>\n"
                    f"\t\t\t\t\t<ul class='card__text'>\n"
                    f"\t\t\t\t\t\t<li class='card'><strong>Diet:</strong> {animal_object[1]}</li>\n"
                    f"\t\t\t\t\t\t<li class='card'><strong>Location:</strong> {animal_object[2]}</li>\n")
    if animal_object[3] is not None:
        animal_card += f"\t\t\t\t\t\t<li class='card'><strong>Type:</strong> {animal_object[3]}</li>\n"
    animal_card += (f"\t\t\t\t\t</ul>\n"
                    f"\t\t\t\t<p>\n"
                    f"\t\t\t</li>\n"
                    f"\t\t\t")

    return animal_card


def load_animal_data(file_path):
    """
    Loads a JSON file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_user_input():
  """
  Gets user input, checks that the user didn't input an empty string,
  in which case will prompt the user to return a valid input.
  Returns  a string.
  """
  while True:
    user_input = input("What animal name would you like to search for? ")
    if len(user_input) > 0:
        return user_input
    else:
        print("Please, enter a valid input before pressing return.")
        continue


def main():
    """
    1. Gets user input to search for an animal name at Animal API
    2. Makes a request to Animal API and saves it into a json file
    3. Loads the json file to a variable as a list of dictionaries
    If the list isn't empty:
    4. Parses the list of dictionaries into a string containing html cards
    5. Generates the html file from a template, by replacing a
        hardcoded string with the html cards
    Otherwise:
    6. Generates a "not found" html file, by replacing the text
        with a header indicating the non-existing input

    :return:
    """
    string_to_be_replaced = "__REPLACE_ANIMALS_INFO__"

    animal_name = get_user_input()  # Milestone 2
    data_fetcher.fetch_json_file(animal_name)  # Milestone 1
    animals_data = load_animal_data("animal.json")

    if len(animals_data) > 2:
        new_string = get_animal_info_cards(animals_data)
        replace_animals_info_html(string_to_be_replaced, "animals_template.html",
                              f"{animal_name}.html", new_string)
        print("Zootopia with API successfully generated!")
    else:  # Milestone 3
        not_found_string = f"<h2>The animal <em>{animal_name}</em> doesn't exist...</h2>"
        print(f"{animal_name} not found...")
        replace_animals_info_html(string_to_be_replaced, "animals_template.html",
                                  "not_found.html", not_found_string)
        print("But at least the program didn't crash!")


if __name__ == "__main__":
    main()
