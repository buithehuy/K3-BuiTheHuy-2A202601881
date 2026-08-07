import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
if response.status_code == 200:
    models = response.json().get("data", [])
    print("Available Groq models:")
    for model in models:
        print(f" - {model['id']}")
else:
    print(f"Error fetching models: {response.status_code} {response.text}")
