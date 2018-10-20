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

    def is_it_white(self, rbg):
        if rbg[0] > whiteRMinVal and rgb[1] > whiteGMinVal and rgb[2] > whiteBMinVal:
            print('is WHITE')
            return True
        print('NOT ----- white')
        return False

    def is_it_yellow(self, rbg):
        if self.isValueBetween(yellowRMinVal, yellowRMaxVal, rbg[0]) and self.isValueBetween(yellowGMinVal, yellowGMaxVal, rbg[1]) and self.isValueBetween(yellowBMinVal, yellowBMaxVal, rbg[2]):
            return True
        return False

    def is_it_orange(self, rbg):
        if self.isValueBetween(orangeRMinVal, orangeRMaxVal, rbg[0]) and self.isValueBetween(orangeGMinVal, orangeGMaxVal, rbg[1]) and self.isValueBetween(orangeBMinVal, orangeBMaxVal, rbg[2]):
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
                self.car.stop()
            else:
                print('RUN FORWARD ---')
                self.car.run()
        self.car.stop()

    def stop(self):
        self.car.stop()
