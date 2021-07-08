import json
import MessageController
import ServerProvider

if __name__ == '__main__':
    ServerProvider.Init()
    MessageController.api.run()
