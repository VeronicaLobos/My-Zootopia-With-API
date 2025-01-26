import requests as req
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("my_api_key")

URL = "https://api.api-ninjas.com/v1/animals?name=dog"


def check_query_status():

    headers = {"X-Api-Key" : API_KEY}
    payload = {"animal": input("What animal would you like to inquire about? ")}

    animal_query = req.get(URL, payload).url
    response = req.get(animal_query, headers=headers)

    if response.status_code == 200:
        print(f"{animal_query} is green, proceed")
        return response.json()
    else:
        print(f"Error: {response.status_code}")


def save_json_file():
    pass


def main():
    animal_json = check_query_status()
    print(animal_json)
    #save_json_file(animal_json)

if __name__ == "__main__":
    main()
