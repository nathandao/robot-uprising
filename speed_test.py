from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering

wheel_circ = 3.14 * 5.6
forward_distance = 20
left_distance = 10

rotations1 = 150 / wheel_circ
rotations2 = 100 / wheel_circ

mt = MoveSteering(OUTPUT_A, OUTPUT_B)
ms = MoveTank(OUTPUT_A, OUTPUT_B)

ms.on_for_rotations(75, 75, rotations1)
mt.on_for_rotations(-20, SpeedPercent(75), 10)
ms.on_for_rotations(75, 75, rotations2)

