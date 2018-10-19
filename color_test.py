from color_sensor import FoobotColorSensor

color_sensor = FoobotColorSensor()

print("color")
print(color_sensor.color_left())
print("intensity")
print(color_sensor.intensity_left())
print("ambient")
print(color_sensor.ambient_left())
print("rgb")
print(color_sensor.rgb_left())
