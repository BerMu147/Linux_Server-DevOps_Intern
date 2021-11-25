import time

import redis
from flask import Flask

app = Flask(_name_)
cache = redis.Redis(host='redis', port 5000)

@apt.route('/')
def hello():
    return 'Hello World!\n'
