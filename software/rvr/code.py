# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_bno055
import busio

SCL = board.IO1
SDA = board.IO2

i2c = busio.I2C(SCL, SDA)


sensor = adafruit_bno055.BNO055_I2C(i2c)

# If you are going to use UART uncomment these lines
# uart = board.UART()
# sensor = adafruit_bno055.BNO055_UART(uart)


while True:
    print("Temperature: {} degrees C".format(sensor.temperature))
    """
    print(
        "Temperature: {} degrees C".format(temperature())
    )  # Uncomment if using a Raspberry Pi
    """
    # Measures the temperature of the chip in degrees Celsius.

    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
    #Gives the raw accelerometer readings, in m/s. Returns an empty tuple of length 3 when this property has been disabled by the current mode.

    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    #Gives the raw magnetometer readings in microteslas. Returns an empty tuple of length 3 when this property has been disabled by the current mode.

    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
    #Gives the raw gyroscope reading in radians per second. Returns an empty tuple of length 3 when this property has been disabled by the current mode.

    print("Euler angle: {}".format(sensor.euler))
    #Gives the calculated orientation angles, in degrees. Returns an empty tuple of length 3 when this property has been disabled by the current mode.

    print("Quaternion: {}".format(sensor.quaternion))
    #Gives the calculated orientation as a quaternion. Returns an empty tuple of length 3 when this property has been disabled by the current mode.

    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
    #Returns the linear acceleration, without gravity, in m/s. Returns an empty tuple of length 3 when this property has been disabled by the current mode.

    print("Gravity (m/s^2): {}".format(sensor.gravity))
    #Returns the gravity vector, without acceleration in m/s. Returns an empty tuple of length 3 when this property has been disabled by the current mode.

    print()

    time.sleep(1.0)
