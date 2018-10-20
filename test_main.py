from threading import Thread
from main import init_telemetrics, loop

init_telemetrics()

def test_t():
    global us_distance
    while loop:
        print('DISTANCE=======', us_distance)

t = Thread(target=test_t)
t.start()
