from telemetry_finder import findTelemetry
from telemetriesSaver import saveTelemetries
import json
from config import http, url, headers, playerNames, ZONE, MATCH_LIMIT
from tools import tprint

def getPlayerIdByName(name):
    tprint('getting player id for '+name)
    fields = {"filter[playerNames]": name}
    # connect!
    r = http.request('GET', url, headers=headers, fields = fields)
    # here is what we got
    response = r.data.decode()

    # show json data
    import json
    data = json.loads(response)

    # get player from data
    playerId = data['data'][0]['id']
    return playerId

def getPlayerById(id):
    tprint('getting player by id: '+ id)
    urlPlayer = url+'/'+id
    r = http.request('GET', urlPlayer, headers=headers)
    playerRes = r.data.decode()

    return json.loads(playerRes)

def getMatchesOfPlayer(player):
    tprint('getting matches of player ')
    return player['data']['relationships']['matches']['data']


def fetchData(playerName):
    matches = getMatchesOfPlayer(getPlayerById(getPlayerIdByName(playerName)))
    matches = matches[:MATCH_LIMIT]

    tprint('Got match ids: ' + str([match['id'] for match in matches]))

    telemetries = []

    print('total'+str(len(matches)))
    i=1

    for match in matches:
        print(i)
        i+=1
        telemetry = findTelemetry(ZONE, match['id'], http)
        tprint('found telemetry for match id:'+match['id'])
        telemetries.append(telemetry)
        tprint('append finished')

    saveTelemetries(playerName, telemetries)

if __name__ == '__main__':
    for name in playerNames:
        fetchData(name)