import requests

url = "http://127.0.0.1:5000/signup"

data = {
    "name" : "Ana",
    "email" : "ana@gmail.com",
    "password"  : "ana2345",
}

response = requests.post(url, json=data)

print("Response from server", response.json())
