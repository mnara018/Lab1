import time
import random
from Lights import *
from Displays import *
from MyLights import *
from MyButtons import *
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

myDisplay = LCDDisplay(sda=0, scl=1, i2cid=0)
myDisplay.showText("Welcome! let's play a game")
myDisplay.reset()


L = MyLights()
L.blinking

b = MyButtons()
b. buttonPressed

