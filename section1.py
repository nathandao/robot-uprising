from foobot.color_sensor import FoobotColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering
from math import pi
from foobot.ultrasonic_sensor import FoobotUltrasonicSensor

orangeRedHighVal = 210
orangeRedLowVal = 190
orangeGreenHighVal = 223
orangeGreenLowVal = 203
orangeBlueHighVal = 170
orangeBlueLowVal = 140

foobie = FoobotDrive()
ultrasonic = FoobotUltrasonicSensor()
color_sensor = FoobotColorSensor()

#gets initial distance from wall to the right of the robot
UsDistanceFromWall = ultrasonic.distance()

#moves straigth and keeps distance from wall in a certain range of 10-15 cm


#bot moves from Start to first orange

def moveFromStartToOrange():
    while not orangeColorDetected(cs_left_rgb):
            moveForwardWithWallDistance(10, 10, 10)



#detects if color is orange and sends back a boolean
def orangeColorDetected(colorArray):
    if (colorArray[0] < orangeRedHighVal and colorArray[0] > orangeRedLowVal) and
    (colorArray[1] < orangeGreenHighVal and colorArray[1] > orangeGreenLowVal) and
    (colorArray[2] < orangeBlueHighVal and colorArray[2] > orangeBlueLowVal):
        return True
    else:
        return False

#function for moving forward, give target distance (cm) from wall, increment for movement in cm and turn in degrees
def moveForwardWithWallDistance(targetDistanceFromWall, moveIncrement, turnIncrement):

    target = targetDistanceFromWall
    foobie.move_straigth(moveIncrement)
    if (ultrasonic.distance() > target):
        foobie.turn_right(turnIncrement)
        foobie.move_straigth(moveIncrement)
    elif (ultrasonic.distance() < target):
        foobie.turn_left(turnIncrement)
        foobie.move_straigth(moveIncrement)
    else:
        foobie.move_straigth(moveIncrement)
