
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

    LAR_MOTOR=10
    MED_MOTOR=14.4
    DEG_TO_ROT=360

    def reset(self):
        self.motorA.reset_angle(0)
        self.motorB.reset_angle(0)
        self.motorC.reset_angle(0)
        self.motorD.reset_angle(0)
        self.gyroSensor.reset_angle(0)

    def forward(self,speed,distance):
        self.reset()
        print("test")
        self.motorB.run(speed*self.LAR_MOTOR)
        self.motorC.run(speed*self.LAR_MOTOR)
        while self.motorC.angle() < distance*self.DEG_TO_ROT:
            wait(10)
        self.motorB.run(0)
        self.motorC.run(0)

    def backward(self,speed,distance):
        self.reset()
        self.motorB.run(speed*-1*self.LAR_MOTOR)
        self.motorC.run(speed*-1*self.LAR_MOTOR)
        while self.motorC.angle() > -distance*self.DEG_TO_ROT:
            print(self.motorC.angle())
            print("\n")
            wait(10)
        self.motorB.run(0)
        self.motorC.run(0)

    def turnright(self,speed,angle):
        self.reset()
        self.motorB.run(speed*-1*self.LAR_MOTOR)
        self.motorC.run(speed*self.LAR_MOTOR)
        print("turn")
        while self.gyroSensor.angle() < angle:
            wait(5)
            print(self.gyroSensor.angle())
        if self.gyroSensor.angle() > angle:
            while self.gyroSensor.angle() > angle:
                self.motorB.run(20*self.LAR_MOTOR)
                self.motorA.run(-20*self.LAR_MOTOR)
        self.motorB.run(0)
        self.motorC.run(0)

    def turnleft(self,speed,angle):
        self.reset()
        self.motorB.run(speed*self.LAR_MOTOR)
        self.motorC.run(speed*-1*self.LAR_MOTOR)
        print("turn")
        while self.gyroSensor.angle() > angle*-1:
            wait(5)
            print(self.gyroSensor.angle())
        if self.gyroSensor.angle() < angle:
            while self.gyroSensor.angle() < angle:
                self.motorB.run(-20*self.LAR_MOTOR)
                self.motorA.run(20*self.LAR_MOTOR)
        self.motorB.run(0)
        self.motorC.run(0)
    
    def DogGearA(self,speed,distance,direction):
        self.reset()
        if direction == 1:
            self.motorA.run(speed*self.MED_MOTOR)
            print("clDogRotate")
            while self.motorA.angle() < distance*self.DEG_TO_ROT:
                wait(5)
                print(self.motorA.angle())
            self.motorA.run(0)

        elif direction == -1:
            self.motorA.run(speed*direction*self.MED_MOTOR)
            print("cnclDogRotate")
            print(distance*direction*self.DEG_TO_ROT)
            while self.motorA.angle() > distance*direction*self.DEG_TO_ROT:
                wait(5)
                print(self.motorA.angle())
            self.motorA.run(0)

    def attachMotorD(self,speed,distance,direction):
        self.reset()
        if direction == 1:
            self.motorD.run(speed*self.LAR_MOTOR)
            print("forMotorDRotate")
            print(self.motorD.angle())
            while self.motorD.angle() < distance*self.DEG_TO_ROT:
                wait(5)
                print(self.motorD.angle())
            self.motorD.run(0)

        elif direction == -1:
            self.motorD.run(speed*direction*self.LAR_MOTOR)
            print("aftMotorDRotate")
            while self.motorD.angle() > distance*direction*self.DEG_TO_ROT:
                wait(5)
                print(self.motorD.angle())
            self.motorD.run(0)
    
    def shallowTurn(self,rightspeed,leftspeed,angle,direction):
        self.reset()
        self.motorB.run(rightspeed*self.LAR_MOTOR)
        self.motorC.run(leftspeed*self.LAR_MOTOR)
        print("turn")
        if direction == -1:
            while self.gyroSensor.angle() > angle: 
                wait(5)
                print(self.gyroSensor.angle())
            self.motorB.run(0)
            self.motorC.run(0)
        elif direction == 1:
            while self.gyroSensor.angle() < angle:
                wait(5)
                print(self.gyroSensor.angle())
            self.motorB.run(0)
            self.motorC.run(0)
        self.motorB.run(0)
        self.motorC.run(0)

    def runUntilStucked(self, motor, speed, direction):
        if direction == 1:
            motor.run_until_stalled(speed*self.LAR_MOTOR, Stop.COAST, 100)
        elif direction == -1:
            motor.run_until_stalled(-speed*self.LAR_MOTOR, Stop.COAST, 100)

    def findLine(self, speed, color, sensor):
        self.reset()
        self.motorB.run(speed*self.LAR_MOTOR)
        self.motorC.run(speed*self.LAR_MOTOR)
        print("findLine")
        if sensor == 1:
            while self.colorSensorleft.color() != color:
                wait(5)
                print(self.colorSensorleft.color())
        elif sensor == 2:
            while self.colorSensorright.color() != color:
                wait(5)
                print(self.colorSensorright.color())
        self.motorB.run(0)
        self.motorC.run(0)
    # def alignWall(self, speed,):
    #     self.reset()
    #     self.motorB.run(-1*speed)
    #     self.motorA.run(speed*-1)
    #     print("alignWall")
    #     while !self.motorA.stalled() || !self.motorB.stalled():
    #         if !self.motorA.stalled() && !self.motorB.stalled():
    #             wait(5)
    #         elif self.motorA.stalled() && !self.motorB.stalled():
    #             wait(5)
    #             self.motorA.run(0)
    #             self.motorB.run(-1*speed)
    #         elif !self.motorA.stalled() && self.motorB.stalled():
    #             wait(5)
    #             self.motorA.run(-1*speed)
    #             self.motorB.run(0)
    #         elif self.motorA.stalled() && self.motorB.stalled():
    #             self.motorA.run(0)
    #             self.motorB.run(0)
    #     self.reset()
    def alignWallMark2(self,speed):
        self.reset()
        self.motorB.run(speed*-1*LAR_MOTOR)
        self.motorA.run(speed*-1*LAR_MOTOR)
        print("alignWall")
        while motorB.speed() > 20 and motorC.speed() > 20:
            wait(5)
        self.motorB.run(0)
        self.motorC.run(0)