import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.json()["current_user_url"])
