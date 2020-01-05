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
        self.robot.reset()
        self.robot.resetGyro()
        motorA = self.robot.getMotorA()

        
        self.robot.forward(30, .5)
        self.robot.turnright(10,45)
        self.robot.forward(30, .5)
        self.robot.resetGyro()
        self.robot.turnleft(10,35)
        self.robot.forward(30,1.5)
        # self.robot.shallowTurn(30,40,20,1)
        # self.robot.shallowTurn(40,30,-20,-1)
        # self.robot.forward(25,1.10)
        # wait(1000)
        # self.robot.DogGearA(20, 0.18, 1)
        # wait(250)
        # self.robot.DogGearA(20, 0.18, -1)
        # wait(1000)
        # self.robot.DogGearA(20, 0.18, 1)
        # wait(250)
        # self.robot.DogGearA(20, 0.18, -1)
        # self.robot.backward(50,1)
        # self.robot.turnright(20,90)
        # self.robot.backward(50,2.5)
        # self.robot.turnLeftSloppy(20,45)