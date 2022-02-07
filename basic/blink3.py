# blink three times at startup on blackpill

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.C13)
led.direction = digitalio.Direction.OUTPUT

for x in range(0, 3):
    led.value = False
    time.sleep(0.2)
    led.value = True
    time.sleep(0.2)
