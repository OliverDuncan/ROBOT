from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Bridge:
    def  __init__(self, robot):
       self.robot=robot
    
    def run(self):
        self.robot.forward(250,2160)
        self.robot.turnright(250,80)
        self.robot.forward(250,720)
        self.robot.attachMotorD(250,1,1)        