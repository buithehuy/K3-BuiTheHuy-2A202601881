import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
payload_template = {"messages": [{"role": "user", "content": "hello"}], "max_tokens": 10}

response = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
if response.status_code == 200:
    models = response.json().get("data", [])
    for model in models:
        m_id = model['id']
        payload = dict(payload_template)
        payload["model"] = m_id
        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        if res.status_code == 200:
            print(f"Working model: {m_id}")
            break
