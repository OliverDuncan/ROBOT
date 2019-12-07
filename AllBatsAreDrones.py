from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class AllBatsAreDrones:
    def  __init__(self, robot):
       self.robot=robot

    def run(self):
        # Hello there I will be your guide to this program, my name is phil
        # This gets access to motorD from the robot class
        motor= self.robot.getMotorD()
        # This holds the attachment motor in place
        motor.stop(Stop.HOLD)
        # This is just the driving to the desired location
        self.robot.forwardMark2TheBetterOne(50,2,20)
        self.robot.turnright(20,90)
        self.robot.forwardMark2TheBetterOne(50,1.5,20)
        self.robot.turnright(20,90)
        # Thank you for coming on this wonderful tourventure
       
