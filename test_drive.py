from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering

sp = MoveSteering(OUTPUT_A, OUTPUT_B)
sp.on_for_rotations(-50, SpeedPercent(75), 45)

# from foobot.drive import FoobotDrive
# car = FoobotDrive(4.7, 11.4, 1, 70, 20)
# car.turn(-45)
# car.turn(45)
