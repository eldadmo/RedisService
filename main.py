import json
import os

import messageController
import serverProvider
from serverConfig import ServerConfig


def ReadServerConfig():
    try:
        cwd = os.getcwd()
        environment_path = cwd
        with open(environment_path + "/serverConfig.json") as jsonFile:
            json_object = json.load(jsonFile)
            server_config_object = ServerConfig(**json_object)
            jsonFile.close()
        return server_config_object
    except Exception as ex:
        print("Warning: Cannot parse serverConfig.json from path:" + str(
            environment_path) + "/serverConfig.json\r\n" + "Exception:" + str(ex))
        return None


if __name__ == '__main__':
    serverProvider.Init()
    serverConfig = ReadServerConfig()
    if serverConfig is None:
        messageController.api.run()
    else:
        messageController.api.run(serverConfig.localhost, serverConfig.port)
