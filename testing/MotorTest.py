#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks import ev3dev2
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, MoveTank,SpeedPercent, follow_for_ms, MoveDifferential, SpeedRPM

# Write your program here
brick.sound.beep()

Tank_Drive = MoveTank(OUTPUT_C, OUTPUT_B)

brick.sound.beep()

Tank_Drive.on_for_rotations(100, 100, 3000)

brick.sound.beep()