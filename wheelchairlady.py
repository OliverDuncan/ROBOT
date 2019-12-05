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
        self.robot.DogGearA(20,0.25,1)
        self.robot.forward(50,3)
        self.robot.backward(50,.5)
        self.robot.DogGearA(20,0.25,-1)
        self.robot.forward(50,2)
        self.robot.attachMotorD(50,0.25,1)
        self.robot.backward(60,5)
    