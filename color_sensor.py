#!/usr/bin/env python3

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2

class FoobotColorSensor:
  def __init__(self):
    self.left = ColorSensor(INPUT_1)
    self.right = ColorSensor(INPUT_2)

  def get_sensor_color(self, s):
    s.mode = 'COL-COLOR'
    colors=('unknown','black','blue','green','yellow','red','white','brown')
    return colors[s.value()]

  def left_color(self):
    return self.get_sensor_color(self.left)

  def right_color(self):
    return self.get_sensor_right(self.right)
