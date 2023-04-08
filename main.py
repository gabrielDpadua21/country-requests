import requests


BASE_URL = "https://restcountries.com/v2"


if __name__ == "__main__":
    country = input("Type the country name: ")
    response = requests.get(f"{BASE_URL}/name/{country}")
    if response.status_code == 200:
        print(response.text)