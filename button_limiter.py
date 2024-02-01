# button_limitor.py
#Author: Frank R. Leotta III

#Discription: This ia a funtion that will limit a buttons usage on a webpage. It will only allow the button to be clicked a certain number of times before it is disabled.

#https://www.freecodecamp.org/news/pyscript-python-front-end-framework/ #useful reference guide



#Imports
import pyscript as ps
import sys
import time
import copy

def limiter(Total_time_varible: int, Switch: bool):
    """summery:
    Turns off a varible after a certain amount of time has passed.  This is to limit the amount of times a button can be pressed.  Use this in a while loop with the switch as the condition, with the switch being the condition to break the loop.
    Just make sure each option turns the switch limitor on, which will activate this function.

    Args:
    countdown_varible (int): the total amount of time that will be counted.  I recommend 15 seconds.
    Switch (bool): the switch that will be turned off

    return:
        none
    """
    countdown = copy.deepcopy(Total_time_varible)
    countdown_end = 0
    for i in range(Total_time_varible, countdown_end, -1):
        print(countdown)
        time.sleep(1)
        countdown -= 1
    if countdown == 0:
        Switch = False
    return Switch








print("hello world")
time.sleep(1)
print("goodbye world")

countdown = 5
swich = True
waldo = limiter(countdown, swich)
print(waldo)
print("done")
