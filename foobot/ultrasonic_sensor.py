from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_4

class FoobotUltrasonicSensor:
    def __init__(self):
        self.name = 'ulra_sensor'
        self.sensor = UltrasonicSensor(INPUT_4)
        self.mode = 'US-DIST-CM'

    def distance(self):
        return sensor.value()
