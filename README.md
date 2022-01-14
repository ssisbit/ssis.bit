# ssis:bit
AIO solution for SSIS students

![T8 running CircuitPython](docs/ssis.bit_2022-01-06.jpg)

## Hardware

CircuitPython supports [more than 200 different boards](https://circuitpython.org/downloads). Locally available is the [TTGO T8 ESP32-S2 ST7789](https://circuitpython.org/board/lilygo_ttgo_t8_s2_st7789/) at several online stores. The board includes the powerful 240MHz CPU, 4MB Flash and 8MB PSRAM, a 1.14" ST7789 display, a microSD card slot for virtually unlimited local data storage, battery connector 1.25mm JST with charge controller and regular USB-C connector. And buildin WiFi, of course.

![LILYGO T8](docs/T8.jpg)

The planned adapterplate adds a 3-way button for input, place to hold the little 350 mAh battery and interface for I2C with regular 2.54mm 4pin JST XH as well as the small Stemma QT 1mm JST SH connector (QWIIC).

## Software

The ssis:bit runs [CircuitPython](https://circuitpython.org/) and can be easily programmed with the [Mu Editor](https://codewith.mu/en/). There is a lot to learn on [Adafruit with CircuitPython]() and with their great libraries there is less frustration getting things started.

## Motivation and History

More will be updated in the [docs/history](docs/history.md) document, but the idea is from 2020 with the [T-Display](https://github.com/kreier/t-display) board. Similar idea: Not just the Microcomputer but included power supply (LiPo), display (just 240x135 color) and input device (not keyboard, but 3 buttons) to have it always with you and ready to use.

A major challenge to get students use more of the microcomputers like Arduino, Raspberry Pi or micro:bit is the need for 3 more accessories to use them:

1. Input (keyboard, accelerometer, buttons, microphone)
2. Output (display, LEDs, matrix, beeper, serial back to PC)
3. Power supply (LiPo battery, AC adapter)

Some of these challenges are solved partially with the micro:bit - but limited in the end with just 2 buttons as input and a 5x5 red LED matrix as output. And the power adapter with 2 AAA batteries is not physically connected, making the solution less robust. Advantages with the Lilygo T8 ST7789:

1. AIO solution with 3 button input, 240x135 color display output and small LiPo battery
2. Standardaised QWIIC / STEMMA QT 1mm JST SH adapter for I2C sensors and IO
3. Standardised STEMMA 2mm GROVE 2mm JST PH connector
4. SD Card with GB of space for websites, data, images
5. WIFI build in to serve as an AP students can connect to, or to connect to the Internet
6. USB-C for charging and simple upload of programs to the CIRCUITPY folder
7. REPL - get starting programming right away!

## Installation

Connect your T8 ST7789 to a USB port of your computer and determine the port. You can do this by right-click on the Windows symbol > Device Manager > ports (COM & LPT) and there you'll find ```USB-SERIAL CH340 (COM5)```. Here COM5 would be your serial port. Open ```cmd``` or ```powershell``` and navigate to the folder with the esptool.exe and firmware.bin.

- Check your board with `esptool.exe --port COM5 flash_id`
- Erase the flash `esptool --port COM5 erase_flash`
- Flash the new firmware with `esptool.exe --port COM5 --baud 460800 write_flash -z 0x0 firmware.bin`

CircuitPython should now be running on your T8. Now you have to switch the USB-C port from the serial CH340 interface to the native USB interface of the ESP32-S2. Therefore you need to change the DIP switches on the bottom of the board:

![T8 ST7789 switch bottom](docs/T8_USB_OTG.png)

After that the board will be detected as a USB drive named "CIRCUITPY". You can just upload any program and it will reset the machine and start the code.py in the root folder.

``` py
Adafruit CircuitPython 7.1.0 on 2021-12-28; LILYGO TTGO T8 ESP32-S2 w/Display with ESP32S2
>>> 
```

Here you can directly try your first *hello_world*.

``` py
>>> print("Hello world!")
Hello world.
```

### Original sources with updates

First he have to obtain the two programs and the firmware.

#### esptool.py

The __esptool.py__ is the software provided by esp to upload the firmware to their SoCs. I got mine from the Arduino installation at the path `C:\Users\You\AppData\Local\Arduino15\packages\esp32\tools\esptool_py\2.6.1\ ` . You can download the latest version from github:

[https://github.com/espressif/esptool](https://github.com/espressif/esptool)

#### firmware

The latest MicroPython firmware for the ESP32 can be found on [micropython.org](https://micropython.org/download/esp32/). This firmware does not include a driver for the ST7789 display. You have several options to include the display library.
