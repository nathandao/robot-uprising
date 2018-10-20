from threading import Thread
from time import sleep

from foobot.drive import FoobotDrive
from foobot.color_sensor import FoobotColorSensor
from foobot.ultrasonic_sensor import FoobotUltrasonicSensor

# Initializing components and ports:
#
# Ultrasonic Sensor: PIN 4
# Left Color Senror: PIN 1
# Right Color Sensor: PIN 2
# Left Motor: PIN A
# Right Motor: PIN B


car = FoobotDrive(3.7, 10.5, 3/5, 70, 20)
cs = FoobotColorSensor()
us = FoobotUltrasonicSensor()

loop = True

us_distance = -1

cs_left_rgb = []
cs_right_rgb = []

cs_left_rgb = [-1, -1, -1]
cs_right_rgb = [-1, -1, -1]
cs_left_mode = 'rgb'
cs_right_mode = 'rgb'

def t_cs_left():
    global cs_left_mode
    global cs_left_reading
    while loop:
        if cs_left_mode == 'rgb':
            cs_left_reading = cs.rgb_left()
        if cs_left_mode == 'ambient':
            cs_left_reading = cs.ambient_left()

cs_left_thread = Thread(target = t_cs_left)

def t_cs_right():
    global cs_right_mode
    global cs_right_reading
    while loop:
        if cs_right_mode == 'rgb':
            cs_left_reading = cs.rgb_left()
        if cs_left_mode == 'ambient':
            cs_left_reading = cs.ambient_left()

cs_right_thread = Thread(target = t_cs_right)

def t_us():
    global us_distance
    while loop:
        us_distance = us.distance()

us_thread = Thread(target = t_us)

def t_log():
    global us_distance, cs_left_reading, cs_right_reading
    while loop:
        print(cs_left_reading(0))
        print(cs_left_reading(1))
        print(cs_left_reading(2))
        print(us_distance)
        sleep(0.5);

log_thread = Thread(target = t_log)

cs_left_thread.start()
cs_right_thread.start()
us_thread.start()
log_thread.start()
