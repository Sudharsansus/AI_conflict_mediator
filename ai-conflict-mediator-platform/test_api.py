import requests

url = "http://127.0.0.1:8000/analyze/"
payload = {
    "message": "You always interrupt me in meetings and it’s frustrating."
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
