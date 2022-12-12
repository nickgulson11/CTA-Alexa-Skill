import requests
import json

train_api_key = "7edf9206960247dfad403efa90a3c88f"
bus_api_key = "hyTi6EDZxyNFxe5nJefGbm4Ts"
api_url = "http://lapi.transitchicago.com/api/1.0/"
endpoints = json.loads('{"arrivals" : "ttarrivals.aspx"}')
mapid = "40630" # Clark & Division

x = requests.get(api_url + endpoints['arrivals'] + "?key=" + train_api_key + "&max=4&mapid=" + mapid + "&outputType=JSON")
print(x.json())