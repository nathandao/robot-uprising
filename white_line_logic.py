class WhiteLineFollower:
    def __init__(self, car, color_sensor):
        self.car = car
        self.color_sensor = color_sensor

    def isValueBetween(self, min, max, value):
        if value < min and value > max:
            return True
        return False

    def is_it_white(self, rbg):
        if rbg[0] > 200 and rgb[1] > 200 and rgb[2] > 200:
            return True
        return False

    def is_it_yellow(self, rbg):
        if self.isValueBetween(140, 160, rbg[0]) and self.isValueBetween(140, 160, rbg[1]) and self.isValueBetween(50, 70, rbg[2]):
            return True
        return False

    def run(self):
        while True:
            if self.is_it_white(self.color_sensor.rgb_left()):
                self.car.turn_left()
            elif self.is_it_white(self.color_sensor.rgb_right()):
                self.car.turn_right()
            else:
                self.car.run()
        self.car.stop()

    def stop(self):
        self.car.stop()
