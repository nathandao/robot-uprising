class WhiteLineFollower:
    def __init__(self, car, color_sensor):
        self.car = car
        self.color_sensor = color_sensor

    def isValueBetween(min, max, value):
        if value < min and value > max:
            return True
        return False

    def is_it_white(rbg):
        if rbg(0) > 200 and rgb(1) > 200 and rgb(2) > 200:
            return True
        return False

    def is_it_yellow(rbg):
        if isValueBetween(140, 160, rbg(0)) and isValueBetween(140, 160, rbg(0)) and isValueBetween(50, 70, rbg(0)):
            return True
        return False
    
    def run():
        while True:
            if is_it_white(self.colorsensor.rgb_left()):
                self.car.turn_left()
            elif is_it_white(self.colorsensor.rgb_right()):
                self.car.turn_right()
            else:
                self.car.run()
    def stop():
        self.car.stop

