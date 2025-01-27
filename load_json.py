import requests as req
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.environ.get("my_api_key")

URL = "https://api.api-ninjas.com/v1/animals"


def get_animal_info():
    """
    Checks for the status
    :return: A list of
    """
    headers = {"X-Api-Key" : API_KEY}
    payload = {"name": input("What animal would you like to inquire about? ")}
    # make this input in the main script later

    animal_query = req.get(URL, payload).url
    response = req.get(animal_query, headers=headers)

    if response.status_code == 200:
        print(f"{animal_query} is green, proceed")
        return str(response.text)

    else:
        print(f"Error: {response.status_code}")


def check_input(content):
    if content == '[]':
        print("Animal name not found.")


def save_json_file(json_obj):
    with open("animal.json", "w", encoding="utf-8") as handle:
        handle.write(json_obj)


def fetch_json_file():  # change name duh
    animal_json = get_animal_info()
    #print(animal_json)
    check_input(animal_json)
    save_json_file(animal_json)