from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Deathish:
    def  __init__(self, robot):
       self.robot=robot
    
    def run(self):
        self.robot.reset()
        self.robot.resetGyro()
        self.robot.attachMotorDHold(0,0,-1)
        # wait(1000)
        self.robot.driveStraight(200,4.8,0)
        self.robot.attachMotorD(5,.1,-1)
        wait(1000)
        self.robot.resetGyro()
        self.robot.backwardRampUp(50,.3)
        self.robot.turnright(10,20)
        self.robot.backward(25,.5)
        self.robot.resetMotorA()
        self.robot.DogGearA(50,.25,-1)
        self.robot.resetGyro
        self.robot.turnright(10,45)
        self.robot.backward(100,5)

        self.robot.reset()
        self.robot.resetMotorD()
        self.robot.resetMotorA()
        # self.robot.backwardRampUp(50,1.5)
        # self.robot.turnRightSloppy(10,35)
        # self.robot.backward(100,2.5)
        # self.robot.attachMotorD(20,.5,1)