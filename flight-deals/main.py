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
    "authorization": f"Bearer token here"
}
response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", params=flight_finder_parameters, headers=flight_finder_headers)
print(response.raise_for_status())


json = response.json()

# print(json['data'][0]['source'])

# print(json['data'][0]['price']['currency'])

# print(json['data'][0]['price']['total'])

# print(json['data'][0]['price']['grandTotal'])

# print("Type: ",json['data'][0]['type'])
# print("id: " ,json['data'][0]['id'])
# print("Source: ",json['data'][0]['source'])
# print("Instant Ticket: ",json['data'][0]['instantTicketingRequired'])
# print("oneWay: " ,json['data'][0]['oneWay'])
# print("isUpSellOffer: " ,json['data'][0]['isUpsellOffer'])
# print("last Ticketing date: " ,json['data'][0]['lastTicketingDate'])
# print("ltdt: " ,json['data'][0]['lastTicketingDateTime'])
# print("number of bookable seats: " ,json['data'][0]['numberOfBookableSeats'])
# print("itineraries: " , json['data'][0]['itineraries'])        


flight_deals_table = PrettyTable()
flight_deals_table.field_names = ["Departure City", "Arrival City", "Currency Code","Cost (ZAR)", "oneWay",
                                  "Seats Available"]

    #   'itineraries': [
    #     {
    #       'duration': 'PT2H25M',
    #       'segments': [
    #         {
    #           'departure': {
    #             'iataCode': 'DUR',
    #             'at': '2024-08-20T08:40:00'
    #           },
    #           'arrival': {
    #             'iataCode': 'CPT',
    #             'at': '2024-08-20T11:05:00'
    #           },
    #           'carrierCode': '5Z',
    #           'number': '901',
    #           'aircraft': {
    #             'code': 'CR1'
    #           },
    #           'operating': {
    #             'carrierCode': '5Z'
    #           },
    #           'duration': 'PT2H25M',
    #           'id': '15',
    #           'numberOfStops': 0,
    #           'blacklistedInEU': False
    #         }
    #       ]
    #     }
    #   ],

for i in range(17):
    flight_deals_table.add_row(["DBN", "CPT",
                                f"{json['data'][i]['price']['currency']}", 
                                f"{json['data'][i]['price']['grandTotal']}", 
                                f"{not(json['data'][i]['oneWay'])}",
                                f"{json['data'][i]['numberOfBookableSeats'] }",
                                
                                ])
    
print(flight_deals_table)





#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Find amazing flight deals
# Api's needed:
#     Flight finder API --> Find Flights
#     Google sheets API --> How to find flights
#     Gmail API --> Send an email to make me aware


# Google sheet: City, IATA Code, Lowest Price



