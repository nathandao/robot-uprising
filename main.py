from threading import Thread
from time import sleep

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


car = FoobotDrive(3.7, 10.5, 3/5, 70, 20)
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
        sleep(0.1);

cs_left_thread = Thread(target = t_cs_left)

def t_cs_right():
    global cs_right_mode, cs_right_reading, cs_right_rgb
    while loop:
        if cs_right_mode == 'rgb':
            cs_right_rgb = cs.rgb_right()
        if cs_left_mode == 'ambient':
            cs_left_reading = cs.ambient_right()
        sleep(0.1);

cs_right_thread = Thread(target = t_cs_right)

def t_us():
    global us_distance
    while loop:
        us_distance = us.distance()
        sleep(0.1);

us_thread = Thread(target = t_us)

def t_log():
    global us_distance, cs_left_rgb, cs_right_rgb
    while loop:
        print(','.join(str(x) for x in cs_left_rgb))
        print(','.join(str(x) for x in cs_right_rgb))
        print(us_distance)
        sleep(0.5);

log_thread = Thread(target = t_log)

cs_left_thread.start()
cs_right_thread.start()
us_thread.start()

log_thread.start()

follow = WhiteLineFollower(car=car, color_sensor=cs)
follow.run()
