##########################################################################################
# API used: https://rapidapi.com/skyscanner/api/skyscanner-flight-search?endpoint=5a9ca032e4b04378c0c99930
#
#    >>>>> Application for flight tickets search <<<<<
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
  "adults": 1
}

# Optional parameters
opt_params = {
  "inboundDate": "2019-05-10",
  "cabinClass": "business",
  "children": 0,
  "infants": 0,
  "includeCarriers": "",
  "excludeCarriers": "",
  "groupPricing": 0
}

# merge
parameters = merge_dicts(required_params, opt_params)


##########################################################################################
# Search

# POST Create session
"""
Create a flight search session. A successful response contains no content. 
The session key to poll the results is provided in the Location header of the 
response. The last value of location header contains the session key which is 
required when polling the session. 
"""

source = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"
post_response = unirest.post(source,
  headers={
    "X-RapidAPI-Key": "c5567760d2msh8aee5dc9ea49120p1b7f06jsndeadf5b02269",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  params = parameters
)

# Add error handling here
if False:
  sys.exit()

# GET Poll session results
"""
Get itineraries from a created session.
Key received in post header must be inserted in src string.
"""

# session_key = ".../{session_key}""
session_key = post_response.headers["Location"]
last_slash_pos = session_key.rfind("/")
session_key = session_key[last_slash_pos+1:]

# insert session key in GET source
source = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/"\
  + session_key + "?"

get_response = unirest.get(source,
  headers={
    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "e08015148bmsh741474b8af3942ap1b29d7jsnc1343256972b"
  }
)

# Add error handling here
if False:
  sys.exit()

##########################################################################################
# Handle data result










