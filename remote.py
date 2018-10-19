#!/usr/bin/env python3

from drive import FoobotDrive

car = FoobotDrive(3.53, 15.28, 3/5, 70, 20)

while True:
    dist = input()
    car.move_straigth(dist)
