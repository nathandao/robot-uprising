from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering

from foobot.drive import FoobotDrive

car = FoobotDrive(4.7, 11.4, 1, 70, 20)

car.turn(45)
car.turn(-45)
