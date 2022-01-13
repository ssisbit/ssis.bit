# This test will initialize the display using displayio and draw a solid green
# background, a smaller purple rectangle, and some yellow text.

# adapted from https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout/circuitpython-displayio-quickstart

import time, random
import board, displayio, terminalio, digitalio
from adafruit_display_text import label

display = board.DISPLAY      # CP already sets up display for us, 240x135 for LILYGO T8 ESP32-S2
screen = displayio.Group()   # a main group that holds everything
display.show(screen)         # add main group to display

pin = digitalio.DigitalInOut(board.IO0)    # just to exit the program with the boot switch 
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

# First set some parameters used for shapes and text
BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0x00FF00  # Bright Green
FOREGROUND_COLOR = 0xAA0088  # Purple
TEXT_COLOR       = 0xFFFF00

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
screen.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(
    display.width - BORDER * 2, display.height - BORDER * 2, 1
)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
screen.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width // 2 - text_width // 2,
    y=display.height // 2,
)
text_group.append(text_area)  # Subgroup for text scaling
screen.append(text_group)

time.sleep(1)

while True:
    if not pin.value :
      time.sleep(0.1)
      while not pin.value:
        time.sleep(0.1)
      exec(open("menu.py").read())
    time.sleep(0.1)