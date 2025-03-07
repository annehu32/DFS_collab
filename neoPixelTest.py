from machine import Pin
import neopixel
import time

numPixel = 150

pixel = neopixel.NeoPixel(Pin(0), numPixel)

purple = (55,0,200)
teal = (0, 255, 50)
off = (0,0,0)


while True:
    for i in range(0,numPixel):
        pixel[i] = purple
        pixel.write()

    time.sleep(1)

    for i in range(0,numPixel):
        pixel[i] = off
        pixel.write()
        
    time.sleep(1)
    
    for i in range(0, numPixel):
        pixel[i] = teal
        pixel.write()
        
    time.sleep(1)

    for i in range(0,numPixel):
        pixel[i] = off
        pixel.write()

