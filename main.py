import json

import requests


BASE_URL = "https://restcountries.com/v2"


if __name__ == "__main__":
    country = input("Type the country name: ")
    response = requests.get(f"{BASE_URL}/name/{country}")
    if response.status_code == 200:
        infos = json.loads(response.text)[0]
        print("##############################")
        for data in infos:
            print(f"{data}: {infos[data]}")
        print("##############################")