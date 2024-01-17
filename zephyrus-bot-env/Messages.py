import requests

url = "https://gate.whapi.cloud/chats"

headers = {
    "accept": "application/json",
    "authorization": "Bearer hLnmqrmxoMJxxa6krm8kHnfxjpNmEeg3"
}

response = requests.get(url, headers=headers)

print(response.text)