from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Parkish:
    def  __init__(self, robot):
       self.robot=robot
    
    def run(self):
        self.robot.forward(40,2.4)
        self.robot.backward(40,.5)
        self.robot.turnright(25,30)
        self.robot.backward(100,3)