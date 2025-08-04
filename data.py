

import requests
parameters = {
    "amount": 5,
    "category": 9,  # General Knowledge

    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # Ensure we raise an error for bad responses
data = response.json()

question_data = data["results"]
