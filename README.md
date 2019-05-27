-运行抓取代码-
python3 dataFetcher.py

-运行设置-
config: config.py

-字段设置方法-
运行程序之后，如果程序发现了新字段， 会打印出来这样的内容：
fieldWheelDestroy += \
['_D', '_T', 'attackId', 'attacker.accountId', 'attacker.health', 'attacker.isInBlueZone', 'attacker.isInRedZone', 'attacker.location.x', 'attacker.location.y', 'attacker.location.z', 'attacker.name', 'attacker.ranking', 'attacker.teamId', 'attacker.zone', 'common.isGame', 'damageCauserName', 'damageTypeCategory', 'vehicle.feulPercent', 'vehicle.healthPercent', 'vehicle.vehicleId', 'vehicle.vehicleType']

只需要把这些内容粘贴到 fields.py文件尾部就行了。
更新fields.py文件后， 再次运行抓取代码。