from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class CrossyRoad:
    def  __init__(self, robot):
       self.robot=robot
    def run(self):
        self.robot.resetGyro()
        print(self.robot.readGyro)
        wait(50)
        self.robot.driveStraight(300,4.5,0)
        self.robot.alignWall(100)
        self.robot.resetGyro()
        self.robot.turnleft(20,90)