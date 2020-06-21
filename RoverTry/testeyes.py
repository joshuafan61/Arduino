import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice

gpio.setmode(gpio.BCM)
servposnum = 0
MOTOR_PIN = 2
GPIO_TRIGGER = 23
GPIO_ECHO = 24
gpio.setup(4,gpio.OUT)
pwm_motor=gpio.PWM(4,50)
pwm_motor.start(7.5)
gpio.setup(23,gpio.OUT)
gpio.setup(24,gpio.IN)

def distance():
    gpio.output(23, False)
    time.sleep(0.5)
    gpio.output(23, True)
    time.sleep(0.00001)
    gpio.output(23, False)
    start = time.time()
    while gpio.input(24) == 0:
        start = time.time()
    while gpio.input(24) == 1:
        stop = time.time()
    elapsed = stop - start
    distance = elapsed * 34000
    distance = distance / 2
    return distance

try:
    while True:
        distance_0 = distance()
        if (distance_0 < 20):
            pwm_motor.ChangeDutyCycle(4.5)
            time.sleep(0.5)
            pwm_motor.ChangeDutyCycle(10.5)
            time.sleep(0.5)
        pwm_motor.ChangeDutyCycle(7.5)
        distance_0 = distance()
        print(distance_0)
except KeyboardInterrupt:
    gpio.cleanup()
