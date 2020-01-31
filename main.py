#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from robot import Robot
from bridge import Bridge
from crane import Crane
from muchPointExploit import MuchPointExploit
from elevator import Elevator
from wheelchairlady import wheelchairlady
from AllBatsAreDrones import AllBatsAreDrones
from parkish import Parkish
from testunodos import Testunodos
from TreesDeath import TreesDeath
from CrossyRoad import CrossyRoad
from Deathish import Deathish
from HoldMotorD import HoldMotorD

# Write your program here 
brick.sound.beep()
motorA=Motor(Port.A)
motorC = Motor(Port.C)
motorB = Motor(Port.B)
motorD=Motor(Port.D)
sensor1= ColorSensor(Port.S1)
sensor2=ColorSensor(Port.S2)
sensor3=GyroSensor(Port.S3)
sensor4=TouchSensor(Port.S4)

hoid= Robot(motorA,motorB,motorC,motorD,sensor1,sensor2,sensor3,sensor4)
countED=0
# Create the arrays
names=["crane","muchPointExploit", "HoldmotorD", "deathish", "parkish","CrossyRoad","wheelchairlady","TreesDeath","Testunodos"]
missions=[Crane(hoid),MuchPointExploit(hoid),HoldMotorD(hoid),Deathish(hoid),Parkish(hoid),CrossyRoad(hoid),WheelchairLady(hoid),TreesDeath(hoid),Testunodos(hoid)]

def buttonrelease():
    while any(brick.buttons()):
        wait(10)

while True:
    brick.display.text(names[countED])
    if Button.CENTER in brick.buttons():
        # run selected mission
        buttonrelease()        
        missions[countED].run()
        if (countED != 6):
            countED= countED+1
    # move up and down in the list
    if Button.UP in brick.buttons():
        buttonrelease()
        countED= countED+1
    if Button.DOWN in brick.buttons():
        buttonrelease()
        countED= countED-1
    if Button.LEFT in brick.buttons():
        buttonrelease()
        hoid.brick.sound.beep(1500, 3000, 30)
    
        