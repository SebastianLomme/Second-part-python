# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line

import this
from time import sleep
from math import sin
import datetime
import sys
import greet


def wait(sec):
    sleep(sec)
    print("test")
    return


def my_sin(number):
    return sin(number)


def iso_now():
    time = datetime.datetime.today().isoformat("-", "minutes")
    return time


print(iso_now())


def platform():
    platform = sys.platform
    return platform


print(platform())


def supergreeting_wrapper(name):
    return greet.supergreeting(name)


print(supergreeting_wrapper("Sebastian"))
