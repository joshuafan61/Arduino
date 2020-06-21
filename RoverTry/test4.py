import RPi.GPIO as GPIO
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
import time

GPIO.setmode(GPIO.BCM)

servposnum = 0
MOTOR_PIN = 2
GPIO.setup(MOTOR_PIN,GPIO.OUT)
pwm_motor = GPIO.PWM(MOTOR_PIN,50)
pwm_motor.start(7.5)

GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
start = False
counter = 0

GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

GPIO.setup(4,GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

def reset():
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)

def front_left_forward():
        GPIO.output(20, GPIO.HIGH) ##start
        GPIO.output(17, GPIO.HIGH) ##+
        GPIO.output(18, GPIO.LOW) ##-

def front_right_forward():
        GPIO.output(21, GPIO.HIGH) ##start
        GPIO.output(22, GPIO.HIGH) ##+
        GPIO.output(25, GPIO.LOW) ##-

def rear_left_forward():
        GPIO.output(4, GPIO.HIGH) ##start
        GPIO.output(6, GPIO.HIGH) ##+
        GPIO.output(13, GPIO.LOW) ##-

def rear_right_forward():
        GPIO.output(27, GPIO.HIGH) ##start
        GPIO.output(19, GPIO.HIGH) ##+
        GPIO.output(26, GPIO.LOW) ##-

def front_left_back():
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)

def front_right_back():
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)

def rear_left_back():
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)

def rear_right_back():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(26, GPIO.HIGH)

def forward():
        reset()
        front_left_forward()
        front_right_forward()
        rear_left_forward()
        rear_right_forward()

def back():
        reset()
        front_left_back()
        front_right_back()
        rear_left_back()
        rear_right_back()

def front_left_turn():
        reset()
        front_right_forward()
        rear_right_forward()
        front_left_back()
        rear_left_back()
        time.sleep(0.3)
        reset()

def front_right_turn():
        reset()
        front_left_forward()
        rear_left_forward()
        front_right_back()
        rear_right_back()
        time.sleep(0.3)
        reset()

def rear_left_turn():
        reset()
        rear_left_back()
        front_left_back()
        time.sleep(0.3)
        reset()

def rear_right_turn():
        reset()
        rear_right_back()
        front_right_back()
        time.sleep(0.3)
        reset()

def stop():
        reset()
        
def avoid():
        distance_1 = distance()
        while(distance_1 < 15):
            back()
            front_right_turn()
            distance_1 = distance()
        time.sleep(0.3)
        
def distance():
	GPIO.output(GPIO_TRIGGER,False)
	time.sleep(0.5)
	GPIO.output(GPIO_TRIGGER,True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER,False)
	start = time.time()
	while GPIO.input(GPIO_ECHO)==0:
		start = time.time()
	while GPIO.input(GPIO_ECHO)==1:
		stop = time.time()
	elapsed = stop - start
	distance = elapsed * 34000
	distance = distance / 2
	return distance

def car():
	distance_0 = distance()
##	global servposnum 
##	while(distance_0 > 15):
##		if(servposnum == 0):
##			pwm_motor.ChangeDutyCycle(7.5)
##			servposnum = 1
##			time.sleep(0.001)
##		elif(servposnum == 1):
##			pwm_motor.ChangeDutyCycle(10.5)
##			servposnum = 2
##			time.sleep(0.001)
##		elif(servposnum == 2):
##			pwm_motor.ChangeDutyCycle(7.5)
##			servposnum = 3
##			time.sleep(0.001)
##		elif(servposnum == 3):
##			pwm_motor.ChangeDutyCycle(4.5)
##			servposnum = 1
##			time.sleep(0.001)
        forward()		
        distance_0 = distance()
        print(distance_0)
	stop()

try:
	while True:
##		inputValue = GPIO.input(5)
##		if(inputValue == False):
##			counter += 1
##		if(counter > 0 and counter % 2 == 0):
##			start = True
##		elif(counter % 2 == 1):
##			start = False
	
		print('car starts')
		front_left_forward()
##		car()
##		avoid()
	
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('car stops')
finally:
	GPIO.cleanup()

