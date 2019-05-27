# coding=utf-8
import csv
from tools import tprint
from flattern import flattern
from fields import fieldPlayerAttack, fieldPlayerTakeDamage, fieldWheelDestroy


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


def saveCSV(filename, aList, mode, varableOfField):
    # 计算表头
    realFieldnames = getHeadList(aList)
    supportedFields = eval(varableOfField)
    # 如果发现了新的field， 打印出来。 下次咱们可以把打印出来的内容， 添加到fields.py中。
    unknownFields = list(set(realFieldnames) - set(supportedFields))
    if unknownFields:
        unknownFields.sort()
        print('{} += \\'.format(varableOfField))
        print(unknownFields)

    with open(filename, mode) as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=supportedFields)
        if (mode == 'w'):
            writer.writeheader()
        for item in aList:
            writer.writerow(item)


# 由于太多的telemetries会带来内存问题， 后面建议一次只存一场比赛的telemetries.
# mode 有两种， 'a'表示追加。 不写表头。 'w'表示重写。 包括表头。
def saveTelemetries(playerName, telemetries, mode):
    def _(log):
        return list(map(flattern, log))

    [logPlayerAttackTs, logPlayerTakeDamageTs,
     logWheelDestroyTs] = splitTelemetries(telemetries)
    saveCSV(playerName + '_playerAttack.csv', _(logPlayerAttackTs), mode,
            'fieldPlayerAttack')
    saveCSV(playerName + 'playerTakeDamage.csv', _(logPlayerTakeDamageTs),
            mode, 'fieldPlayerTakeDamage')
    saveCSV(playerName + 'wheelDestroy.csv', _(logWheelDestroyTs), mode,
            'fieldWheelDestroy')
