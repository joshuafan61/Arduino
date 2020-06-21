import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(26, gpio.OUT)
    gpio.setup(19, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.setup(25, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(17, gpio.OUT)

def reverse(tf):
    init()
    gpio.output(13, True)##rear
    gpio.output(6, False)
    gpio.output(26, True)
    gpio.output(19, False)
    gpio.output(18, True)##front
    gpio.output(17, False)
    gpio.output(25, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()

def forward(tf):
    init()
    gpio.output(13, gpio.LOW)##rear
    gpio.output(6, gpio.HIGH)
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(18, False)##front
    gpio.output(17, True)
    gpio.output(25, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    init()
    gpio.output(13, False)##rear
    gpio.output(6, True)
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(18, False)##front
    gpio.output(17, True)
    gpio.output(25, False)
    gpio.output(22, False)##differ from forward
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    init()
    gpio.output(13, False)##rear
    gpio.output(6, True)
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(18, False)##front
    gpio.output(17, False)##differ from forward
    gpio.output(25, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    init()
    gpio.output(13, False)##rear
    gpio.output(6, True)
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(18, False)##front
    gpio.output(17, True)
    gpio.output(25, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    init()
    gpio.output(13, False)##rear
    gpio.output(6, True)
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(18, True)##front
    gpio.output(17, False)
    gpio.output(25, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()
    
forward(3)
