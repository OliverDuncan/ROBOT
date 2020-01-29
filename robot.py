
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
      
    # these are constants that are used later in various functions
    LAR_MOTOR=10
    MED_MOTOR=14.4
    DEG_TO_ROT=360

    def getMotorD(self):
        return self.motorD

    def getMotorA(self):
        return self.motorA
    

    def reset(self):
        # this just resets all of the motor angle sensors 
        self.motorB.reset_angle(0)
        self.motorC.reset_angle(0)
        self.motorD.reset_angle(0)
    
    def resetMotorA(self):
        self.motorA.reset_angle(0)
    
    def resetGyro(self):
        # this resets the gyro sensor
        self.gyroSensor.reset_angle(0)

    def runForward(self,speed):
        self.motorB.run(speed*self.LAR_MOTOR)
        self.motorC.run(speed*self.LAR_MOTOR)

    def runBackward(self,speed):
        self.motorB.run(speed*self.LAR_MOTOR*-1)
        self.motorC.run(speed*self.LAR_MOTOR*-1)

    def stopRun(self):
        self.motorB.run(0)
        self.motorC.run(0)

    def forward(self,speed,distance):# This is the function to move the robot forward.
        self.reset()# This resets the angles on all of the motors.
        # print("test")# This prints test on the computer for debugging
        self.runForward(speed)# to transition the degrees per second into a scale of 1 to 100, 100 being as fast as possible for the large motorA.run_timeotor which is 990 d/s
        # The motors will continue to run until they are told to stop, so until the motor angle is greater than the distance it will
        while self.motorC.angle() < distance*self.DEG_TO_ROT:
            wait(5)
        self.stopRun()

    def forwardRampUp(self,finalSpeed,distance):
        accel=1.1
        self.reset()
        speed=5* self.LAR_MOTOR
        while speed < finalSpeed*self.LAR_MOTOR and self.motorC.angle() < distance*self.DEG_TO_ROT :
            self.runForward(speed)
            wait(1)
            speed=speed*accel
        while self.motorC.angle() < distance*self.DEG_TO_ROT:
            wait(1)
        self.stopRun()

    def backward(self,speed,distance): # This does the same as the forward but in reverse.
        self.reset()
        self.runBackward(speed)
        while self.motorC.angle() > -distance*self.DEG_TO_ROT:
            # print(self.motorC.angle())
            # print("\n")
            wait(5)
        self.stopRun()

    # This function turns the robot to the right.
    def turnright(self,speed,angle): 
        self.reset() # Again it resets first.
        self.motorB.run(speed*-1*self.LAR_MOTOR) # Then it makes one motor rotate one direction
        self.motorC.run(speed*self.LAR_MOTOR) # and the other motor rotates the other direction causing the robot to turn.
        # print("turn")
        while self.gyroSensor.angle() < angle:# Then same as the forward/backward it loops until the gyrosensor is greater than the angle.
            wait(1)
        self.stopRun()
        # print("step 2")
        while self.gyroSensor.angle() > angle + 1: # Then differing from forward/backward it corrects itself, because the gyro overshoots.
                # print(self.gyroSensor.angle())
                self.motorB.run(speed/2*self.LAR_MOTOR)
                self.motorC.run(-speed/2*self.LAR_MOTOR)
        self.stopRun() # Then it stops for the last time
        # print(self.gyroSensor.angle())

    def turnleft(self,speed,angle): #See Also turnright
        this.turnLeftNoReset(speed, angle*-1)
        # self.reset()
        # self.motorB.run(speed*self.LAR_MOTOR)
        # self.motorC.run(speed*-1*self.LAR_MOTOR)
        # # print("turn")
        # while self.gyroSensor.angle() > angle*-1:
        #     wait(1)
        #     # print(self.gyroSensor.angle())
        # while self.gyroSensor.angle() < ((angle*-1)-1):
        #     self.motorB.run(-speed/2*self.LAR_MOTOR)
        #     self.motorC.run(speed/2*self.LAR_MOTOR)
        # self.motorB.run(0)
        # self.motorC.run(0)

    def turnLeftNoReset(self,speed,angle): #See Also turnright
        self.reset()
        self.motorB.run(speed*self.LAR_MOTOR)
        self.motorC.run(speed*-1*self.LAR_MOTOR)
        # print("turn")
        while self.gyroSensor.angle() > angle:
            wait(1)
            # print(self.gyroSensor.angle())
        while self.gyroSensor.angle() < ((angle)-1):
            self.motorB.run(-speed/2*self.LAR_MOTOR)
            self.motorC.run(speed/2*self.LAR_MOTOR)
        self.stopRun()
    
    def DogGearA(self,speed,distance,direction): #Rotates the dog gear in port A
        self.resetMotorA()
        if direction == 1: # if the function is told either 1 or -1 then rotates in one direction or the other. 
            self.motorA.run(speed*self.MED_MOTOR)
            # print("clDogRotate")
            while self.motorA.angle() < distance*self.DEG_TO_ROT: # it turns the motor until it meets distance specifications.
                wait(1)
                # print(self.motorA.angle())
            self.motorA.run(0)

        elif direction == -1:
            self.motorA.run(speed*direction*self.MED_MOTOR)
            # print("cnclDogRotate")
            # print(distance*direction*self.DEG_TO_ROT)
            while self.motorA.angle() > distance*direction*self.DEG_TO_ROT:
                wait(1)
                # print(self.motorA.angle())
            self.motorA.run(0)

    def DogGearHold(self,speed,distance,direction): #This causes the dog gear to hold its position.
        self.resetMotorA()
        this.DogGearHoldNoReset(speed,distance,direction)
        # if direction == 1:
        #     self.motorA.run(speed*self.MED_MOTOR)
        #     # print("clDogRotate")
        #     while self.motorA.angle() < distance*self.DEG_TO_ROT:
        #         wait(1)
        #         # print(self.motorA.angle())
        #     self.motorA.stop(Stop.HOLD)

        # elif direction == -1:
        #     self.motorA.run(speed*direction*self.MED_MOTOR)
        #     # print("cnclDogRotate")
        #     # print(distance*direction*self.DEG_TO_ROT)
        #     while self.motorA.angle() > distance*direction*self.DEG_TO_ROT:
        #         wait(1)
        #         # print(self.motorA.angle())
        #     self.motorA.stop(Stop.HOLD)
            
    def DogGearHoldNoReset(self,speed,distance,direction): #This causes the dog gear to hold its position.
        if direction == 1:
            self.motorA.run(speed*self.MED_MOTOR)
            # print("clDogRotate")
            while self.motorA.angle() < distance*self.DEG_TO_ROT:
                wait(1)
                # print(self.motorA.angle())
            self.motorA.stop(Stop.HOLD)

        elif direction == -1:
            self.motorA.run(speed*direction*self.MED_MOTOR)
            # print("cnclDogRotate")
            # print(distance*direction*self.DEG_TO_ROT)
            while self.motorA.angle() > distance*direction*self.DEG_TO_ROT:
                wait(1)
                # print(self.motorA.angle())
            self.motorA.stop(Stop.HOLD)




    def attachMotorD(self,speed,distance,direction): # This rotates the large attachment motor.
        self.reset()
        if direction == 1:
            self.motorD.run(speed*self.LAR_MOTOR)
            # print("forMotorDRotate")
            # print(self.motorD.angle())
            while self.motorD.angle() < distance*self.DEG_TO_ROT:
                wait(5)
                # print(self.motorD.angle())
            self.motorD.stop(Stop.COAST)

        elif direction == -1:
            self.motorD.run(speed*direction*self.LAR_MOTOR)
            # print("aftMotorDRotate")
            while self.motorD.angle() > distance*direction*self.DEG_TO_ROT:
                wait(5)
                # print(self.motorD.angle())
            self.motorD.stop(Stop.COAST)

    def attachMotorDHold(self,speed,distance,direction):
        this.attachMotorD(speed,distance,direction)
        self.motorD.stop(Stop.HOLD)
        
        # self.reset()


        # if direction == 1:
        #     self.motorD.run(speed*self.LAR_MOTOR)
        #     # print("forMotorDRotate")
        #     # print(self.motorD.angle())
        #     while self.motorD.angle() < distance*self.DEG_TO_ROT:
        #         wait(5)
        #         # print(self.motorD.angle())
        #     self.motorD.stop(Stop.HOLD)

        # elif direction == -1:
        #     self.motorD.run(speed*direction*self.LAR_MOTOR)
        #     # print("aftMotorDRotate")
        #     while self.motorD.angle() > distance*direction*self.DEG_TO_ROT:
        #         wait(5)
        #         # print(self.motorD.angle())
        #     self.motorD.stop(Stop.HOLD)

    
    def shallowTurn(self,rightspeed,leftspeed,angle,direction): # Turns the robot shallowly by running both motors in the same direction but one faster than the other.
        self.reset()
        self.resetGyro()
        self.motorB.run(rightspeed*self.LAR_MOTOR)
        self.motorC.run(leftspeed*self.LAR_MOTOR)
        # print("turn")
        if direction == -1:
            while self.gyroSensor.angle() > angle: 
                wait(5)
                # print(self.gyroSensor.angle())
            self.stopRun()
        elif direction == 1:
            while self.gyroSensor.angle() < angle:
                wait(5)
                # print(self.gyroSensor.angle())
            self.stopRun()

    def findLine(self, speed, color, sensor): # Drives forward until specified sensor finds a line.
        self.reset()
        self.runForward(speed)
        # print("findLine")
        if sensor == 1:
            while self.colorSensorleft.color() != color:
                wait(5)
                # print(self.colorSensorleft.color())
        elif sensor == 2:
            while self.colorSensorright.color() != color:
                wait(5)
                # print(self.colorSensorright.color())
        self.stopRun()


  

    # def motorBySeconds(motor, seconds, speed, direction):
    #     self.reset()
    #     if motor == self.motorA:
    #         speed = speed*self.MED_MOTOR
    #     else 
    #         speed = speed*self.LAR_MOTOR 
    #     motor.run_time(speed, seconds*1000, Stop.BRAKE)

    def turnRightSloppy(self,speed,angle): # This pair of functions turns sloppily to save time in situations where it isn't nescessary to be precise.
        self.reset()
        self.motorB.run(speed*-1*self.LAR_MOTOR)
        self.motorC.run(speed*self.LAR_MOTOR)
        # print("turn")
        while self.gyroSensor.angle() < angle:
            wait(1)
        self.motorB.stop()
        self.motorC.stop()
        # print(self.gyroSensor.angle())

    def turnLeftSloppy(self,speed,angle):
        self.reset()
        self.motorB.run(speed*self.LAR_MOTOR)
        self.motorC.run(speed*-1*self.LAR_MOTOR)
        # print("turn")
        while self.gyroSensor.angle() > angle*-1:
            wait(1)
        self.motorB.run(0)
        self.motorC.run(0)

    def driveStraight(self,speed,distance,angle): # this drives straight by turning when thrown off to the same relative angle specified.
        self.reset()
        drivebase = DriveBase(self.motorC, self.motorB, 62.4, 101)
        brick.display.clear()
        while self.motorC.angle() < distance*self.DEG_TO_ROT and self.motorB.angle() < distance*self.DEG_TO_ROT:
            error = self.gyroSensor.angle()- angle
            error= error * -4
            print(error)
            drivebase.drive(speed, error)
        self.motorB.run(0)
        self.motorC.run(0)
    
   
    def readGyro(self):
        return self.gyroSensor.angle()

    def dontFindTheColor(self,speed,sensor):
        self.reset()
        self.motorB.run(speed*self.LAR_MOTOR)
        self.motorC.run(speed*self.LAR_MOTOR)
        # print("findLine")
        if sensor == 1:
            while self.colorSensorleft.color() == Color.WHITE or self.colorSensorleft.color() == Color.BLACK:
                while self.colorSensorleft.color() == Color.WHITE or self.colorSensorleft.color() == Color.BLACK:
                    wait(5)
                wait(10)
                    # print(self.colorSensorleft.color())
        elif sensor == 2:
            while self.colorSensorright.color() == Color.WHITE or self.colorSensorright.color() == Color.BLACK:
                while self.colorSensorright.color() == Color.WHITE or self.colorSensorright.color() == Color.BLACK:
                    wait(5)
                wait(10)
                # print(self.colorSensorright.color())
        self.motorB.run(0)
        self.motorC.run(0)


    
    def backwardRampUp(self,finalSpeed,distance):
        accel=1.2
        self.reset()
        speed=-5* self.LAR_MOTOR
        while speed > finalSpeed*self.LAR_MOTOR*-1 and  self.motorC.angle() > distance*self.DEG_TO_ROT*-1:
            self.motorB.run(speed)      
            self.motorC.run(speed)
            wait(10)
            speed=speed*accel
        while self.motorC.angle() > distance*self.DEG_TO_ROT*-1:
            wait(1)
        self.motorB.run(0)
        self.motorC.run(0)

    def alignWall(self,finalSpeed): # This was the second attempt at a align wall function. Instead of using run_until_stalled we stop the motor when it starts moving slower. 
        self.reset()
        finalSpeed = finalSpeed * -1 * self.LAR_MOTOR
        speed= 5 * -1 * self.LAR_MOTOR
        while speed > finalSpeed:
            self.motorB.run(speed)
            self.motorC.run(speed)
            wait(10)
            speed = speed * 1.2
        # print("alignWall")
        # wait (500)
        while self.motorB.speed() *-1> 50*self.LAR_MOTOR or self.motorC.speed() > 50*self.LAR_MOTOR:
            # print(self.motorB.speed())
            wait(1)
        self.motorB.run(0)
        self.motorC.run(0)

    
    def runUntilStucked(self, motor, speed, direction): # Rotates specified motor until it can't anymore using premade function run_until_stalled
        if direction == 1:
            motor.run_until_stalled(speed*self.LAR_MOTOR, Stop.COAST, 100)
        elif direction == -1:
            motor.run_until_stalled(-speed*self.LAR_MOTOR, Stop.COAST, 100)