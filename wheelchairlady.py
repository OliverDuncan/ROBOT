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
        self.robot.backward(20,.2)
        # Drops tan block
        self.robot.DogGearHoldNoReset(15,0.12,-1)
        self.robot.backward(15,0.2)
        self.robot.findLine(-20,Color.WHITE,1)
        self.robot.backwardRampUp(10,.4)
        self.robot.turnright(10,59)
        # does elevator.
        self.robot.driveStraight(200,2,60)
        self.robot.DogGearHoldNoReset(15,.25,-1)
        self.robot.backward(20,1.5)
        self.robot.findLine(-20,Color.WHITE,1)
        self.robot.findLine(-20,Color.BLACK,1)
        self.robot.backwardRampUp(40,.3)
        self.robot.turnLeftNoReset(10,0)
        # alligns onto the wall
        self.robot.backwardRampUp(50,1.8)
        # self.robot.resetGyro()
        self.robot.driveStraight(200,.85,0)
        self.robot.turnright(10,90)
        self.robot.driveStraight(200,2.5,90)
        self.robot.backwardRampUp(20,2.5)
        self.robot.turnLeftNoReset(15,0)
        self.robot.backwardRampUp(50,1.5)
        self.robot.driveStraight(200,1,0)
        self.robot.findLine(20,Color.WHITE,2)
        self.robot.findLine(20,Color.BLACK,2)
        self.robot.backwardRampUp(15,.7)
        self.robot.turnright(15,-27)
        wait(500)
        self.robot.driveStraight(100,2,-27)
        self.robot.findLine(20,Color.BLACK,1)
        self.robot.driveStraight(200,3,-27)

        self.robot.reset()
        self.robot.resetMotorD()
        self.robot.resetMotorA()
        # # This took forever but I am glad it works.
    
    
        

       
      
        

        