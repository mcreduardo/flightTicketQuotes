# https://rapidapi.com/skyscanner/api/skyscanner-flight-search?endpoint=5a9ca032e4b04378c0c99930

import unirest
import json





# required parameters
country = "US"
currency = "USD"
locale = "en-US"
originPlace = "SFO-sky"
destinationPlace = "LHR-sky"
adults = 1
outboundDate = "2019-05-01"

# Optional parameters
inboundDate = "2019-05-10"
cabinClass = "economy" # “economy”, “premiumeconomy”, “business”, “first”
children = 0
infants = 0
includeCarriers = ""
excludeCarriers = ""
groupPricing = False

# Create session
response = unirest.post("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0",
  headers={
    "X-RapidAPI-Key": "c5567760d2msh8aee5dc9ea49120p1b7f06jsndeadf5b02269",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  params={
    "inboundDate": "2019-05-10",
    "cabinClass": "business",
    "children": 0,
    "infants": 0,
    "country": "US",
    "currency": "USD",
    "locale": "en-US",
    "originPlace": "SFO-sky",
    "destinationPlace": "LHR-sky",
    "outboundDate": "2019-05-01",
    "adults": 1
  }
)

print "\n\n"
print response.headers['Location']
print response.body
print "\n\n"



string = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/SFO-sky/JFK-sky/2019-05-01?inboundpartialdate=2019-05-01"

response = unirest.get("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/69f914b9-eaaf-48ee-8c2b-b3c954d2152f?pageIndex=0&pageSize=10",
  headers={
    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "e08015148bmsh741474b8af3942ap1b29d7jsnc1343256972b"
  }
).body

print "\n\n"
print response
print "\n\n"