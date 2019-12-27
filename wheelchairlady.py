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
        # self.robot.turnleft(10,25)
        # self.robot.forward(50,4)
        # self.robot.DogGearA(20,0.3,-1)
        # self.robot.forward(40,0.05)
        # self.robot.DogGearA(20,0.3,1)
        # self.robot.forward(50,2.5)
        # self.robot.turnright(20,30)html/

        self.robot.driveStraight(200,8,0)

        self.robot.forward(50,4)
        self.robot.DogGearA(20,0.3,-1)
        self.robot.forward(40,0.1)
        self.robot.DogGearA(20,0.3,1)
        self.robot.forward(50,0.25)
        self.robot.turnleft(20,45)
        self.robot.forward(50,1)

    