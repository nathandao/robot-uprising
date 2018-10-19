#!/usr/bin/env python3

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2

class FoobotColorSensor:
  def __init__(self):
    self.left = ColorSensor(INPUT_1)
    self.right = ColorSensor(INPUT_2)

  def color(self, s):
    s.mode = 'COL-COLOR'
    colors = ('unknown','black','blue','green','yellow','red','white','brown')
    return colors[s.value()]

  def left(self):
    return self.color(self.left)

  def color_right(self):
    return self.color(self.right)

  def intensity(self, s):
    s.mode = 'COL-REFLECT'
    return s.value()

  def intensity_left(self):
    return self.intensity(self.left)

  def intensity_right(self):
    return self.intensity(self.right)

  def ambient(self, s):
    s.mode = 'COL-AMBIENT'
    return s.value()

  def ambient_left(self):
    return self.ambient(self.left)

  def ambient_right(self):
    return self.ambient(self.right)

  def rgb(self, s):
    s.mode = 'COL-RGB-RAW'
    return s.value()

  def rgb_left(self):
    return self.rgb(self.left)

  def rgb_right(self):
    return self.rgb(self.right)
