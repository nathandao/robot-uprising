from getkey import getkey, keys
from drive import FoobotDrive
import thread
import time

car = FoobotDrive(5.6, 12)

val = 'test'

while True:
  key = getkey()
  if key == keys.UP:
      val = 'non test'
      print(val)
      car.move_straigth(0.5)
  elif key == keys.DOWN:
      val = 'test'
      print(val)
      car.move_straigth(-0.5)
  elif key == keys.LEFT:
      print(val)
      car.turn(-2)
  elif key == keys.RIGHT:
      print(val)
      car.turn(2)
  else:
      print(val)
      print("YYOLOOO")
