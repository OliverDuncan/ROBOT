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

        # self.robot.driveStraight(200,8,0)

        self.robot.resetGyro()
        self.robot.reset()
        self.robot.DogGearHold(0,0,-1)
        self.robot.driveStraight(200,0.6,0)
        self.robot.turnright(10,87)
        self.robot.driveStraight(200,3.6,90)

        # self.robot.DogGearHold(0,0,-1)
        # self.robot.forward(50,4)
        self.robot.DogGearA(15,0.25,-1)
        self.robot.forward(20,0.2)
        self.robot.DogGearA(20,0.3,1)
        self.robot.forward(20,0.7)
        gyro= self.robot.readGyro()
        self.robot.resetGyro()
        self.robot.turnleft(7,47+(gyro -90))
        self.robot.resetGyro()
        self.robot.driveStraight(200,2,0) # go a little bit further
        self.robot.DogGearA(20,0.2,-1)
        self.robot.backward(50,0.3)
        self.robot.turnright(20,15)
    
      
        

        # self.robot.turnright(10,10)
        # self.robot.forward(20,0.2)
        # self.robot.DogGearHold(10,0.05 ,-1)
        # self.robot.turnright(10,60)

        # self.robot.forward(100,3)
    