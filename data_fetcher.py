import requests as req
from dotenv import load_dotenv
import os


load_dotenv()

### API_KEY = os.environ.get("my_api_key")
API_KEY = os.getenv("my_api_key")

URL = "https://api.api-ninjas.com/v1/animals"


def get_animal_info(animal_name):
    """

    :param animal_name: The name of the animal to look for
    :return: A json response as a string if requests is successful,
    an error message indicating
    """
    headers = {"X-Api-Key" : API_KEY}
    payload = {"name": animal_name}

    try:
        animal_query = req.get(URL, payload).url
        response = req.get(animal_query, headers=headers)
        response.raise_for_status()
        print(f"Requesting '{animal_name}' to {URL}")
        return response.text
    except ValueError as e:
        print(f"Error: {e}")
        return
    except NameError as e:
        print(f"Error: {e}")
        return "Check URL and API key and try again."


def save_json_file(json_obj):
    """
    """
    with open("animal.json", "w", encoding="utf-8") as handle:
        handle.write(json_obj)


def fetch_json_file(animal_name):  # change name duh
    """
    """
    animal_json = get_animal_info(animal_name)
    save_json_file(animal_json)