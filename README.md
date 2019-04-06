### Description

Implementation of flight tickets search for multiple destinations in python using 
[Skyscanner Flight Search-API](https://rapidapi.com/skyscanner/api/skyscanner-flight-search/details).


### Example 

searchMultipleDestinations.py

Input:
```python
origin = "ORD"
destinations = [\
    "SFO",\
    "OAK",\
    "SJC"]
outboundDate = "2019-04-11"
inboundDate  = "2019-04-14"
```

Output:
```
From ORD to SFO.
From 2019-04-11 to 2019-04-14.

Cheapest quotes (USD):

  1) MinPrice: 342.0, not direct
      Outbound:
        Departure: 2019-04-11T00:00:00
        Carrier(s):  Frontier Airlines
      Inbound:
        Departure: 2019-04-14T00:00:00
        Carrier(s):  Frontier Airlines

  2) MinPrice: 427.0, direct
      Outbound:
        Departure: 2019-04-11T00:00:00
        Carrier(s):  American Airlines
      Inbound:
        Departure: 2019-04-14T00:00:00
        Carrier(s):  American Airlines


From ORD to OAK.
From 2019-04-11 to 2019-04-14.

Cheapest quotes (USD):

  1) MinPrice: 436.0, not direct
      Outbound:
        Departure: 2019-04-11T00:00:00
        Carrier(s):  Spirit Airlines
      Inbound:
        Departure: 2019-04-14T00:00:00
        Carrier(s):  Spirit Airlines


From ORD to SJC.
From 2019-04-11 to 2019-04-14.

Cheapest quotes (USD):

  1) MinPrice: 591.0, direct
      Outbound:
        Departure: 2019-04-11T00:00:00
        Carrier(s):  United
      Inbound:
        Departure: 2019-04-14T00:00:00
        Carrier(s):  United
```