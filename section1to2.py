from main import car, cs_left_rgb, cs_right_rgb, start_telemetrics
import startToChallengeOne


start_telemetrics()

#turn left slowly until right sensor crosses on to yellow, then we know bot is aligned
def first_orange_crossing():
    global cs_left_rgb, cs_right_rgb
    while not orangeColorDetected(cs_right_rgb):
        car.turn_left(5)
    
    while orangeColorDetected(cs_right_rgb):
        car.move_straigth(5)
    
    

    