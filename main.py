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

# #hoid.DogGearA(100,6,-1)
# #hoid.forward(100,660)
# #hoid.backward(100,660)
# #hoid.turnleft(100,81)
# #hoid.turnright(50,81)
# #hoid.shallowTurn(50,150,90,-1)
# crane = Crane(hoid)
# #crane.run()
# # bridge = Bridge(hoid)
# # bridge.run()
# # hoid.attachMotorD(50,660,-1)

# #muchPointExploit = MuchPointExploit(hoid)
# #muchPointExploit.run()

# elevator=Elevator(hoid)
# elevator.run()


countED=0
names=["crane","bridge","muchPointExploit","elevator"]
missions=[Crane(hoid),Bridge(hoid),MuchPointExploit(hoid),Elevator(hoid)]

while countED<5:
    brick.display.text(names[countED])
    buttons= brick.buttons()
    if Button.CENTER in buttons:
        missions[countED].run()
        countED= countED+1
    if Button.UP in buttons:
         countED= countED+1
    if Button.DOWN in buttons:
         countED= countED-1