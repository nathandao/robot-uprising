from threading import Thread
from time import sleep
import time
from variables import *

from foobot.drive import FoobotDrive
from foobot.color_sensor import FoobotColorSensor
from foobot.ultrasonic_sensor import FoobotUltrasonicSensor
from white_line_logic import WhiteLineFollower

# Initializing components and ports:
#
# Ultrasonic Sensor: PIN 4
# Left Color Senror: PIN 1
# Right Color Sensor: PIN 2
# Left Motor: PIN A
# Right Motor: PIN B

car = FoobotDrive(4.7, 11.4, 3/5, 70, 20)
cs = FoobotColorSensor()
us = FoobotUltrasonicSensor()

loop = True

us_distance = -1

cs_left_reading = []
cs_right_reading = []

cs_left_rgb = [-1, -1, -1]
cs_right_rgb = [-1, -1, -1]

cs_left_mode = 'rgb'
cs_right_mode = 'rgb'

def t_cs_left():
    global cs_left_mode, cs_left_reading, cs_left_rgb
    while loop:
        if cs_left_mode == 'rgb':
            cs_left_rgb = cs.rgb_left()
        if cs_left_mode == 'ambient':
            cs_left_reading = cs.ambient_left()
        sleep(0.2);

cs_left_thread = Thread(target = t_cs_left)

def t_cs_right():
    global cs_right_mode, cs_right_reading, cs_right_rgb
    while loop:
        if cs_right_mode == 'rgb':
            cs_right_rgb = cs.rgb_right()
        if cs_left_mode == 'ambient':
            cs_left_reading = cs.ambient_right()
        sleep(0.2);
cs_right_thread = Thread(target = t_cs_right)

def t_us():
    global us_distance
    while loop:
        us_distance = us.distance()
        sleep(0.2);

us_thread = Thread(target = t_us)

def t_log():
    global us_distance, cs_left_rgb, cs_right_rgb
    while loop:
        print(','.join(str(x) for x in cs_left_rgb))
        print(','.join(str(x) for x in cs_right_rgb))
        print(us_distance)
        sleep(0.5);

log_thread = Thread(target = t_log)

def init_telemetrics(show_log = True):
    cs_left_thread.start()
    cs_right_thread.start()
    us_thread.start()

    if show_log == True:
        log_thread.start()

init_telemetrics(show_log = False)

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
                self.car.run()
        self.car.stop()

    def stop(self):
        self.car.stop()
