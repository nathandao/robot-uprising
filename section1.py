#!/usr/bin/env python3

from foobot.ultrasonic_sensor import FoobotUltrasonicSensor
from main import car, cs, us

orangeRedHighVal = 180
orangeRedLowVal = 155
orangeGreenHighVal = 55
orangeGreenLowVal = 30
orangeBlueHighVal = 45
orangeBlueLowVal = 20

#gets initial distance from wall to the right of the robot
UsDistanceFromWall = us.distance()

def moveFromStartToOrange():
    while not orangeColorDetected(cs.rgb_left()):
        moveForwardWithWallDistance(10, 10, 10)


# detects if color is orange and sends back a boolean
def orangeColorDetected(colorArray):
    if (colorArray[0] < orangeRedHighVal and colorArray[0] > orangeRedLowVal) and (colorArray[1] < orangeGreenHighVal and colorArray[1] > orangeGreenLowVal) and (colorArray[2] < orangeBlueHighVal and colorArray[2] > orangeBlueLowVal):
        print('Orange Not Detected')
        return True
    else:
        print('Orange Detected!===================')
        return False

# function for moving forward, give target distance (cm) from wall, increment for movement in cm and turn in degrees
def moveForwardWithWallDistance(targetDistanceFromWall, moveIncrement, turnIncrement):
    target = targetDistanceFromWall
    car.move_straigth(moveIncrement)
    if (us.distance() > target):
        print('distance hight than target, turning left')
        car.turn_left(turnIncrement)
        car.move_straigth(moveIncrement)
    elif (us.distance() < target):
        print('distance lower than target, turning right')
        car.turn_right(turnIncrement)
        car.move_straigth(moveIncrement)
    else:
        print('moving straight')
        car.move_straigth(moveIncrement)

moveFromStartToOrange()
