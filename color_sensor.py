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

  def left_color(self):
    return self.get_color(self.left)

  def right_color(self):
    return self.get_color(self.right)

  def intensity(self, s):
    s.mode = 'COL-REFLECT'
    return s.value()

  def intensity_left(self):
    return self.get_intensity(self.left)

  def right_intensity(self):
    return self.get_intensity(self.right)

  def get_sensor_ambient(self, s):
    s.mode = 'COL-AMBIENT'
    return s.value()

  def left_ambient(self):
    return self.get_ambient(self.left)

  def right_ambient(self):
    return self.get_ambient(self.right)

  def get_sensor_rgb_raw(self, s):
    s.mode = 'COL-RGB-RAW'
    return s.value()

  def left_rgb_raw(self):
    return self.get_rgb_raw(self.left)

  def right_rgb_raw(self):
    return self.get_rgb_raw(self.right)
