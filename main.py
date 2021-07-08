import messageController
import serverProvider

if __name__ == '__main__':
    serverProvider.Init()
    messageController.api.run()
