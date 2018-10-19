#!/usr/bin/env python3

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2

cl1 = ColorSensor(INPUT_1)
cl2 = ColorSensor(INPUT_2)

cl.mode = 'COL-REFLECT'
colors=('unknown','black','blue','green','yellow','red','white','brown')

while True:
  print(colors[cl1.value()])
  print(colors[cl2.value()])
