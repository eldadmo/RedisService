import datetime
from datetime import datetime
from redisConfig import RedisConfig
import redis
import json
import os

redisService = None


def Init():
    redis_config_object = ReadConfig()
    global redisService
    if redis_config_object is None:
        redisService = redis.Redis(host='localhost', port=6379, db=0, password=None, socket_timeout=None)
    else:
        redisService = redis.Redis(host=redis_config_object.localhost, port=redis_config_object.port,
                                   db=redis_config_object.db, password=None, socket_timeout=None)


def ReadConfig():
    try:
        cwd = os.getcwd()
        environment_path = cwd
        with open(environment_path + "/redisConfig.json") as jsonFile:
            json_object = json.load(jsonFile)
            redis_config_object = RedisConfig(**json_object)
            jsonFile.close()
        return redis_config_object
    except Exception as ex:
        print("Warning: Cannot parse redisConfig.json from path:" + str(
            environment_path) + "/redisConfig.json\r\n" + "Exception:" + str(ex))
        return None


def SetItem(message):
    _timeStamp = int(datetime.timestamp(datetime.now()))
    redisService.hset("Message_Batch", _timeStamp, message)
    return _timeStamp


def GetRangeMessages(fromRange, toRange):
    keys = redisService.hkeys("Message_Batch")
    print(keys)
    messages = []
    for keyTimeStamp in keys:
        current_item_time = datetime.fromtimestamp(int(keyTimeStamp))
        if fromRange <= current_item_time <= toRange:
            message = redisService.hget("Message_Batch", keyTimeStamp)
            if message:
                redisService.hdel("Message_Batch", keyTimeStamp)
                messages.append(message.decode("utf-8"))
    return messages


def GetLastMessage():
    time_stamps_keys = redisService.hkeys("Message_Batch")
    max_key_value = 0
    for timeStampsKey in time_stamps_keys:
        if max_key_value < int(timeStampsKey):
            max_key_value = int(timeStampsKey)
    if max_key_value != 0:
        message = redisService.hget("Message_Batch", max_key_value)
        if message:
            redisService.hdel("Message_Batch", max_key_value)
            return message.decode("utf-8")
    return None
