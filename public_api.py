import requests
from base64 import b64encode
from pprint import pprint

# Define the url and the data to be sent
url = "https://api.techinterviewer.ai/sessions"
data = {"interview_config_id": "663addb129ba3bee5086a58b"} # CustomerSupportInterview

# Define the username and the api_key
username = "shreyas.jaganmohan@gmail.com"
api_key = "15593c18-2159-49cc-a864-b2031780f0c2"

# Encode the username and api_key using base64
credentials = b64encode(bytes(f"{username}:{api_key}", encoding='utf8')).decode('utf8')

# Define the headers
headers = {
    "Authorization": f"Basic {credentials}"
}

# Make the POST request
response = requests.post(url, json=data, headers=headers)

# Print the session object
resJson = response.json()
print('response of POST /sessions from creating the session', resJson)

# Make a GET request to /sessions with basic auth and pass in the session id
session_id = resJson.get('id')  # replace with your session id
session_url = f"{url}/{session_id}"
session_response = requests.get(session_url, headers=headers)

# Print the session details
pprint(session_response.json())
