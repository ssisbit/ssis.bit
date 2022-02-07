# blink three times at startup on blackpill

import time
import board
import digitalio
import microcontroller

led = digitalio.DigitalInOut(board.C13)
led.direction = digitalio.Direction.OUTPUT

for x in range(0, 3):
    led.value = False
    time.sleep(0.2)
    led.value = True
    time.sleep(0.2)

print("This is a Blackpill, running at {:.1f} MHz".format(float(microcontroller.cpu.frequency)/1000000))
print("The CPU has a temperature of {:.1f} °C.".format(microcontroller.cpu.temperature))
