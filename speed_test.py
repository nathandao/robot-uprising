from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

wheel_circ = 3.14 * 5.6
forward_distance = 150
left_distance = 100

rotations1 = 150 / wheel_circ
rotations2 = 100 / wheel_circ

ms = MoveTank(OUTPUT_A, OUTPUT_B)
ms.on_for_rotations(75, 75, rotations1)

ms.on_for_degrees(-50, 50, 90)

ms.on_for_rotations(75, 75, rotations2)

