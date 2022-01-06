# ssis:bit

AIO solution for SSIS students

## Hardware

CircuitPython supports [more than 200 different boards](https://circuitpython.org/downloads). Locally available is the [TTGO T8 ESP32-S2 ST7789](https://circuitpython.org/board/lilygo_ttgo_t8_s2_st7789/) at several online stores. The board includes the powerful 240MHz CPU, 4MB Flash and 8MB PSRAM, a 1.14" ST7789 display, a microSD card slot for virtually unlimited local data storage, battery connector 1.25mm JST with charge controller and regular USB-C connector. And buildin WiFi, of course.

![LILYGO T8](T8.jpg)

The planned adapterplate adds a 3-way button for input, place to hold the little 350 mAh battery and interface for I2C with regular 2.54mm 4pin JST XH as well as the small Stemma QT 1mm JST SH connector (QWIIC).

## Software

<img src="circuitpython.png" align="right">

The ssis:bit runs [CircuitPython](https://circuitpython.org/) and can be easily programmed with the [Mu Editor](https://codewith.mu/en/). There is a lot to learn on [Adafruit with CircuitPython]() and with their great libraries there is less frustration getting things started.

## History

More will be updated in the [docs/history](docs/history.md) document, but the idea is from 2020 with the [T-Display](https://krier.github.io/t-display) board. Similar idea: Not just the Microcomputer but included power supply (LiPo), display (just 240x135 color) and input device (not keyboard, but 3 buttons) to have it always with you and ready to use.

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


## 2022

Please update.

## 2021

Start of development of the ssis:bit project based on CircuitPython and the T8 ST7789 from Lilygo.

![T8 running CircuitPython](ssis.bit_2022-01-06.jpg)

## 2020

The idea is born with a T-Display. But to control the display you need a fast ST7789 library, needs to be integrated into the binary of MicroPython. Feasable, but still not easy enouth for students.

## 2019

AISVN Robot car club - 10 students signed up! In 3 months we build our own robot cars that could be controlled with Bluetooth.

## 2018

ASA Arduino club at AIS.

## 2017

Visit to SSIS for the [VTC 2017](https://2017.vietnamtechconference.org/) Vietnam Tech Conference. Students presented their Arduino projects on Friday.

## 2016

It is not too complicated to connect a 20x4 LCD display and a barometric sensor to measure the artificial vacuum created at school with students from grade 4: [Video on YouTube](https://youtu.be/cFKzpqvAh60) down to [50 mBar](https://youtu.be/ohafJIDlITo). Didn't want to risk my Nexus 4 cellphone to measure the pressure inside.

## 2015

First experiences with Arduinos. The cheap copies from China with a different USB-to-serial interface (CH340) and needed installation of the driver made it accessable easily. Working with 5 Volt first projects were developed.