import requests

# Check Server Cloud
url = "https://gate.whapi.cloud/health?wakeup=true&channel_type=web"

# Get Channel Settings
# url = "https://gate.whapi.cloud/settings"

# Get allowed events
# url = "https://gate.whapi.cloud/settings/events"

# Get Limits
# url = "https://gate.whapi.cloud/limits"

headers = {
    "accept": "application/json",
    "authorization" : "Bearer hLnmqrmxoMJxxa6krm8kHnfxjpNmEeg3"
    }

response = requests.get(url, headers=headers)

print(response.text)