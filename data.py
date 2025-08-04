

import requests
parameters = {
    "amount": 20, #change this to get more or fewer questions
    "category": 9,  # change this to get questions from different categories

    "type": "boolean" # change this to "multiple" for multiple choice questions
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # Ensure we raise an error for bad responses
data = response.json()

question_data = data["results"]
