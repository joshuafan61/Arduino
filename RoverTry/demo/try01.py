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
    gpio.output(13, False)##rear
    gpio.output(6, True)
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
    gpio.output(25, True)
    gpio.output(22, True)##differ from forward
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
    gpio.output(26, True)
    gpio.output(19, False)
    gpio.output(18, False)##front
    gpio.output(17, True)
    gpio.output(25, True)
    gpio.output(22, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    init()
    gpio.output(13, True)##rear
    gpio.output(6, False)
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(18, True)##front
    gpio.output(17, False)
    gpio.output(25, False)
    gpio.output(22, True)
    time.sleep(tf)
    gpio.cleanup()

def reset():
    init()
    gpio.output(13, False)##rear
    gpio.output(6, False)
    gpio.output(26, False)
    gpio.output(19, False)
    gpio.output(18, False)##front
    gpio.output(17, False)
    gpio.output(25, False)
    gpio.output(22, False)    

def distance():
    gpio.setmode(gpio.BCM)
    gpio.setup(23,gpio.OUT)
    gpio.setup(24,gpio.IN)
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

def avoid():
    gpio.setmode(gpio.BCM)
    distance_1 = distance()
    while(distance_1 < 15):
        reverse(1)
        pivot_right(1)
        distance_1 = distance()
    time.sleep(0.3)

def autoMove():
    distance_0 = distance()
    servposnum = 0
    while(distance_0 > 15):
	if(servposnum == 0):
	    pwm_motor.ChangeDutyCycle(7.5)
            servposnum = 1
            time.sleep(1)
	elif(servposnum == 1):
            pwm_motor.ChangeDutyCycle(10.5)
	    servposnum = 2
            time.sleep(1)
	elif(servposnum == 2):
            pwm_motor.ChangeDutyCycle(7.5)
            servposnum = 3
            time.sleep(1)
	elif(servposnum == 3):
            pwm_motor.ChangeDutyCycle(4.5)
            servposnum = 1
            time.sleep(1)
        forward(1)
        distance_0 = distance()
        print(distance_0)
    reset()

def key_input(event):
    #init()
    print 'KEY: ', event.char
    key_press = event.char
    sleep_time = 0.050

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    elif key_press.lower() == 'q':
        pivot_left(sleep_time)
    elif key_press.lower() == 'e':
        pivot_right(sleep_time)
    elif key_press.lower() == 'u':
        try:
            while True:
                print('car starts')
                autoMove()
                avoid()
                time.sleep(0.3)
        except KeyboardInterrupt:
            gpio.cleanup()
            print('car stops')

try:
    root = tk.Tk()
    root.bind('<KeyPress>', key_input)
    root.mainloop()
except KeyboardInterrupt:
    LEDMatrix.scroll_message_horiz(["Goodbye!"], 1, 6)
    LEDMatrix.clear_all()    
    gpio.cleanup()
