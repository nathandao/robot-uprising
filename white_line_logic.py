import time
from variables import *

class WhiteLineFollower:
    def __init__(self, car, color_sensor):
        self.car = car
        self.color_sensor = color_sensor

    def isValueBetween(self, min, max, value):
        if value < min and value > max:
            return True
        return False

    def is_it_white(self, rgb):
        if rgb[0] > whiteRMinVal and rgb[1] > whiteGMinVal and rgb[2] > whiteBMinVal:
            print('is WHITE')
            return True
        print('NOT ----- white')
        return False

    def is_it_yellow(self, rgb):
        if self.isValueBetween(yellowRMinVal, yellowRMaxVal, rgb[0]) and self.isValueBetween(yellowGMinVal, yellowGMaxVal, rgb[1]) and self.isValueBetween(yellowBMinVal, yellowBMaxVal, rgb[2]):
            return True
        return False

    def is_it_orange(self, rgb):
        if self.isValueBetween(orangeRMinVal, orangeRMaxVal, rgb[0]) and self.isValueBetween(orangeGMinVal, orangeGMaxVal, rgb[1]) and self.isValueBetween(orangeBMinVal, orangeBMaxVal, rgb[2]):
            return True
        return False

    def run(self):
        while True:
            # If both sensors on white, prioritise right turns
            if self.is_it_white(self.color_sensor.rgb_left()) and self.is_it_white(self.color_sensor.rgb_right()):
                self.car.stop()
                self.car.turn_right(15)
            elif self.is_it_white(self.color_sensor.rgb_left()):
                self.car.stop()
                self.car.turn_left(15)
            elif self.is_it_white(self.color_sensor.rgb_right()):
                self.car.stop()
                self.car.turn_right(15)
            # On yellow just go pres button and come back
            elif self.is_it_yellow(self.color_sensor.rgb_left()) or self.is_it_yellow(self.color_sensor.rgb_right()):
                print('YELLOW ---')
                self.car.stop()
                self.car.move_straigth(10)
                time.sleep(8)
                self.car.move_straigth(-10)
                self.car.turn_left(180)
            # Section end if we reach orange color
            elif self.is_it_orange(self.color_sensor.rgb_left()) or self.is_it_orange(self.color_sensor.rgb_right()):
                print('ORANGE --- STOP')
                self.car.stop()
            else:
                print('RUNNING===============')
                self.car.run()
        self.car.stop()

    def stop(self):
        self.car.stop()
