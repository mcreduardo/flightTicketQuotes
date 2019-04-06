##########################################################################################
# API used: https://rapidapi.com/skyscanner/api/skyscanner-flight-search?endpoint=5a9ca032e4b04378c0c99930
#
#    >>>>> Search for cheap quotes for multiple destinations given dates <<<<<
#
# note: Implemented for python 2 only
# March 2019
# Eduardo Moura Cirilo Rocha
##########################################################################################

import sys
from browseQuotes import browseQuotes

origin = "MSN"
destinations = [\
    "SFO",\
    "OAK",\
    "SJC"]
outboundDate = "2019-04-11"
inboundDate  = "2019-04-14"

for destination in destinations:
    # Search Parameters
    # required parameters
    required_params = {
    "country": "US",
    "currency": "USD",
    "locale": "en-US",
    "originPlace": origin,
    "destinationPlace": destination,
    "outboundDate": outboundDate,
    "inboundDate": inboundDate,
    }

    browseQuotes(required_params = required_params, printOutput = True)
