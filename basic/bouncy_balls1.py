# bouncy_balls1.py - use displayio to make simple bounch balls
# 20 Jul 2021 - @todbot
import time, random
import board, displayio, terminalio
from adafruit_display_text import label
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect

display = board.DISPLAY  # CP already sets up display for us, 240x135 for LILYGO T8 ESP32-S2
screen = displayio.Group()  # a main group that holds everything
display.show(screen) # add main group to display

background = Rect(0,0, display.width, display.height, fill=0x000000 ) # background color
screen.append(background)
hello_lbl = label.Label(terminalio.FONT, text="Hello\nWorld!", color=0xffffff,
                        anchored_position=(display.width//2, display.height//2),
                        anchor_point=(0.5,0.5) ) 
screen.append(hello_lbl)

num_balls = 20
balls = displayio.Group() # group of balls
vees = []  # array of velocities for each ball
for i in range(num_balls):
    fill = random.randint(0,0xffffff) # random color
    b = Circle(display.width//2,display.height//2, 10, fill=fill, outline=0,stroke=1)
    v = [random.randint(-3,3), random.randint(-3,3)] # random initial velocity
    vees.append(v)
    balls.append(b)
screen.append(balls)  # add ball group to screen
while True:
    for i in range(len(balls)):
        b = balls[i] # get a ball
        v = vees[i]  # get its velocity
        b.x = int(b.x + v[0]) # update ball position
        b.y = int(b.y + v[1]) # update ball position
        # if ball hits edge, bounce it off by reflecting velocity
        if b.x <= 0 or b.x > display.width: v[0] = -v[0] + random.random()-0.5
        if b.y <= 0 or b.y > display.height: v[1] = -v[1] + random.random()-0.5
    time.sleep(0.01)
