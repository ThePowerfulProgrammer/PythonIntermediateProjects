import requests
from prettytable import PrettyTable
import smtplib
from secret import amadeus_endpoint,amadeus_access_token



endpoint = "https://api.sheety.co/a51ec32c3d55dea8bc8eb9b96bcf0953/flightDeals/sheet1"
flightLocationsResponse = requests.get(url=endpoint)
flightLocationsResponse.raise_for_status()
FLRJ = flightLocationsResponse.json()

locationCode = []
destinationCities = []
destinationCode = []
destinationPrice = []


for i in range(len(FLRJ['sheet1'])):
    locationCode.append(FLRJ['sheet1'][i]['origin'] )
    destinationCities.append(FLRJ['sheet1'][i]['city'])
    destinationCode.append(FLRJ['sheet1'][i]['iataCode'])
    destinationPrice.append(FLRJ['sheet1'][i]['lowestPrice'])
    
print(locationCode)
print(destinationCities)
print(destinationCode)
print(destinationPrice)

flight_deals_table = PrettyTable()
flight_deals_table.field_names = ["Departure City", 
                                "Departure DateTime",
                                "Arrival City",
                                "Arrival DateTime",
                                "Final PD",
                                "Currency Code",
                                "Cost",
                                "oneWay",
                                "Seats Available",
                                "Carrier"]

flight_finder_headers = {
    "authorization": f"Bearer "
}


for i in range(len(destinationCode)):
        
    flight_finder_parameters = {
        "originLocationCode": locationCode[i],
        "destinationLocationCode": destinationCode[i],
        "departureDate": "2024-08-20",
        "adults":1,
        "currencyCode": "ZAR", 
        "maxPrice": destinationPrice[i]
        
    }

    print("Token ",amadeus_access_token)

    response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", params=flight_finder_parameters, headers=flight_finder_headers)
    print(response.raise_for_status())
    json = response.json()
        

    for i in range(json['meta']['count']):
        flight_deals_table.add_row([f"{json['data'][i]['itineraries'][0]['segments'][0]['departure']['iataCode']}",
                                    f"{ json['data'][i]['itineraries'][0]['segments'][0]['departure']['at']}", 
                                    
                                    f"{json['data'][i]['itineraries'][0]['segments'][0]['arrival']['iataCode']}",
                                    f"{json['data'][i]['itineraries'][0]['segments'][0]['arrival']['at']}",
                                    
                                    f"{json['data'][i]['lastTicketingDate']}",
                                    
                                    f"{json['data'][i]['price']['currency']}", 
                                    
                                    f"{json['data'][i]['price']['grandTotal']}", 
                                    f"{not(json['data'][i]['oneWay'])}",
                                    
                                    f"{json['data'][i]['numberOfBookableSeats'] }",
                                    f"{json['dictionaries']['carriers'][ json['data'][i]['itineraries'][0]['segments'][0]['carrierCode']  ]}",                                
                                    

                                    ])
            
print(flight_deals_table)


# with smtplib.SMTP("smtp.gmail.com") as conn:
#     conn.starttls()
#     conn.login(user="azuraramnath@gmail.com", password="geof xuax dufw mict")
    
#     conn.sendmail(
#         from_addr="azuraramnath@gmail.com",
#         to_addrs="ashishr0301@gmail.com",
#         msg=f"Subject:Flight Deals\n\n{flight_deals_table}"
#     )






