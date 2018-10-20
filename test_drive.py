# from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering

# sp = MoveSteering(OUTPUT_A, OUTPUT_B)
# sp.on_for_rotations(-100, SpeedPercent(20), 10)

from foobot.drive import FoobotDrive
car = FoobotDrive(4.7, 11.1, 1, 70, 20)
car.turn_left(45)
car.turn_right(45)
