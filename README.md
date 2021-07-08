# RedisService
A small redis service which provide the ability to save content via Rest API

Usage:
    First, you need to define an ip and port for the service
    
* Add message to  [Publis]:
    using POST command to path : curl --location --request POST 'http://127.0.0.1:5000/Publish' \ --header 'Content-Type: application/json' \ --data-raw '{"Content": "PUT YOUR CONTENT HERE"}'
    
* Get last message from:
    using GET coammand to path : curl --location --request GET 'http://127.0.0.1:5000/Messages/Last'
    
* Get messages within provided range :
    curl --location --request GET 'http://127.0.0.1:5000/Messages/ByTimeRange' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "fromRange":"2021-07-08 13:00:02",
        "toRange":"2021-07-08 14:40:02"
    }'
    

Requirements
* Redis server running :
  it's possible to change port and ip using <redisConfig.json>
* See <Requirements.txt> file

How to install:
* use provide <Dockerfile> in order to use it with docker or just run main.py on your local machine.

