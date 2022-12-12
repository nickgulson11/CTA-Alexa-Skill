import requests
import json

train_api_key = "7edf9206960247dfad403efa90a3c88f"
bus_api_key = "hyTi6EDZxyNFxe5nJefGbm4Ts"
api_url = "http://lapi.transitchicago.com/api/1.0/"
endpoints = json.loads('{"arrivals" : "ttarrivals.aspx"}')

x = requests.get(api_url + endpoints['arrivals'] + "?key=" + train_api_key + "&max=4&mapid=40360&outputType=JSON")
print(x.json())