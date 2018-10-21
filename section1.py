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

# detects if color is orange and sends back a boolean
def orangeColorInShadowDetected(colorArray):
    if (colorArray[0] < variables.orange_shadow_high_r and colorArray[0] > variables.orange_shadow_low_r) and (colorArray[1] < variables.orange_shadow_high_g and colorArray[1] > variables.orange_shadow_low_g) and (colorArray[2] < variables.orange_shadow_high_b and colorArray[2] > variables.orange_shadow_low_b):
        print('Orange Not Detected')
        return True
    else:
        print('Orange Detected!===================')
        return False

# detects whitetape in shadow conditions
def whitetapeInShadowDetected(colorArray):
    if (colorArray[0] < variables.whitetape_light_high_r and colorArray[0] > variables.whitetape_light_low_r) and (colorArray[1] < variables.whitetape_shadow_high_g and colorArray[1] > variables.whitetape_shadow_low_g) and (colorArray[2] < variables.whitetape_shadow_high_b and colorArray[2] > variables.whitetape_shadow_low_b):
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
        car.turn_left(turnIncrement)w
        car.move_straigth(moveIncrement)
    elif (us.distance() < target):
        print('distance lower than target, turning right')
        car.turn_right(turnIncrement)
        car.move_straigth(moveIncrement)
    else:
        print('moving straight')
        car.move_straigth(moveIncrement)

moveFromStartToOrange()
