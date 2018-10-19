from getkey import getkey, keys
from drive import FoobotDrive

car = FoobotDrive(5.6, 12)

while True:
  key = getkey()
  if key == keys.UP:
      car.move_straigth(0.5)
  elif key == keys.DOWN:
      car.move_straigth(-0.5)
  elif key == keys.LEFT:
      car.turn(-2)
  elif key == keys.RIGHT:
      car.turn(2)
  else:
      print("YYOLOOO")
