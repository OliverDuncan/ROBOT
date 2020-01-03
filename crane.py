
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
        self.robot.resetMotor()
        self.robot.resetGyro()
        motorA = self.robot.getMotorA()

        

        # self.robot.shallowTurn(30,40,20,1)
        # self.robot.shallowTurn(40,30,-20,-1)
        # self.robot.forward(25,1.10)
        # wait(1000)
        # # self.motorBySeconds(self.motorA, )
        # motorA.stop(Stop.HOLD)
        self.robot.DogGearA(50, 0.5, 1)
        wait(500)
        self.robot.DogGearA(50, 0.5, -1)
        wait(1000)
        motorA.run_time(1440,2000,Stop.HOLD)
        # motorA.stop(Stop.COAST)
        # self.robot.backward(50,1)
        self.robot.forwardMark2TheBetterOne(-50,1,20)
        self.robot.turnright(20,90)
        # self.robot.backward(50,3)
        self.robot.forwardMark2TheBetterOne(-50,3,20)
        self.robot.turnleft(20,90)