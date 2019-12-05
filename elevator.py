from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Elevator:
    def  __init__(self, robot):
       self.robot=robot
    
    def run(self):
       self.robot.forward(50,.03)
       self.robot.turnright(20,82)
       wait(500)
       self.robot.forward(40,5.5)
       self.robot.DogGearA(20,.05,-1)
       self.robot.forward(50,1)
       self.robot.DogGearA(20,.05,-1)
       print ("before backward")
       self.robot.backward(50,7.45)

    
    