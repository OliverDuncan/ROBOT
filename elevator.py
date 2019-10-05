from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Elevator:
    def  __init__(self, robot):
       self.robot=robot
    
    def run(self):
        self.robot.forward(50,5.5)
        self.robot.turnleft(25,30)
        self.robot.forward(50,.7)
        self.robot.turnright(75,30)
        self.robot.backward(50,5.5)