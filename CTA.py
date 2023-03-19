import requests
import json
from datetime import datetime

train_api_key = "7edf9206960247dfad403efa90a3c88f"
bus_api_key = "hyTi6EDZxyNFxe5nJefGbm4Ts"
bus_api_url = "http://www.ctabustracker.com/bustime/api/v2/getpredictions"
train_api_url = "http://lapi.transitchicago.com/api/1.0/"
endpoints = json.loads('{"arrivals" : "ttarrivals.aspx"}')
stpid_lasalle_north = "1445"
stpid_lasalle_south = "14763"
stpid_clark_north = "1898"
stpid_clark_south = "1852"
mapid = "40630" # Clark & Division

def getTrainTimes():
    now = datetime.now()
    response = requests.get(train_api_url + endpoints['arrivals'] + "?key=" + train_api_key + "&max=8&mapid=" + mapid + "&outputType=JSON")
    if response.status_code != 200:
        print('error')
        return "No upcoming Red Line trains"
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
    return formString([["Northbound Red Line Trains ", northbound],["Southbound Red Line Trains ", southbound]])

def getBusTimes():
    try:
        lasalle_north_response = requests.get(bus_api_url + "?key=" + bus_api_key + "&rt=156&stpid=" + stpid_lasalle_north + "&format=json").json()['bustime-response']['prd']
    except:
        lasalle_northbound = []
        print("API error")
    else:
        now = lasalle_north_response[0]['tmstmp']
        now = datetime.strptime(now,'%Y%m%d %H:%M')
        lasalle_northbound = []
        for i in lasalle_north_response:
            dt = datetime.strptime(i['prdtm'],'%Y%m%d %H:%M')
            print('traintime', dt)
            timeDiff = dt - now
            time = int(timeDiff.seconds / 60)
            if timeDiff.days < 0 or time==0:
                print("missedthis one")
            else:
                lasalle_northbound.append(time)

    
    try:
        lasalle_south_response = requests.get(bus_api_url + "?key=" + bus_api_key + "&rt=156&stpid=" + stpid_lasalle_south + "&format=json").json()['bustime-response']['prd']
    except:
        lasalle_southbound = []
        print("API error")
    else:
        now = lasalle_south_response[0]['tmstmp']
        now = datetime.strptime(now,'%Y%m%d %H:%M')
        lasalle_southbound = []
        for i in lasalle_south_response:
            dt = datetime.strptime(i['prdtm'],'%Y%m%d %H:%M')
            print('traintime', dt)
            timeDiff = dt - now
            time = int(timeDiff.seconds / 60)
            if timeDiff.days < 0 or time==0:
                print("missedthis one")
            else:
                lasalle_southbound.append(time)

    try:
        clark_north_response = requests.get(bus_api_url + "?key=" + bus_api_key + "&rt=22&stpid=" + stpid_clark_north + "&format=json").json()['bustime-response']['prd']
    except:
        clark_northbound = []
        print("API error")
    else:
        now = clark_north_response[0]['tmstmp']
        now = datetime.strptime(now,'%Y%m%d %H:%M')
        clark_northbound = []
        for i in clark_north_response:
            dt = datetime.strptime(i['prdtm'],'%Y%m%d %H:%M')
            print('traintime', dt)
            timeDiff = dt - now
            time = int(timeDiff.seconds / 60)
            if timeDiff.days < 0 or time==0:
                print("missedthis one")
            else:
                clark_northbound.append(time)

    try:
        clark_south_response = requests.get(bus_api_url + "?key=" + bus_api_key + "&rt=22&stpid=" + stpid_clark_south + "&format=json").json()['bustime-response']['prd']
    except:
        clark_southbound = []
        print("API error")
    else:
        now = clark_south_response[0]['tmstmp']
        now = datetime.strptime(now,'%Y%m%d %H:%M')
        clark_southbound = []
        for i in clark_south_response:
            dt = datetime.strptime(i['prdtm'],'%Y%m%d %H:%M')
            print('traintime', dt)
            timeDiff = dt - now
            time = int(timeDiff.seconds / 60)
            if timeDiff.days < 0 or time==0:
                print("missedthis one")
            else:
                clark_southbound.append(time)
    
    buses = [["Northbound 156 Buses ", lasalle_northbound],["Southbound 156 Buses ", lasalle_southbound],["Northbound 22 Buses ", clark_northbound],["Southbound 22 Buses ", clark_southbound]]
    return formString(buses)

def formString(trainTimes):
    print(trainTimes)
    response = ""
    first = True
    for i in trainTimes:
        if not i[1]:
            response = response + "There are no upocoming " + i[0] + ".  "
        else:
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
#print(requests.get("http://www.ctabustracker.com/bustime/api/v2/getdirections?key=" + bus_api_key + "&rt=22&format=json").json())
#print(requests.get("http://www.ctabustracker.com/bustime/api/v2/getstops?key=" + bus_api_key + "&rt=22&dir=Northbound&format=json").json())
#print(requests.get("http://www.ctabustracker.com/bustime/api/v2/getpredictions?key=" + bus_api_key + "&stpid=" + stpid_clark_north + "&format=json").json())
print(getBusTimes())