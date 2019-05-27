import json
urlPattern = "https://api.pubg.com/shards/%s/matches/%s"

def findTelemetryURL(region, matchId, http):
    url = urlPattern %(region, matchId)
    headers = {"Accept": "application/vnd.api+json"}
    r = http.request('GET', url, headers = headers)
    response = r.data.decode()
    data = json.loads(response)
    assetsId = data['data']['relationships']['assets']['data'][0]['id']
    included = data['included']
    telemetryItem = None
    for item in included:
        if item['id'] == assetsId:
            telemetryItem = item
            break

    telemetryURL = telemetryItem['attributes']['URL']
    return telemetryURL

def findTelemetryByURL(url, http):
    r = http.request('GET', url, headers={"Accept": "application/vnd.api+json"})
    return [x for x in json.loads(r.data.decode()) \
        if x['_T'] == 'LogPlayerAttack' \
            or  x['_T'] == 'LogPlayerTakeDamage'\
                 or x['_T'] == 'LogWheelDestroy']


def findTelemetry(region, matchId, http):
    telemetryURL = findTelemetryURL(region, matchId, http)
    return findTelemetryByURL(telemetryURL, http)




# {
#     "type": "asset",
#     "id": "aca364cc-6758-11e9-a2eb-0a586462471d",
#     "attributes": {
#         "name":
#         "telemetry",
#         "description":
#         "",
#         "createdAt":
#         "2019-04-25T12:50:16Z",
#         "URL":
#         "https://telemetry-cdn.playbattlegrounds.com/bluehole-pubg/pc-as/2019/04/25/12/50/aca364cc-6758-11e9-a2eb-0a586462471d-telemetry.json"
#     }
# }
