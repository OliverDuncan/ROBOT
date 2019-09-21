#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from robot import Robot

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

# crane = Crane(hoid)
# crane.run()
 bridge = Bridge (hoid)
 bridge.run()

# hoid.forward(250,660)
# hoid.backward(250,660)
# hoid.turnleft(250,81)
# hoid.turnright(250,81)
