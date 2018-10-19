from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering
from math import pi

# Usage:
# car = FoobotDrive(wheel_diameter, distance_between_wheel_center_points, default_speed)
# if default_speed is not set, default speed is 50

# distances and lenght in cm

class FoobotDrive:

    def __init__(self,
                 wheel_diameter,
                 wheel_dist,
                 gear_ratio = 1,
                 default_speed = 0,
                 default_turn_speed = 100):

        self.wheel_diameter = wheel_diameter
        self.wheel_circ = wheel_diameter * pi
        self.wheel_dist = wheel_dist
        self.default_speed = default_speed
        self.default_turn_speed = default_turn_speed
        self.gear_ratio = gear_ratio
        # self.move_steering = MoveSteering(OUTPUT_A, OUTPUT_B)
        self.move_tank= MoveTank(OUTPUT_A, OUTPUT_B)

    def move_straigth(self, distance, speed = 0):
        if speed == 0:
            speed = self.default_speed
        rotations = distance / self.wheel_dist / gear_ratio
        self.move_tank.on_for_rotations(self.default_speed, self.default_speed, rotations)

    def turn(self, deg, speed = 0):
        if speed == 0:
            speed = self.default_turn_speed
        if deg < 0:
            speed = 0 - speed
        rotation_arc = (pi * self.wheel_dist) * (deg / 360)
        self.move_tank.on_for_rotations(speed, 0 - speed, rotation_arc / 16 / gear_ratio)

    def turn_right(self, deg, speed = 0):
        turn(deg, speed)

    def turn_left(self, deg, speed = 0):
        turn(0 - deg, speed)

    def run(self, speed = 0):
        if speed == 0:
            speed = self.default_speed
        self.move_tank.run_forever(speed)
