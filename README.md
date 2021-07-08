# RedisService
A small redis service which provide the ability to save content via Rest API

Usage:
    First, you need to define an ip and port for the service
    * Add message to pool:
    using post command to path : curl --location --request POST 'http://127.0.0.1:5000/Publish' \ --header 'Content-Type: application/json' \ --data-raw '{"Content": "PUT YOUR CONTENT HERE"}'

    * Get last message from:

Requirements
    * See <Requirements.txt> file