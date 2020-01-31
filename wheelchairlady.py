from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class wheelchairlady:
    def  __init__(self, robot):
       self.robot=robot
    def run(self):
        self.robot.resetGyro()
        self.robot.resetAllMotors()
        self.robot.DogGearHoldNoReset(0,0,-1)
        self.robot.driveStraight(200,0.2,0)
        self.robot.dsf(100,Color.BLACK,1,0)
        self.robot.backwardRampUp(20,.25)
        self.robot.turnRightSloppy(50,45)
        self.robot.turnright(10,90)
        self.robot.driveStraight(250,3.5,90)
        # drops red block
        self.robot.DogGearHoldNoReset(15,0.25,-1) 
        self.robot.forward(20,0.2) 
        self.robot.DogGearHoldNoReset(15,0,1)
        gyro = self.robot.readGyro()
        if gyro < 90: 
            self.robot.turnright(5,90)
        elif gyro > 90:
            self.robot.turnLeftNoReset(5,90)
        self.robot.driveStraight(100,.7,90)
        self.robot.dsf(100,Color.WHITE,2,90)
        self.robot.dsf(100,Color.BLACK,2,90)
        self.robot.backward(10,.1)
        self.robot.turnLeftNoReset(10,26)
        self.robot.driveStraight(200,2.2,26)
        self.robot.backward(20,.2)
        # Drops tan block
        self.robot.DogGearHoldNoReset(15,0.12,-1)
        self.robot.backward(15,0.2)
        self.robot.dsf(-100,Color.WHITE,1,26)
        self.robot.backwardRampUp(10,.3)
        self.robot.turnright(10,60)
        # does elevator.
        self.robot.driveStraight(200,2,60)
        self.robot.DogGearHoldNoReset(15,.25,-1)
        gyro = self.robot.readGyro()
        if gyro < 60: 
            self.robot.turnright(5,60)
        elif gyro > 60:
            self.robot.turnLeftNoReset(5,60)
        self.robot.backward(25,1.4)
        self.robot.dsf(-100,Color.WHITE,1,60)
        self.robot.dsf(-100,Color.BLACK,1,60)
        self.robot.backwardRampUp(50,.2)
        self.robot.turnLeftNoReset(10,0)
        # alligns onto the wall
        self.robot.backwardRampUp(50,1.8)
        self.robot.driveStraight(200,.85,0)
        self.robot.turnRightSloppy(30,75)
        self.robot.turnright(10,90)
        self.robot.driveStraight(200,3,90)
        # drop swing
        self.robot.backwardRampUp(40,2.8)
        self.robot.turnLeftSloppy(30,-15)
        self.robot.turnLeftNoReset(15,0)
        # align back on the wall
        self.robot.backwardRampUp(50,1.5)
        self.robot.driveStraight(200,1,0)
        self.robot.dsf(100,Color.WHITE,2,0)
        self.robot.dsf(100,Color.BLACK,2,0)
        self.robot.backwardRampUp(15,.5)
        self.robot.turnright(15,-30)
        wait(100)
        self.robot.driveStraight(100,.5,-30)
        self.robot.dsf(100,Color.BLACK,1,-30)
        # drive up the bridge
        self.robot.driveStraight(200,2.9,-30)  
        # # This took forever but I am glad it works.
    
    
        

       
      
        

        