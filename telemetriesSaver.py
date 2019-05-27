import csv
from tools import tprint
from flattern import flattern

def splitTelemetries(telemetries):
    logPlayerAttackTs = []
    logPlayerTakeDamageTs = []
    logWheelDestroyTs = []
    for telemetry in telemetries:
        for tObj in telemetry:
            if tObj['_T'] == 'LogPlayerAttack':
                logPlayerAttackTs.append(tObj)
            if tObj['_T'] == 'LogPlayerTakeDamage':
                logPlayerTakeDamageTs.append(tObj)
            if tObj['_T'] == 'LogWheelDestroy':
                logWheelDestroyTs.append(tObj)
    return [logPlayerAttackTs, logPlayerTakeDamageTs, logWheelDestroyTs]

def getHeadList(listOfDict):
    head = set()
    for item in listOfDict:
        for k in item:
            head.add(k)
    head = list(head)
    head.sort()
    return head

def saveCSV(filename, aList):
    with open(filename, 'w') as csvfile:
        fieldnames = getHeadList(aList)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in aList:
            writer.writerow(item)




def saveTelemetries(playerName, telemetries):
    def _(log):
        return map(flattern, log)
    [logPlayerAttackTs, logPlayerTakeDamageTs, logWheelDestroyTs] = splitTelemetries(telemetries)
    saveCSV(playerName+'_playerAttack.csv', _(logPlayerAttackTs))
    saveCSV(playerName + 'playerTakeDamage.csv', _(logPlayerTakeDamageTs))
    saveCSV(playerName + 'wheelDestroy.csv', _(logWheelDestroyTs))
