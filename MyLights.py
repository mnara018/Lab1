import time
import random
from Lights import *
from Displays import *
from Buzzer import *

"""This class can randomly blink the lights """
class MyLight:
    def __init__(self):
        self._rl = Light(13,"red") """ connects the red light to pin GP13, assigns a name"""
        self._gl = Light(12,"green") """ connects the green light to pin GP12, assigns a name"""
        self._yl = Light(11,"yellow") """ connects the yellow light to pin GP11, assigns a name"""
        self._bl = Light(10,"blue") """ connects the blue light to pin GP10, assigns a name"""
        self._buzzer =PassiveBuzzer(16) """ connects the buzzer to the gp16"""
        self.Display()
        self.Lights()
        self._num = 0 "storage a number"
        self._alllights = [] """create an empty list of lights"""
    
    def incrementNumber (self): """ add one to inicial number"""
        self._num = self._num +1
    
    def blinking (self): """Blink all lights"""
        self._alllights.blink(0.5,1)
    
    def randomSQ (self): """ creates a random sequence of ligths """
        self._sq = random.choice(self._alllights)
        return self._sq
    
    
    def lightDescription (self,name): """describes the color and produce a sound when the light is on"""
        if self._rl.on(): 
            self.display.showText("red")
            self._buzzer.beep()
           
        elif self._gl.on():
            self.display.showText("green")
            self._buzzer.beep()
       
        elif self._yl.on()":
            self.display.showText("yellow")
            self._buzzer.beep()
        
        elif self._bl.on()":
            self.display.showText("yellow")
            self._buzzer.beep()
        else:
            pass

