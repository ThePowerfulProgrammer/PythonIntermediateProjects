import requests


site = requests.get("https://api.kanye.rest")
JSON = site.json()
print(JSON)
print(JSON['quote'])