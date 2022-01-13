"""CircuitPython Essentials Digital In Out example"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.LCD_BCKL)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.IO0)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        led.value = True
    else:
        led.value = False

    time.sleep(0.01)  # debounce delay