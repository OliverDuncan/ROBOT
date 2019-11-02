from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class WheelchairLady:
    def  __init__(self, robot):
       self.robot=robot
    def run(self):
        self.robot.forward(50,6)
        self.robot.turnright(20,20)
        self.robot.forward(50,2)
        self.robot.backward(50,1)
        self.robot.turnleft(20,20)
        self.robot.backward(60,5)
    