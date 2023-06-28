import random

import requests

def generate_token():
    no =random.randint(1, 99999999999999999)
    request_body = {
        "clientName": "Mircea",
        "clientEmail": f"mirci{no}@example.com"
    }
    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json=request_body)
    return response.json()["accessToken"]