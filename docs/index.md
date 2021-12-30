# ssis:bit
AIO microcomputer solution with CircuitPython, display and battery for SSIS students.

## Hardware

CircuitPython supports [more than 200 different boards](https://circuitpython.org/downloads). Locally available is the [TTGO T8 ESP32-S2 ST7789](https://circuitpython.org/board/lilygo_ttgo_t8_s2_st7789/) at several online stores. The board includes the powerful 240MHz CPU, 4MB Flash and 8MB PSRAM, a 1.14" ST7789 display, a microSD card slot for virtually unlimited local data storage, battery connector 1.25mm JST with charge controller and regular USB-C connector. And buildin WiFi, of course.

![LILYGO T8](T8.jpg)

The planned adapterplate adds a 3-way button for input, place to hold the little 350 mAh battery and interface for I2C with regular 2.54mm 4pin JST XH as well as the small Stemma QT 1mm JST SH connector (QWIIC).

## Software

<img src="circuitpython.png" align="right">

The ssis:bit runs [CircuitPython](https://circuitpython.org/) and can be easily programmed with the [Mu Editor](https://codewith.mu/en/). There is a lot to learn on [Adafruit with CircuitPython]() and with their great libraries there is less frustration getting things started.

## History

More will be updated in the [docs/history](docs/history.md) document, but the idea is from 2020 with the [t-display](https://github.com/kreier/t-display) board. Similar idea: Not just the Microcomputer but included power supply (LiPo), display (just 240x135 color) and input device (not keyboard, but 3 buttons) to have it always with you and ready to use.
