import requests


API_URL = "https://www.giantbomb.com/api/games/"
parameters = {
    "amount":10,
    "type":"boolean"
    }


response = requests.get(API_URL)
response.raise_for_status()
# data = response.json()
# question_data = data["results"]

print(response)