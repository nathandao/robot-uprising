import keyboard #Using module keyboard
from drive import FoobotDrive

car = FoobotDrive(3.53, 15.28, 3/5, 50, 20)

def shout(e):
    car.stop()

keyboard.on_release(shout)

while True:
    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            car.run()
        if keyboard.is_pressed(keyboard.KEY_DOWN):
            car.run()
        if keyboard.is_pressed('q'):
            break
        else:
            pass
    except:
        break

car.stop()
