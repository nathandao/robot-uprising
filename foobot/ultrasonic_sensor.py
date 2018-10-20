from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_4

class FoobotUltrasonicSensor:
    def __init__(self):
        self.sensor = UltrasonicSensor(INPUT_4)
        self.sensor.mode = 'US-DIST-CM'

    def distance(self):
        return self.sensor.distance_centimeters
