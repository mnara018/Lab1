import time
import random
from Displays import *
from Button import *
from Buzzer import *


class Mybuttons:
    
    def __init__(self):
        self._br =Button (18, "red" , buttonhandler=self)
         self._bg =Button (19, "green" , buttonhandler=self)
        self._by =Button (20, "yellow" , buttonhandler=self)
         self._bb =Button (21, "blue" , buttonhandler=self)
        self._display =LCDDisplay(sda = 0, scl =1, i2cid=0)
        self._buzzer =PassiveBuzzer(15)
        self.Display()

    def buttonPressed (self,name): """Handles the pressed button, describes the color, produces a sound"""
        if name == "red": 
            self.display.showText("red")
            self._buzzer.beep()
            time.sleep(0.5)
        elif name == "green":
            self.display.showText("green")
            self._buzzer.beep()
            time.sleep(0.5)
        elif name == "yellow":
            self.display.showText("yellow")
            self._buzzer.beep()
            time.sleep(0.5)
        elif name == "blue":
            self.display.showText("blue")
            self._buzzer.beep()
            time.sleep(0.5)
        else:
            self.reset()
            self.display()

    def run (self): """Keep the game active"""

        while True:
            time.sleep(0.5)

     def buttonReleased (self,name):  """buttons liberation"""
