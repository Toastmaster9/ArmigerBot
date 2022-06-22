# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time,board
import pwmio
from adafruit_motor import servo

#Set your servo and led objects. Make sure to set your pins for each one.
pwm = pwmio.PWMOut(board.A0, duty_cycle=2 ** 15, frequency=50)
led = pwmio.PWMOut(board.A1, frequency=5000, duty_cycle=32000)

#Make a servo object and tell it to use the pwm object we just declared.
my_servo = servo.Servo(pwm)

#Loop forever
while True:

    #Use this to control your servo
    for x in range(10,170,3):
        my_servo.angle=x
        time.sleep(0.04)
    for x in range(170,10,-3):
        my_servo.angle=x
        time.sleep(0.04)

    #Use this code to control your LED
    #for x in range(0,32000,1000):
    #    led.duty_cycle=x
    #    time.sleep(0.1)
    #for x in range(32000,0,-1000):
    #    led.duty_cycle=x
    #    time.sleep(0.1)


#Use this code to zero your servo!
my_servo.angle=90
time.sleep(200.0)
