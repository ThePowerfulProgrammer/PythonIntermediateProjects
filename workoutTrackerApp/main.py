import requests
from requests.auth import HTTPBasicAuth
from secret import Application_ID,APIKEY, SHEEETY_ENDPOINT, AuthHeader
import datetime

host_domain = "https://trackapi.nutritionix.com"

endpoint = f"{host_domain}/v2/natural/exercise"

Headers = {
    "x-app-id": Application_ID,
    "x-app-key": APIKEY 
}

parameters = {
    "query": input("Enter exercise: "),
    "weight_kg": 75,
    "height_cm": 170,
    "age": 23
}

postResponse = requests.post(url=endpoint,json=parameters, headers=Headers)
print(postResponse)
postResponse.raise_for_status()

JSON = postResponse.json()


for exercise in JSON['exercises']:
    body = {
        "sheet1" : {
            "date": datetime.datetime.today().strftime("%Y/%m/%d"),
            "time": datetime.datetime.today().time().strftime("%H:%M:%S"),
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    
    header = {
        "Authorization":AuthHeader,
    }
    
    sheetyPostResponse = requests.post(url=SHEEETY_ENDPOINT, json=body)
    
    
    
    
    
    print(sheetyPostResponse.raise_for_status())
    print(sheetyPostResponse.text)
