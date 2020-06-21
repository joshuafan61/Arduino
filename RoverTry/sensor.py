import RPi.GPIO as gpio
import time

##GPIO.setmode(GPIO.BCM)
##GPIO.setup(12, GPIO.OUT)
##GPIO.setup(16, GPIO.IN)
##def distance():
##	GPIO.output(12,False)
##	start = time.time()
##	while GPIO.input(16)==0:
##		start = time.time()
##	while GPIO.input(16)==1:
##		stop = time.time()
##	elapsed = stop - start
##	distance = elapsed * 34000
##	distance = distance / 2
##	return distance
##        GPIO.cleanup()
##print(distance())

def distance(measure='cm'):
    try:
        gpio.setmode(gpio.BCM)
        gpio.setup(12, gpio.OUT)
        gpio.setup(16, gpio.IN)

        gpio.output(12, False)
        while gpio.input(16) == 0:
            nosig = time.time()

        while gpio.input(16) == 1:
            sig = time.time()

        tl = sig - nosig

        if measure == 'cm':
            distance = tl / 0.000058
        elif measure == 'in':
            distance = tl/ 0.000148
        else:
            print('improper choice of measurement: in or cm')
            distance = None

        gpio.cleanup()
        return distance
    except:
        distance = 10
        gpio.cleanup()
        return distance

print(distance('cm'))
