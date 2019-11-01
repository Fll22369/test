#!/usr/bin/env pybricks-micropython


from ev3dev2.motor import Motor, OUTPUT_B

m = Motor(OUTPUT_B)

m.on_for_seconds(10,1000)
