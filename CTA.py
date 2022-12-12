import requests
import json
from datetime import datetime

train_api_key = "7edf9206960247dfad403efa90a3c88f"
bus_api_key = "hyTi6EDZxyNFxe5nJefGbm4Ts"
api_url = "http://lapi.transitchicago.com/api/1.0/"
endpoints = json.loads('{"arrivals" : "ttarrivals.aspx"}')
CandD = "40630" # Clark & Division

def getTrainTimes(mapid):
    now = datetime.now()
    response = requests.get(api_url + endpoints['arrivals'] + "?key=" + train_api_key + "&max=8&mapid=" + mapid + "&outputType=JSON")
    if response.status_code != 200:
            print('error')
    else:        
        trains = response.json()
        trains = trains['ctatt']['eta']
        northbound = []
        southbound = []
        for i in trains:
            arrT = i['arrT']
            dt = datetime.strptime(arrT, '%Y-%m-%dT%H:%M:%S')
            #print('traintime', dt)
            timeDiff = dt - now
            time = int(timeDiff.seconds / 60)
            #print(timeDiff)
            if timeDiff.days < 0 or time==0:
                print("missedthis one")
            elif i['destNm'] == 'Howard' and len(northbound)<3:
                #northbound.append([dt,time])
                northbound.append(time)
            elif i['destNm'] == '95th/Dan Ryan' and len(southbound)<3:
                #southbound.append([dt,time])
                southbound.append(time)
    return [["Northbound Trains: ", northbound],["Southbound Trains: ", southbound]]

trainTimes = getTrainTimes(CandD)
for i in trainTimes: print(i)
