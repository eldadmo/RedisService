import datetime
from datetime import datetime
from RedisConfig import RedisConfig
import redis
import json
import os

redisService = None
def Init():
    RedisConfig_object = ReadConfig()
    global redisService
    if RedisConfig_object is None:
        redisService = redis.Redis(host='localhost', port=6379, db=0, password=None, socket_timeout=None)
    else:
        redisService = redis.Redis(host=RedisConfig_object.localhost, port=RedisConfig_object.port, db=RedisConfig_object.db, password=None, socket_timeout=None)

def ReadConfig():
    try:
        cwd = os.getcwd()
        EnviromentPath = cwd + "/venv"
        with open(EnviromentPath + "/Redis.Config.json") as jsonFile:
            jsonObject = json.load(jsonFile)
            RedisConfig_object = RedisConfig(**jsonObject)
            jsonFile.close()
        return RedisConfig_object
    except Exception as ex:
        print("Warning: Cannot parse Redis.Config.json from path:"+ str(EnviromentPath) + "/Redis.Config.json\r\n" + "Execption: " + str(ex))
        return None

def SetItem(message):
    # r.hset('price', 'time', 'value')
    _timeStamp = int(datetime.timestamp(datetime.now()))
    redisService.hset("Message_Batch",_timeStamp,message)
    return _timeStamp

def GetRangeMessages(fromRange, toRange):
    keys = redisService.hkeys("Message_Batch")
    print(keys)
    messages = []
    for keyTimeStamp in keys:
        currentItemTime = datetime.fromtimestamp(int(keyTimeStamp))
        if fromRange <= currentItemTime <= toRange:
            message = redisService.hget("Message_Batch",keyTimeStamp)
            if message:
                redisService.hdel("Message_Batch",keyTimeStamp)
                messages.append(message.decode("utf-8"))
    return messages


def GetLastMessage():
    timeStampsKeys = redisService.hkeys("Message_Batch")
    maxKeyValue = 0
    for timeStampsKey in timeStampsKeys:
        if maxKeyValue < int(timeStampsKey):
            maxKeyValue = int(timeStampsKey)
    if maxKeyValue != 0:
        message = redisService.hget("Message_Batch", maxKeyValue)
        if message:
            redisService.hdel("Message_Batch", maxKeyValue)
            return message.decode("utf-8")
    return None
