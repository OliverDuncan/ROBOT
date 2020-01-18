from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class TreesDeath:
    def  __init__(self, robot):
       self.robot=robot
    
    def run(self):
        self.robot.reset()
        self.robot.resetGyro()
        self.robot.attachMotorDHold(10,.25,-1)
        self.robot.driveStraight(200,4,0)
        self.robot.attachMotorD(5,.4,-1)
        wait(500)
        self.robot.resetGyro()
        self.robot.backwardRampUp(50,2.2)
        self.robot.attachMotorD(10,.1,1)
        self.robot.turnRightSloppy(20,1)
        self.robot.backwardRampUp(50,5)