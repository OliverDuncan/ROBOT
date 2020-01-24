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
        self.robot.resetMotorA()
        self.robot.DogGearHoldNoReset(0,0,-1)
        self.robot.driveStraight(200,0.2,0)
        self.robot.findLine(20,Color.BLACK,1)
        self.robot.backwardRampUp(20,.25)
        self.robot.turnRightSloppy(50,45)
        self.robot.turnright(10,90)
        self.robot.driveStraight(250,3.5,90)
        # drops red block
        self.robot.DogGearHoldNoReset(15,0.25,-1) 
        self.robot.forward(20,0.2) 
        self.robot.DogGearHoldNoReset(20,0,1)
        self.robot.driveStraight(100,.7,90)
        self.robot.findLine(20,Color.WHITE,2)
        self.robot.findLine(20,Color.BLACK,2)
        self.robot.backward(10,.1)
        self.robot.turnLeftNoReset(10,29)
        self.robot.driveStraight(200,2.14,29)
        self.robot.backwardRampUp(20,.2)
        # Drops tan block
        self.robot.DogGearHoldNoReset(15,0.12,-1)
        self.robot.backwardRampUp(15,0.2)
        self.robot.findLine(-20,Color.WHITE,1)
        self.robot.backwardRampUp(10,.5)
        self.robot.turnright(10,59)
        # does elevator.
        self.robot.driveStraight(200,2,59)
        self.robot.DogGearHoldNoReset(15,.25,-1)
        self.robot.backwardRampUp(20,1.5)
        self.robot.findLine(-20,Color.WHITE,1)
        self.robot.findLine(-20,Color.BLACK,1)
        self.robot.turnLeftNoReset(10,0)
        # alligns onto the wall
        self.robot.backwardRampUp(50,1.8)
        # self.robot.resetGyro()
        self.robot.driveStraight(200,.85,0)
        self.robot.turnright(10,90)
        self.robot.driveStraight(200,4,90)
        self.robot.backwardRampUp(20,3.05)
        self.robot.turnLeftNoReset(15,0)
        self.robot.backwardRampUp(50,1.5)
        self.robot.driveStraight(200,1,0)
        self.robot.findLine(20,Color.WHITE,2)
        self.robot.findLine(20,Color.BLACK,2)
        self.robot.backwardRampUp(15,.5)
        self.robot.turnright(15,-24)
        wait(1000)
        self.robot.driveStraight(200,5,-27)

        
        # # This took forever but I am glad it works.
    
    
        

       
      
        

        # self.robot.turnright(10,10)
        # self.robot.forward(20,0.2)
        # self.robot.DogGearHold(10,0.05 ,-1)
        # self.robot.turnright(10,60)

        # self.robot.forward(100,3)
    