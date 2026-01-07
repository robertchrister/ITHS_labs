# client.py
# FLAG{automation_beats_manual}

import os
import requests
from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv("API_BASE")
TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "5"))


session = requests.session()
session.headers.update({
    "Accept": "application/json"
})

# Fetch Token
response = session.post(f"{BASE_URL}/api/token", timeout=TIMEOUT)
response.raise_for_status()
token = response.json()["token"]

# verify Token
session.headers.update({
    "Authorization": f"Bearer {token}"
})

response = session.post(f"{BASE_URL}/api/verify", timeout=TIMEOUT)
response.raise_for_status()
secret = response.json()["secret"]



response = session.post(f"{BASE_URL}/api/flag", json={"secret": secret}, timeout=TIMEOUT)

response.raise_for_status()

print(response.json()["flag"])

