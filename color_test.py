from foobot.color_sensor import FoobotColorSensor

color_sensor = FoobotColorSensor()

while True:
    side = input('left, right: ')
    m = input('color , intensity, ambient, rgb: ')
    if m == 'color':
        while True:
            if side == 'left':
                print(color_sensor.color_left())
            else:
                print(color_sensor.color_right())

    if m == 'intensity':
        while True:
            if side == 'left':
                print(color_sensor.intensity_left())
            else:
                print(color_sensor.intensity_right())

    if m == 'ambient':
        while True:
            if side == 'left':
                print(color_sensor.intensity_left())
            else:
                print(color_sensor.intensity_right())

    if m == 'rgd':
        while True:
            if side == 'left':
                print(','.join(str(x) for x in color_sensor.rgb_left()))
            else:
                print(','.join(str(x) for x in color_sensor.rgb_right()))

# print(color_sensor.color_left())
# print("intensity")
# print(color_sensor.intensity_left())
# print("ambient")
# print(color_sensor.ambient_left())
# print("rgb")
# print(','.join(str(x) for x in color_sensor.rgb_left()))

# print(color_sensor.color_right())
# print("intensity")
# print(color_sensor.intensity_right())
# print("ambient")
# print(color_sensor.ambient_right())
# print("rgb")
# print(','.join(str(x) for x in color_sensor.rgb_right()))
