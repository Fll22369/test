

from ev3dev2.motor import Motor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, SpeedRPM
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor, InfraredSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.wheel import EV3Tire

s = Sound()
left = LargeMotor(OUTPUT_C)
right = LargeMotor(OUTPUT_B)

s.speak('beep')
