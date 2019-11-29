from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class AllBatsAreDrones:
    def  __init__(self, robot):
       self.robot=robot

    def run(self):
        self.motorD.stop(stop_coast=Stop.HOLD)
        self.forward(50,2)
        self.turnright(50,88)
        self.forward(50,1.5)
        self.turnright(50,88)
       
