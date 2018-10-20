import signal
from xbox360controller import Xbox360Controller


def on_button_pressed(button):
    print('Button {0} was pressed'.format(button.name))


def on_button_released(button):
    print('Button {0} was released'.format(button.name))


def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))

try:
    with Xbox360Controller(0, axis_threshold=0.2) as controller:
        # Button A events
        controller.button_a.when_pressed = on_button_pressed
        controller.button_a.when_released = on_button_released

        #Button b pressed
        controller.button_b.when_pressed = on_button_pressed
        controller.button_b.when_released = on_button_released


        #Button x pressed
        controller.button_x.when_pressed = on_button_pressed
        controller.button_x.when_released = on_button_released

        #Button y pressed
        controller.button_y.when_pressed = on_button_pressed
        controller.button_y.when_released = on_button_released

            
        signal.pause()
except KeyboardInterrupt:
    pass    