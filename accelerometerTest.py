from acceleration import Acceleration
from machine import Pin
import time
import neopixel

# --- Accelerometer setup ---
scl = Pin('GPIO27', Pin.OUT)
sda = Pin('GPIO26', Pin.OUT)
t = Acceleration(scl, sda)
last = 0

## -----  Neopixel setup ---
numPixel = 150
pixel = neopixel.NeoPixel(Pin(0), numPixel)

# defining color combinations for neopixels
purple = (55,0,200)
teal = (0, 255, 50)
off = (0,0,0)

while True:
    accel = t.read_accel()
    print(accel)
    
    if accel > last * 1.5:
        print("--- Triggering positive acceleration case ---")
        for i in range(0,numPixel):
            pixel[i] = purple
            pixel.write()
        
    
    time.sleep(0.25)
