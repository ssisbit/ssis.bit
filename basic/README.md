# Basic programs in CircuitPython

## Hello world

This is simple and straight forward:

``` py
print('Hello World!')
```

## Prime numbers to 10000

This took 11375 ms on an esp32 with 160 MHz:

``` py
import math
import time

last = 10000

start = time.monotonic()
print('Prime numbers to {}'.format(last))

print('2, 3, 5, 7',end='')
for number in range(11, last, 2):
    prime = 1
    for divider in range(2, int(math.sqrt(number))+1, 1):
        if number/divider == int(number/divider):
            prime = 0

    if prime == 1:
        print(',', number,end='')
        
end = time.monotonic()
print('\nThis took:', (end - start), 'seconds.')
```

With text output in Mu it took the ESP32-S2 38.9 seconds. Commenting the print command in line 17 reduced the time to 13.3 seconds.

### Timings

| Frequency |  ESP8266 |   ESP32  | Raspberry Pi 1 | Raspberry Pi 4 |
|:---------:|:--------:|:--------:|:--------------:|:--------------:|
|    40 MHz |     -    | 44427 ms |                |                |
|    80 MHz | 32807 ms | 23323 ms |                |                |
|   160 MHz | 16113 ms | 11375 ms |                |                |
|   240 MHz |     -    |  7783 ms |                |                |
