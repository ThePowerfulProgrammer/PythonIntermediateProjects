import requests
from prettytable import PrettyTable
from secret import amadeus_endpoint,amadeus_access_token


flight_finder_parameters = {
    "originLocationCode": "DUR",
    "destinationLocationCode": "CPT",
    "departureDate": "2024-08-20",
    "adults":1,
    "currencyCode": "ZAR",
    "maxPrice": 2000
    
}


print("Token ",amadeus_access_token)

flight_finder_headers = {
    "authorization": f"Bearer "
}
response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", params=flight_finder_parameters, headers=flight_finder_headers)
print(response.raise_for_status())
json = response.json()
     

flight_deals_table = PrettyTable()
flight_deals_table.field_names = ["Departure City", 
                                 "Departure DateTime",
                                  "Arrival City",
                                  "Arrival DateTime",
                                  "Final PD",
                                  "  ",
                                  "Currency Code",
                                  "Cost",
                                  "oneWay",
                                  "Seats Available",
                                  "Carrier"]
    

for i in range(17):
    flight_deals_table.add_row([f"{json['data'][i]['itineraries'][0]['segments'][0]['departure']['iataCode']}",
                                f"{ json['data'][i]['itineraries'][0]['segments'][0]['departure']['at']}", 
                                
                                f"{json['data'][i]['itineraries'][0]['segments'][0]['arrival']['iataCode']}",
                                f"{json['data'][i]['itineraries'][0]['segments'][0]['arrival']['at']}",
                                
                                f"{json['data'][i]['lastTicketingDate']}",
                                "  ",
                                
                                f"{json['data'][i]['price']['currency']}", 
                                
                                f"{json['data'][i]['price']['grandTotal']}", 
                                f"{not(json['data'][i]['oneWay'])}",
                                
                                f"{json['data'][i]['numberOfBookableSeats'] }",
                                f"{json['dictionaries']['carriers'][ json['data'][i]['itineraries'][0]['segments'][0]['carrierCode']  ]}",                                
                                
                                ])
    
print(flight_deals_table)





#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Find amazing flight deals
# Api's needed:
#     Flight finder API --> Find Flights
#     Google sheets API --> How to find flights
#     Gmail API --> Send an email to make me aware


# Google sheet: City, IATA Code, Lowest Price



