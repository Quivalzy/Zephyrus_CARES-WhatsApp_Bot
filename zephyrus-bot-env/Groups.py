import requests

url = "https://gate.whapi.cloud/groups"

# Create Group

payload = {
    "participants": ["62881082358048"],
    "subject": "Zephyrus Bot Group Testing"
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer hLnmqrmxoMJxxa6krm8kHnfxjpNmEeg3"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)