import requests

url = "http://127.0.0.1:5000/generate"
payload = {
    "prompt": "Hello, how are you?",
    "mode": "text"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
