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
        self.robot.reset()
        self.robot.resetGyro()
        self.robot.driveStraight(250,2.4,0)
        self.robot.backward(40,.5)
        wait(100)
        self.robot.backward(70,4)