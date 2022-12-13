import requests
import json
from datetime import datetime

train_api_key = "7edf9206960247dfad403efa90a3c88f"
bus_api_key = "hyTi6EDZxyNFxe5nJefGbm4Ts"
api_url = "http://lapi.transitchicago.com/api/1.0/"
endpoints = json.loads('{"arrivals" : "ttarrivals.aspx"}')
mapid = "40630" # Clark & Division

def getTrainTimes():
    now = datetime.now()
    response = requests.get(api_url + endpoints['arrivals'] + "?key=" + train_api_key + "&max=8&mapid=" + mapid + "&outputType=JSON")
    if response.status_code != 200:
        print('error')
    else:        
        trains = response.json()
        trains = trains['ctatt']['eta']
        now = trains[0]['prdt']
        now = datetime.strptime(now, '%Y-%m-%dT%H:%M:%S')
        northbound = []
        southbound = []
        for i in trains:
            arrT = i['arrT']
            dt = datetime.strptime(arrT, '%Y-%m-%dT%H:%M:%S')
            print('traintime', dt)
            timeDiff = dt - now
            time = int(timeDiff.seconds / 60)
            if timeDiff.days < 0 or time==0:
                print("missedthis one")
            elif i['destNm'] == 'Howard' and len(northbound)<3:
                #northbound.append([dt,time])
                northbound.append(time)
            elif i['destNm'] == '95th/Dan Ryan' and len(southbound)<3:
                #southbound.append([dt,time])
                southbound.append(time)
    return formString([["Northbound Trains ", northbound],["Southbound Trains ", southbound]])

def formString(trainTimes):
    response = ""
    first = True
    for i in trainTimes:
        response = response + "The next " + i[0] + "are arriving in "
        for j in i[1]:
            if first:
                response = response + str(j) + " "
                first = False
            else:
                response = response + "and " + str(j) + " "
        first = True
        response = response + "minutes.  "
    return response

print(getTrainTimes())