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
                 default_speed = 50,
                 default_turn_speed = 20):

        self.wheel_diameter = wheel_diameter
        self.wheel_circ = wheel_diameter * pi
        self.wheel_dist = wheel_dist
        self.default_speed = default_speed
        self.default_turn_speed = default_turn_speed
        self.gear_ratio = gear_ratio
        self.move_steering = MoveSteering(OUTPUT_A, OUTPUT_B)
        self.move_tank= MoveTank(OUTPUT_A, OUTPUT_B)

    def move_straigth(self, distance, speed = 0):
        if speed == 0:
            speed = self.default_speed
        rotations = distance / self.wheel_dist / self.gear_ratio
        self.move_tank.stop()
        self.move_tank.on_for_rotations(self.default_speed, self.default_speed, rotations)

    def turn(self, deg, speed = 0):
        steering = -100
        if speed == 0:
            speed = self.default_turn_speed
        if deg < 0:
            deg = 0 - deg
            steering = 0 - steering
        rotation_arc = (pi * self.wheel_dist) * (deg / 360)
        rotations = rotation_arc / 8 / self.gear_ratio
        self.move_tank.stop()
        self.move_steering.on_for_rotations(steering, speed, rotations)

    def turn_right(self, deg, speed = 0):
        self.turn(0 - deg, speed)

    def turn_left(self, deg, speed = 0):
        self.turn(deg, speed)

    def run(self, speed = 0):
        if speed == 0:
            speed = self.default_speed
        self.move_tank.on(speed)


    def stop(self):
        self.move_tank.stop()
