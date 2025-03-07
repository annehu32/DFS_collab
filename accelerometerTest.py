from acceleration import Acceleration
from machine import Pin
import uasyncio as asyncio
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

# lights: helper function to change the neopixel color and speed
async def lights(color, delay):
    while True:
        if t.lightVal>0:
            for i in range(0, numPixel):
                pixel[i] = color
                pixel.write()
            await asyncio.sleep(delay)        
            for i in range(0, numPixel):
                pixel[i] = off
                pixel.write()
            await asyncio.sleep(delay)
        await asyncio.sleep(0.01)

async def main():

    while True:            
        accel = t.read_accel()
        print(accel)
        await asyncio.sleep(0.25)
    
# --- Running main ---
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.create_task(t.read_event())
loop.create_task(lights(purple, 0.1))
loop.create_task

try:
    loop.run_forever()

except KeyboardInterrupt:
    print("Exiting...")
