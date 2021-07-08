# RedisService
A small redis service which provide the ability to save content via Rest API

----

Requirements
* Redis server running :
  it's possible to change port and ip using <redisConfig.json>
* See (Requirements.txt) file

-----------

How to install:
* Install Redis-Server [https://hub.docker.com/_/redis]
  ```ruby 
  docker run -d -p 6379:6379 --name redis-server redis
  ```
* Install redisService
    * before you install redisService Update the following redisConfig.json file to desired redis endpoint 
  ```ruby 
  {
  "localhost": "<redis-server-ip>",
  "port": 6379,
  "db": 0 
  }
  ```
  * Build docker image:
  ```ruby
  docker build -t redis-service .
  ```
  
  * Run the service:
  ```ruby
  docker run -d -p 5000:5000 --name my-redis-service redis-service
  ```

* use provide (Dockerfile) in order to use it with docker or just run main.py on your local machine.
-----------
USAGE Examples
* Add message to  [Publis]:
    using POST command to path : 
    ```ruby 
    curl --location --request POST 'http://127.0.0.1:5000/Publish' 
  \ --header 'Content-Type: application/json' \ --data-raw '{"Content": "PUT YOUR CONTENT HERE"}' 
  ```
    
* Get last message from:
    using GET coammand to path :  
  ```ruby 
  curl --location --request GET 'http://127.0.0.1:5000/Messages/Last' 
  ```
    
* Get messages within provided range :
  ```ruby
    curl --location --request GET 'http://127.0.0.1:5000/Messages/ByTimeRange' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "fromRange":"2021-07-08 13:00:02",
        "toRange":"2021-07-08 14:40:02"
    }'
  ```