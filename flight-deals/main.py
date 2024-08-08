from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# 1) Grab google sheet here
dataManger = DataManager()

# 2) Create flight finder

destinationCodes = dataManger.getDestinationCodes()
locationCodes = dataManger.getLocationCode()
destinationPrices = dataManger.getDestinationPrice()

flightSearch = FlightSearch(destinationCodes,locationCodes, destinationPrices)

# 3) create the table
flightData = FlightData(flightSearch.getJson())
flightData.createRows()
print(flightData.getTable())

# 4) Email the table
# notificationManager = NotificationManager(flight_data=flightData.getTable())
# notificationManager.sendMail()





