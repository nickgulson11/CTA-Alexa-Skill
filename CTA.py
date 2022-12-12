import requests
import json

train_api_key = "7edf9206960247dfad403efa90a3c88f"
bus_api_key = "hyTi6EDZxyNFxe5nJefGbm4Ts"
api_url = "http://lapi.transitchicago.com/api/1.0/"
endpoints = json.loads('{"arrivals" : "ttarrivals.aspx"}')
mapid = "40630" # Clark & Division

response = requests.get(api_url + endpoints['arrivals'] + "?key=" + train_api_key + "&max=6&mapid=" + mapid + "&outputType=JSON")
if response.status_code != 200:
        print('error')
else:        
    trains = response.json()
    trains = trains['ctatt']['eta']
    northbound = []
    southbound = []
    for i in trains:
        if i['destNm'] == 'Howard':
            northbound.append(i['arrT'])
        elif i['destNm'] == '95th/Dan Ryan':
            southbound.append(i['arrT'])
    print("Northbound Trains: ", northbound)
    print("Southbound Trains: ", southbound)



