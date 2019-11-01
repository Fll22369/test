#!/usr/bin/env pybricks-micropython

from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

tank_pair.on_for_rotations(-20, SpeedPercent(75), 10)