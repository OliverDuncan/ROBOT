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
        self.robot.forward(50,4.8)
        self.robot.turnleft(.5,150)
        self.robot.forward(60,2)
        self.robot.forward(100,2.5)
        self.robot.forward(50,1)
        self.robot.attachMotorD(50,.8,-1)