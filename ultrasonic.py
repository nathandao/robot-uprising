from foobot.ultrasonic_sensor import FoobotUltrasonicSensor

us = FoobotUltrasonicSensor()

while True:
    us.distance()
