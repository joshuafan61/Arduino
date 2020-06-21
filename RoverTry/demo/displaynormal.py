import time
import math
import Tkinter as tk
from random import randrange
import serial, string, time
import MySQLdb

# Import library
import multilineMAX7219 as LEDMatrix
# Import fonts
from multilineMAX7219_fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT

# The following imported variables make it easier to feed parameters to the library functions
from multilineMAX7219 import DIR_L, DIR_R, DIR_U, DIR_D
from multilineMAX7219 import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from multilineMAX7219 import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT

# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=1)
db = MySQLdb.connect("localhost", "root", "104403011","sensorData")
cur = db.cursor()
cur.execute("SELECT mq2,mq7,mq131,mq135,mq136,pm1,pm25,pm10 FROM sensorData.systemdata")

def warn():
    a = 0
    b = 1
    sad=[[b,b,b,b,b,b,b,b],[b,a,b,b,b,b,b,b],[b,b,a,b,b,a,b,b],[b,b,a,b,b,b,b,b],[b,b,a,b,b,b,b,b],[b,b,a,b,b,a,b,b],[b,a,b,b,b,b,b,b],[b,b,b,b,b,b,b,b]]
    LEDMatrix.gfx_sprite_array(sad, start_x=0, start_y=0, state=GFX_INVERT)
    LEDMatrix.gfx_scroll_towards(new_graphic=GFX_OFF, repeats=3, speed=5, direction=DIR_L, finish=True)
    LEDMatrix.gfx_render()
    LEDMatrix.gfx_render()
    LEDMatrix.gfx_render()
    time.sleep(1)
    LEDMatrix.clear_all()    
    LEDMatrix.scroll_message_horiz(["warning"], 1, 5)
    while True:
        for row in cur.fetchall():
	    mq2 = str(row[0])
	    mq7 = str(row[1])
	    mq131 = str(row[2])
	    mq135 = str(row[3])
	    mq136 = str(row[4])
	    pm1 = str(row[5])
	    pm25 = str(row[6])
	    pm10 = str(row[7])
	    print(mq2)
	    print(mq7)
	    print(mq131)
	    print(mq135)
	    print(mq136)
	    
	    LEDMatrix.scroll_message_horiz(["LPG: 2100"], 1, 5)
            time.sleep(1)
            LEDMatrix.clear_all()    

def normal():
    # Display a stationary message
    a = 1
    b = 0
        ##happy=[[0,0,1,1,1,1,0,0],[0,1,0,1,0,0,1,0],[1,0,1,0,0,1,0,1],[1,0,1,0,0,0,0,1],[1,0,1,0,0,0,0,1],[1,0,1,0,0,1,0,1],[0,1,0,1,0,0,1,0],[0,0,1,1,1,1,0,0]]
    happy=[[b,b,b,b,b,b,b,b],[b,b,a,b,b,b,b,b],[b,a,b,b,b,a,b,b],[b,a,b,b,b,b,b,b],[b,a,b,b,b,b,b,b],[b,a,b,b,b,a,b,b],[b,b,a,b,b,b,b,b],[b,b,b,b,b,b,b,b]]
    LEDMatrix.gfx_sprite_array(happy, start_x=0, start_y=0, state=GFX_INVERT)
    LEDMatrix.gfx_scroll_towards(new_graphic=GFX_OFF, repeats=3, speed=5, direction=DIR_L, finish=True)
    LEDMatrix.gfx_render()
    time.sleep(1)
    LEDMatrix.clear_all()    
    while True:
        for row in cur.fetchall():
	    mq2 = str(row[0])
	    mq7 = str(row[1])
	    mq131 = str(row[2])
	    mq135 = str(row[3])
	    mq136 = str(row[4])
	    pm1 = str(row[5])
	    pm25 = str(row[6])
	    pm10 = str(row[7])
	    print(mq2)
	    print(mq7)
	    print(mq131)
	    print(mq135)
	    print(mq136)
	    
	    LEDMatrix.scroll_message_horiz(["LPG: "+mq2], 1, 5)
	    LEDMatrix.scroll_message_horiz(["CO: "+mq7], 1, 5)
	    LEDMatrix.scroll_message_horiz(["NOx: "+mq131], 1, 5)
	    LEDMatrix.scroll_message_horiz(["HAZ: "+mq135], 1, 5)
	    LEDMatrix.scroll_message_horiz(["H2S: "+mq136], 1, 5)
	    LEDMatrix.scroll_message_horiz(["PM1.0: "+pm1], 1, 5)
	    LEDMatrix.scroll_message_horiz(["PM2.5: "+pm25], 1, 5)
	    LEDMatrix.scroll_message_horiz(["PM10: "+pm10], 1, 5)
            time.sleep(1)
            LEDMatrix.clear_all()
        
try:
    normal()
except KeyboardInterrupt:
    # reset array
    LEDMatrix.scroll_message_horiz(["Goodbye!"], 1, 6)
    LEDMatrix.clear_all()
