
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Robot:
    def __init__(self,motorA,motorB,motorC,motorD,sensor1,sensor2,sensor3,sensor4):
        self.motorA = motorA
        self.motorB=motorB
        self.motorC=motorC
        self.motorD=motorD
        self.colorSensorright=sensor1
        self.colorSensorleft=sensor2
        self.gyroSensor=sensor3
        self.touchSensor=sensor4

    def reset(self):
        self.motorA.reset_angle(0)
        self.motorB.reset_angle(0)
        self.motorC.reset_angle(0)
        self.motorD.reset_angle(0)
        self.gyroSensor.reset_angle(0)

    def forward(self,speed,distance):
        self.reset()
        print("test")
        self.motorB.run(speed)
        self.motorC.run(speed)
        while self.motorC.angle() < distance:
            wait(10)
        self.motorB.run(0)
        self.motorC.run(0)

    def backward(self,speed,distance):
        self.reset()
        self.motorB.run(speed*-1)
        self.motorC.run(speed*-1)
        while self.motorC.angle() > -distance:
            print(self.motorC.angle())
            print("\n")
            wait(10)
        self.motorB.run(0)
        self.motorC.run(0)

    def turnleft(self,speed,angle):
        self.reset()
        self.motorB.run(speed*-1)
        self.motorC.run(speed)
        print("turn")
        while self.gyroSensor.angle() < angle:
            wait(5)
            print(self.gyroSensor.angle())
        self.motorB.run(0)
        self.motorC.run(0)

    def turnright(self,speed,angle):
        self.reset()
        self.motorB.run(speed)
        self.motorC.run(speed*-1)
        print("turn")
        while self.gyroSensor.angle() > angle*-1:
            wait(5)
            print(self.gyroSensor.angle())
        self.motorB.run(0)
        self.motorC.run(0)
    
    def DogGearA(self,speed,distance,direction):
        self.reset()
        if direction == 1:
            self.motorA.run(speed)
            print("clDogRotate")
            while self.motorA.angle() > distance:
                wait(5)
                print(self.motorA.angle())
            self.motorA.run(0)

        elif direction == -1:
            self.motorA.run(speed*direction)
            print("cnclDogRotate")
            while self.motorA.angle() < distance:
                wait(5)
                print(self.motorA.angle())
            self.motorA.run(0)