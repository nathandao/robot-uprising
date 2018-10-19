#!/usr/bin/env python3

from drive import FoobotDrive

car = FoobotDrive(3.53, 15.28, 3/5, 70, 20)

car.move_straigth(20)
car.turn_left(180)
car.turn_right(90)
car.move_straigth(-20)
