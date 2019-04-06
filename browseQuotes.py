##########################################################################################
# API used: https://rapidapi.com/skyscanner/api/skyscanner-flight-search?endpoint=5a9ca032e4b04378c0c99930
#
#    >>>>> Get cheapest quotes from cache prices <<<<<
#
# note: Implemented for python 2 because of limitations of lybrary unirest
# March 2019
# Eduardo Moura Cirilo Rocha
##########################################################################################

import unirest
import json
import sys


def merge_dicts(x, y):
  z = x.copy()
  z.update(y)
  return z

def getCarrier(ids, carriers):
  carriers_found = ""
  for id in ids:
    for carrier in carriers:
      if carrier["CarrierId"] == id:
        carriers_found = carriers_found + " " + carrier["Name"]
  return carriers_found

##########################################################################################

def browseQuotes(required_params, printOutput):
  
  # Search
  # GET Browse Quotes
  """
  Retrieve the cheapest quotes from our cache prices.
  """
  # GET source
  source = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"\
    + "/apiservices/browsequotes/v1.0"\
    + "/" + required_params["country"]\
    + "/" + required_params["currency"]\
    + "/" + required_params["locale"]\
    + "/" + required_params["originPlace"]\
    + "/" + required_params["destinationPlace"]\
    + "/" + required_params["outboundDate"]\
    + "/" + required_params["inboundDate"]
  response = unirest.get(source,
    headers={
      "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
      "X-RapidAPI-Key": "e08015148bmsh741474b8af3942ap1b29d7jsnc1343256972b"
    }
  )

  # Error handling 
  if "ValidationErrors" in response.body:
    print "\nValidation error when browsing quotes:\n"
    print json.dumps(response.body["ValidationErrors"][0], indent=4)
    print ""
    sys.exit()

  #print json.dumps(response.body, indent=4)
  #print response.headers





  ##### Handle data result

  # Search info
  print ""
  print "From " + response.body["Places"][1]["CityName"]\
    + " (" + response.body["Places"][1]["SkyscannerCode"] + ")"\
    + ", " + response.body["Places"][1]["CountryName"] + ", "\
    + "to " + response.body["Places"][0]["CityName"]\
    + " (" + response.body["Places"][0]["SkyscannerCode"] + ")"\
    + ", " + response.body["Places"][0]["CountryName"] + "."
  print "From " + required_params["outboundDate"]\
    + " to " + required_params["inboundDate"] + "."

  # Cheapest quotes:
  print "\nCheapest quotes ("+ response.body["Currencies"][0]["Code"] +"):\n"

  if printOutput:
    i = 1
    for quote in response.body["Quotes"]:
      if quote["Direct"]: direct_str = ", direct"
      else: direct_str = ", not direct"

      print "\t".expandtabs(2) + str(i) + ") " + "MinPrice: "\
        + str(quote["MinPrice"]) + direct_str
      print "\tOutbound:".expandtabs(6)
      print "\tDeparture: ".expandtabs(8) + quote["OutboundLeg"]["DepartureDate"]
      print "\tCarrier(s): ".expandtabs(8)\
        + getCarrier(quote["OutboundLeg"]["CarrierIds"], response.body["Carriers"])
      print "\tInbound:".expandtabs(6)
      print "\tDeparture: ".expandtabs(8) + quote["InboundLeg"]["DepartureDate"]
      print "\tCarrier(s): ".expandtabs(8)\
        + getCarrier(quote["InboundLeg"]["CarrierIds"], response.body["Carriers"])
      print ""

      i += 1
  
  return response






##########################################################################################

if __name__=="__main__":

  # Search Parameters
  # required parameters
  required_params = {
    "country": "US",
    "currency": "USD",
    "locale": "en-US",
    "originPlace": "SFO-sky",
    "destinationPlace": "LHR-sky",
    "outboundDate": "2019-05-01",
    "inboundDate": "2019-05-10",
  }
  # Optional parameters
  opt_params = {
  }

  browseQuotes(required_params = required_params, printOutput = True)

