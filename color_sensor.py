#!/usr/bin/env python3

from ev3dev2.sensor import ColorSensor, INPUT_1, INPUT_2

cl = ColorSensor(INPUT_1)

cl.mode = 'COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')

while True:
  print(colors[cl.value()])
