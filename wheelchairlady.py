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
        self.robot.resetGyro()
        self.robot.reset()
        self.robot.DogGearHoldNoReset(0,0,-1)
        self.robot.driveStraight(200,0.2,0)
        self.robot.findLine(20,Color.BLACK,1)
        self.robot.backward(20,.018)
        self.robot.turnright(10,90)
        self.robot.driveStraight(200,3.3,90)
        # drops red block
        self.robot.DogGearHoldNoReset(15,0.25,-1) 
        self.robot.forward(20,0.2) 
        self.robot.DogGearHoldNoReset(20,0,1)
        self.robot.driveStraight(200,.7,90)
        self.robot.findLine(20,Color.WHITE,2)
        self.robot.findLine(20,Color.BLACK,2)
        self.robot.turnLeftNoReset(10,29)
        self.robot.driveStraight(200,2.14,29)
        self.robot.backward(20,.2)
        # Drops tan block
        self.robot.DogGearHoldNoReset(15,0.12,-1)
        self.robot.backward(15,0.2)
        self.robot.findLine(-20,Color.WHITE,1)
        self.robot.backward(10,.4)
        self.robot.turnright(10,59)
        # does elevator.
        self.robot.driveStraight(200,1.8,59)
        self.robot.DogGearHoldNoReset(15,.25,-1)
        self.robot.backward(20,1.5)
        self.robot.findLine(-20,Color.WHITE,1)
        self.robot.findLine(-20,Color.BLACK,1)
        self.robot.turnLeftNoReset(10,0)
        # alligns onto the wall
        self.robot.alignWall(30)
        self.robot.resetGyro()
        self.robot.driveStraight(200,.85,0)
        self.robot.turnright(10,90)
        self.robot.driveStraight(200,1,90)
        self.robot.dontFindTheColor(25,1)
        self.robot.backward(20,.4)
        #self.robot.resetGyro()
        self.robot.turnright(10,120)
        self.robot.forward(20,0.5)
        self.robot.backward(50,.5) 
        # self.robot.turnLeftNoReset(10,90)   
        # self.robot.backward(50,1)
        # This took forever but I am glad it works.
    
    
        

       
      
        

        # self.robot.turnright(10,10)
        # self.robot.forward(20,0.2)
        # self.robot.DogGearHold(10,0.05 ,-1)
        # self.robot.turnright(10,60)

        # self.robot.forward(100,3)
    