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

##########################################################################################
# Search Parameters

# required parameters
required_params = {
  "country": "US",
  "currency": "USD",
  "locale": "en-US",
  "originPlace": "SFO-sky",
  "destinationPlace": "LHR-sky",
  "outboundDate": "2019-05-01",
}

# Optional parameters
opt_params = {
  "inboundDate": "2019-05-10",
}

# merge
parameters = merge_dicts(required_params, opt_params)


##########################################################################################
# Search

# GET Browse Quotes
"""
Retrieve the cheapest quotes from our cache prices.
"""

# GET source
source = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0"\
  + "/" + required_params["country"]\
  + "/" + required_params["currency"]\
  + "/" + required_params["locale"]\
  + "/" + required_params["originPlace"]\
  + "/" + required_params["destinationPlace"]\
  + "/" + required_params["outboundDate"]\
  + "?inboundpartialdate=" + opt_params["inboundDate"]
  

response = unirest.get(source,
  headers={
    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "e08015148bmsh741474b8af3942ap1b29d7jsnc1343256972b"
  }
)

# Add error handling here
if False:
  sys.exit()

print json.dumps(response.body, indent=4)

##########################################################################################
# Handle data result










