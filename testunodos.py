from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Testunodos:
    def  __init__(self, robot):
       self.robot=robot
    def run(self):
        self.robot.reset()
        self.robot.resetMotorA()
        self.robot.resetGyro()
        # push the blue block for crane
        self.robot.forward(50,2.65)
        self.robot.backward(35,.25)
        self.robot.DogGearA(20, .5, -1)
        self.robot.backwardRampUp(50,.7)
        # go back home
        self.robot.turnright(25,70)
        wait(100)
        self.robot.backwardRampUp(100,1)
        self.robot.turnLeftNoReset(20,0)
        self.robot.resetMotorA()