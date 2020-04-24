# RestfulBot - A robot controlled through an API

## Table of contents
1. [About](#about)
2. [How it works](#how-it-works)
3. [Libraries used in this project](#libraries-used-in-this-project)
4. [Related links](#related-links)

## About
This project came after my [AvoioderBot](https://github.com/jfdona23/AvoiderBot) project as an improvement of it. In this case I will submit instructions like *move forward*, *move backward*, *turn left* or *turn right* through an API.
The hardware is the same used in the [AvoioderBot](https://github.com/jfdona23/AvoiderBot) project.

## How it works
The core idea is based on how several IoT smart devices works: they're constantly calling a remote API asking about what to do. i.e. *turn on*, *change color*, *set speed*, etcetera.
Here I use a local API made with Python, then the robot calls such API in order to retrieve new instructions. To achieve that, there is an endpoint and when the robot places a call it will retrieve a JSON object containing an *instruction* and a *hash*.
The instruction will be evaluated to trigger a proper function, and the hash ensures the robot execute the instruction only once.

## Libraries used in this project
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

## Related links
1. [Building a Basic RestFul API in Python](https://www.codementor.io/@sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq)