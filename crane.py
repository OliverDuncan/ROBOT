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

        DGS=0.1
        WL=100
        WS=50

        self.robot.reset()
        self.robot.resetGyro()
        self.robot.resetMotorA()
        motorA = self.robot.getMotorA()
    
        
        self.robot.shallowTurn(30,40,22,1)
        self.robot.shallowTurn(40,30,-19,-1)
        self.robot.forward(20,.75)
        self.robot.forward(5,.45)
        # print("wait")
        wait(100)
        self.robot.DogGearA(20, DGS, 1)
        wait(WL)
        self.robot.DogGearA(20, DGS, -1)
        wait(WS)
        self.robot.DogGearA(20, DGS, 1)
        wait(WL)
        self.robot.DogGearA(20, DGS, -1)
        wait(WS)
        self.robot.DogGearA(20, DGS, 1)
        wait(600)
        self.robot.DogGearA(20, DGS, -1)