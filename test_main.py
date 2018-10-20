from threading import Thread
from main import us_distance, init_telemetrics

init_telemetrics()

def test_t():
    global us_distance
    print('DISTANCE=======', us_distance)

t = Thread(test_t)
t.start()
