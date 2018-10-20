#!/usr/bin/env python3

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2

class FoobotColorSensor:
  def __init__(self):
    self.left = ColorSensor(INPUT_1)
    self.right = ColorSensor(INPUT_2)

  # gives the color reading of either
  # 'unknown','black','blue','green','yellow','red','white' or 'brown'
  def color(self, s):
    if s.mode != 'COL-COLOR':
      s.mode = 'COL-COLOR'
    colors = ('unknown','black','blue','green','yellow','red','white','brown')
    return colors[s.value()]

  def color_left(self):
    return self.color(self.left)

  def color_right(self):
    return self.color(self.right)

  # gives numberical intensity reading
  def intensity(self, s):
    if s.mode != 'COL-REFLECT':
      s.mode = 'COL-REFLECT'
    return s.value

  def intensity_left(self):
    return self.intensity(self.left)

  def intensity_right(self):
    return self.intensity(self.right)

  # gives ambient light reading value
  def ambient(self, s):
    if s.mode != 'COL-AMBIENT':
      s.mode = 'COL-AMBIENT'
    return s.value

  def ambient_left(self):
    return self.ambient(self.left)

  def ambient_right(self):
    return self.ambient(self.right)

  # gives raw numerical rgb reading value as an array of [red, green, blue]
  def rgb(self, s):
    if s.mode != 'RGB-RAW':
      s.mode = 'RGB-RAW'
    return [s.value(0), s.value(1), s.value(2)]

  def rgb_left(self):
    return self.rgb(self.left)

  def rgb_right(self):
    return self.rgb(self.right)
