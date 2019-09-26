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
        self.robot.forward(250,1925)
        self.robot.turnright(250,70)
        self.robot.forward(300,700)
        self.robot.forward(800,700)
        self.robot.forward(250,400)
        self.robot.attachMotorD(250,360,-1)        