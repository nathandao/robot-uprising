#!/usr/bin/env python3
import variables
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
    while not whitetapeInShadowDetected(cs.rgb_left()):
        moveForwardWithWallDistance(8, 5, 5)
    print("detected whitetape")
    car.turn_left(45)
    while orangeColorInShadowDetected(cs.rgb_left()):
        car.move_straigth(45)
        


# detects if color is orange and sends back a boolean
def orangeColorInShadowDetected(colorArray):
    if (colorArray[0] < variables.orangeRMaxVal and colorArray[0] > variables.orangeRMinVal) and (colorArray[1] < variables.orangeGMaxVal and colorArray[1] > variables.orangeGMinVal) and (colorArray[2] < variables.orangeBMaxVal and colorArray[2] > variables.orangeBMinVal):
        print('Orange Not Detected')
        return True
    else:
        print('Orange Detected!===================')
        return False

# detects whitetape in shadow conditions
def whitetapeInShadowDetected(colorArray):
    if (colorArray[0] < variables.whiteRMaxVal and colorArray[0] > variables.whiteRMinVal) and (colorArray[1] < variables.whiteGMaxVal and colorArray[1] > variables.whiteGMinVal) and (colorArray[2] < variables.whiteBMaxVal and colorArray[2] > variables.whiteBMinVal):
        print('Orange Not Detected')
        return True
    else:
        print('Orange Detected!===================')
        return False

# function for moving forward, give target distance (cm) from wall, increment for movement in cm and turn in degrees
def moveForwardWithWallDistance(targetDistanceFromWall, moveIncrement, turnIncrement):
    target = targetDistanceFromWall
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
