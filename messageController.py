import serverProvider
from datetime import datetime
from flask import Flask, json,request

api = Flask(__name__)

@api.route('/Messages/ByTimeRange', methods=['GET'])
def GetByTime():
    try:
        body = request.json
        _fromRange = datetime.strptime(body['fromRange'],'%Y-%m-%d %H:%M:%S')
        _toRange = datetime.strptime(body['toRange'],'%Y-%m-%d %H:%M:%S')
        _messages = serverProvider.GetRangeMessages(_fromRange, _toRange)
    except Exception as ex:
        return json.dumps("Error" + ex)
    return json.dumps(_messages)

@api.route('/Messages/Last', methods=['GET'])
def GetLast():
    _lastMessage = serverProvider.GetLastMessage()
    return json.dumps(_lastMessage)

@api.route('/Publish', methods=['POST'])
def Publish():
    body = request.json
    content = body["Content"]
    _timeStamp = serverProvider.SetItem(content)
    return json.dumps(_timeStamp)
