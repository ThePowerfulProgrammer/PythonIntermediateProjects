import requests 

parameters = {
    "t":"Proteas"
}

SPORTS_DB_ENDPOINT = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"

response = requests.get(SPORTS_DB_ENDPOINT, params=parameters)
response.raise_for_status()

print(response.json())