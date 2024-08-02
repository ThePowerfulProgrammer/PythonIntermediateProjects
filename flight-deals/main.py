import requests
from secret import amadeus_endpoint


flight_finder_parameters = {
    "originLocationCode": "SYD",
    "destinationLocationCode": "BKK",
    "departureDate": "2024-08-20",
    "adults":1,
    "maxPrice": 300
    
}

flight_finder_headers = {
    "authorization": f"Bearer w8ANPU1nYTnkhjLMbGInjGPnZZWz"
}
response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", params=flight_finder_parameters, headers=flight_finder_headers)
print(response.raise_for_status())


json = response.json()
print(json)





#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Find amazing flight deals
# Api's needed:
#     Flight finder API --> Find Flights
#     Google sheets API --> How to find flights
#     Gmail API --> Send an email to make me aware


# Google sheet: City, IATA Code, Lowest Price



