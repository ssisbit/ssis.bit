# ssis:bit

AIO microcomputer solution with CircuitPython, display and battery for SSIS students.

![T8 running CircuitPython](ssis.bit_2022-01-06.jpg)

## Hardware

CircuitPython supports [more than 200 different boards](https://circuitpython.org/downloads). Locally available is the [TTGO T8 ESP32-S2 ST7789](https://circuitpython.org/board/lilygo_ttgo_t8_s2_st7789/) at several online stores. The board includes the powerful 240MHz CPU, 4MB Flash and 8MB PSRAM, a 1.14" ST7789 display, a microSD card slot for virtually unlimited local data storage, battery connector 1.25mm JST with charge controller and regular USB-C connector. And buildin WiFi, of course.

![LILYGO T8](T8.jpg)

The planned adapterplate adds a 3-way button for input, place to hold the little 350 mAh battery and interface for I2C with regular 2.54mm 4pin JST XH as well as the small Stemma QT 1mm JST SH connector (QWIIC).

## Software

<img src="circuitpython.png" align="right">

The ssis:bit runs [CircuitPython](https://circuitpython.org/) and can be easily programmed with the [Mu Editor](https://codewith.mu/en/). There is a lot to learn on [Adafruit with CircuitPython]() and with their great libraries there is less frustration getting things started.

## GPIO

This document from LilyGO documents the pins of the T8.

![T8 pinmap](T8-pinmap.jpg)

In CircuitPython the following pins are available"

``` py
import board
dir(board)
['__class__', '__name__', 'BATTERY', 'DISPLAY', 'IO0', 'IO1', 'IO11', 'IO12', 'IO13', 'IO15', 'IO16', 'IO17', 'IO18', 'IO19', 'IO2', 'IO20', 'IO21', 'IO3', 'IO39', 'IO4', 'IO40', 'IO41', 'IO42', 'IO45', 'IO46', 'IO5', 'IO6', 'IO7', 'IO8', 'IO9', 'LCD_BCKL', 'LCD_CLK', 'LCD_CS', 'LCD_D_C', 'LCD_MOSI', 'LCD_RST', 'PE_POWER', 'RX', 'RX1', 'SD_CLK', 'SD_CS', 'SD_MISO', 'SD_MOSI', 'TX', 'TX1', 'board_id']
```

To find he assigned pins we running
```
"""CircuitPython Essentials Pin Map Script"""
import microcontroller
import board

board_pins = []
for pin in dir(microcontroller.pin):
    if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
        pins = []
        for alias in dir(board):
            if getattr(board, alias) is getattr(microcontroller.pin, pin):
                pins.append("board.{}".format(alias))
        if len(pins) > 0:
            board_pins.append(" ".join(pins))
for pins in sorted(board_pins):
    print(pins)
```

And get

```
board.BATTERY board.IO9
board.IO0
board.IO1
board.IO11 board.SD_MOSI
board.IO12 board.SD_CLK
board.IO13 board.SD_MISO
board.IO15
board.IO16
board.IO17 board.TX1
board.IO18 board.RX1
board.IO19
board.IO2
board.IO20
board.IO21
board.IO3
board.IO39
board.IO4
board.IO40
board.IO41
board.IO42
board.IO45
board.IO46
board.IO5
board.IO6
board.IO7
board.IO8
board.LCD_BCKL
board.LCD_CLK
board.LCD_CS
board.LCD_D_C
board.LCD_MOSI
board.LCD_RST
board.PE_POWER
board.RX
board.SD_CS
board.TX
```

## Installation

Connect your T8 ST7789 to a USB port of your computer and determine the port. You can do this by right-click on the Windows symbol > Device Manager > ports (COM & LPT) and there you'll find ```USB-SERIAL CH340 (COM5)```. Here COM5 would be your serial port. Open ```cmd``` or ```powershell``` and navigate to the folder with the esptool.exe and firmware.bin.

- Check your board with `esptool.exe --port COM5 flash_id`
- Erase the flash `esptool --port COM5 erase_flash`
- Flash the new firmware with `esptool.exe --port COM5 --baud 460800 write_flash -z 0x0 firmware.bin`

CircuitPython should now be running on your T8. Now you have to switch the USB-C port from the serial CH340 interface to the native USB interface of the ESP32-S2. Therefore you need to change the DIP switches on the bottom of the board:

![T8 ST7789 switch bottom](T8_USB_OTG.png)

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


## History

More will be updated in the [docs/history](./history) document, but the idea is from 2020 with the [t-display](https://github.com/kreier/t-display) board. Similar idea: Not just the Microcomputer but included power supply (LiPo), display (just 240x135 color) and input device (not keyboard, but 3 buttons) to have it always with you and ready to use.
