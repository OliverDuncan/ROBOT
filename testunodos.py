from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Testunodos:
    def  __init__(self, robot):
       self.robot=robot
    def run(self):
        self.robot.resetGyro()
        self.robot.driveStraightTest(100,4,0)
        