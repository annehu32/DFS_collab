from machine import Pin
import time
import neopixel

## -----  Neopixel setup ---
numPixel = 3
pixel = neopixel.NeoPixel(Pin(0), numPixel)

# defining color combinations for neopixels
purple = (55,0,200)
teal = (0, 255, 50)
off = (0,0,0)

for i in range(0, numPixel):
    pixel[i] = purple
    pixel.write()
    time.sleep(0.5)        

for i in range(0, numPixel):
    pixel[i] = off
    pixel.write()
    time.sleep(0.5)
