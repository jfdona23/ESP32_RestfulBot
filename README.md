# RestfulBot - A robot controlled through an API

## Table of contents
1. [About](#about)
2. [How it works](#how-it-works)
3. [API Usage](#api-usage)
3. [Libraries used in this project](#libraries-used-in-this-project)
4. [Related links](#related-links)

## About
This project came after my [AvoioderBot](https://github.com/jfdona23/AvoiderBot) project as an improvement of it. In this case I will submit instructions like *move forward*, *move backward*, *turn left* or *turn right* through an API.
The hardware is the same used in the [AvoioderBot](https://github.com/jfdona23/AvoiderBot) project.

## How it works
The core idea is based on how several IoT smart devices works: they're constantly calling a remote API asking about what to do. i.e. *turn on*, *change color*, *set speed*, etcetera.
Here I use a local API made with Python, then the robot calls such API in order to retrieve new instructions.

To achieve that, the robot places an API call that will retrieve a JSON object containing an *order*, a *time* value and a *hash*.
The *order* will be evaluated to trigger a proper function during *time* seconds and the *hash* ensures that the robot will execute the instruction only once. New identical orders are absolutely possible, since the hash will be different.

If the API is not reachable the red led will blink. By the other side, if the API is good but the received package is not as expected the blue led will blink.
The onboard led will blink whenever the robot is establishing a WiFi connection.

At last, the ultrasonic sensor is placed to ensure the robot will not collide against any obstacle. Sadly, due the way of work of the HC-SR04 I need to calculate the distance on-demand and I'm only able to do it before or after an order is executed, which means the robot will collide against an obstacle if the orders last enough.
To solve that I'm planning to replace the HC-SR04 sensor with an infrared distance sensor since those are configured using a potenciometer on its PCB rather than software. In that way I can use its HIGH output signal to trigger an interruption at any moment and stop the robot if an obstacle is near.

## API usage
In order to run this API you need to install Flask. To do such thing you can just tun **python3 -m pip install -r requirements.txt** in the *LocalAPI* folder.
Then just run **python3 api.py** and the API will start to listen for calls at port 8080.
To place an order to the robot just submit a POST call to the endpoint **/v1/inbound** and send a JSON load as follows:
```json
{
    "order": "forward",
    "time": 2
}
```
Accepted orders are *forward*, *backward*, *left*, *right*, *stop*. Time is any value in seconds (floating numbers are accepted too). Default is one second if no value is sent.
The robot will execute the order and then stop after *time* seconds.
Also, GET calls to the endpoint **/v1/outbound** will retrieve the current order, time and hash.

## Libraries and submodules used in this project
* **Credentials** is just a Class to create objects which store passwords and personal data. Then I ignore *credentials.py* file in *.gitignore*. The Class content is the following:
```python
class Creds:
    def __init__(self, hostname, user, passwd):
        self.hostname = hostname
        self.user = user
        self.passwd = passwd

# And then I can create any secret as an object:
my_wifi = creds("dummyHost", "mySSID", "mySuperPassword")
my_token = creds("localhost", "myUser", "strongT0K3N")
```
* Some **AvoiderBot** files are imported as a GIT submodule. Remember to initialize such module as follows:
```
$ git submodule init
$ git submodule update
```
* [**Urequests**](https://github.com/micropython/micropython-lib/tree/master/urequests) is a micropython implementation of the well known *requests* library.

## Related links
1. [Building a Basic RestFul API in Python](https://www.codementor.io/@sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq)