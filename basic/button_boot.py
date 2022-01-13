"""CircuitPython Essentials Digital In Out example"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.IO0)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        print("not pressed")
    else:
        print("Button pressed")

    time.sleep(1)  # debounce delay