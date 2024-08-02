import requests
from secret import amadeus_endpoint,amadeus_access_token


flight_finder_parameters = {
    "originLocationCode": "SYD",
    "destinationLocationCode": "BKK",
    "departureDate": "2024-08-20",
    "adults":1,
    "maxPrice": 300
    
}


print("Token ",amadeus_access_token)

flight_finder_headers = {
    "authorization": f"Bearer Only use when running"
}
response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", params=flight_finder_parameters, headers=flight_finder_headers)
print(response.raise_for_status())


json = response.json()
print(json['meta'])

print(json['data'][0]['source'])

print(json['data'][0]['price']['currency'])

print(json['data'][0]['price']['total'])






#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Find amazing flight deals
# Api's needed:
#     Flight finder API --> Find Flights
#     Google sheets API --> How to find flights
#     Gmail API --> Send an email to make me aware


# Google sheet: City, IATA Code, Lowest Price



