#!/usr/bin/env python3

from foobot.drive import FoobotDrive

car = FoobotDrive(3.7, 10.5, 3/5, 70, 20)

while True:
    dist = input("distance: ")
    car.move_straigth(int(dist))
