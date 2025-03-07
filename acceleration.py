from machine import I2C, Pin
import struct
import uasyncio as asyncio
import math

class Acceleration():
    def __init__(self, scl, sda, addr = 0x62):
        self.addr = addr
        self.i2c = I2C(1,scl=scl, sda=sda, freq=100000) 
        self.connected = False
        if self.is_connected():
            print('connected')
            self.write_byte(0x11,0) #start data stream
        self.lightVal = 0 # will be used as a flag variable

    def is_connected(self):
        options = self.i2c.scan() 
        print(options)
        self.connected = self.addr in options
        return self.connected 
            
    async def read_accel(self):
        buffer = self.i2c.readfrom_mem(self.addr, 0x02, 6) # read 6 bytes starting at memory address 2
        await asyncio.sleep(0.01)
        return struct.unpack('<hhh',buffer)

    def write_byte(self, cmd, value):
        self.i2c.writeto_mem(self.addr, cmd, value.to_bytes(1,'little'))
        
    async def read_event(self):
        last = 0
        while True:
            try:
                data = await self.read_accel()
                xMag = data[1]
                print("X data: "+str(xMag))
                await asyncio.sleep(0.01)
            
                if xMag > last*1.5:
                    print(str(xMag)+": increasing magnitude")
                    self.lightVal = xMag
                    await asyncio.sleep(0.3)
                last = xMag
                print(str(self.lightVal))
                    
            except Exception as e:
                print(f"Error in read_event: {e}")
                
            await asyncio.sleep(0.1)
        
    
    

