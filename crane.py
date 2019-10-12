
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Crane:
    def  __init__(self, robot):
       self.robot=robot

    def run(self):
        self.robot.attachMotorD(50,.75,1)
        self.robot.shallowTurn(30,40,20,1)
        self.robot.shallowTurn(40,30,-20,-1)
        self.robot.forward(35,.92)
        self.robot.attachMotorD(50,.75,-1)
        self.robot.DogGearA(25,.5,1)