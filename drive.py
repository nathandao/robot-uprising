from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering
from math import pi

class FoobotDrive:

    def __init__(self, wheel_d, wheel_dist, default_speed = 50):
        self.wheel_d = wheel_d
        self.wheel_circ = wheel_d * pi
        self.wheel_dist = wheel_dist
        self.default_speed = default_speed
        # self.move_steering = MoveSteering(OUTPUT_A, OUTPUT_B)
        self.move_tank= MoveTank(OUTPUT_A, OUTPUT_B)

    def move_straigth(self, distance, speed = self.default_speed):
        rotations = distance / self.wheel_dist
        self.move_tank.on_for_rotations(self.default_speed, self.default_speed, rotations)
