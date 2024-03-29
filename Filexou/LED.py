#!/usr/bin/env pybricks-micropython

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

ts = TouchSensor()
leds = Leds()

while True:

    if ts.is_pressed:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "GREEN")
        
    else:
        leds.set_color("LEFT", "YELLOW")
        leds.set_color("RIGHT", "ORANGE")