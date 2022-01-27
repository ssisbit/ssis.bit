import os
import time
import board
import busio
import sdcardio
import storage

spi = busio.SPI(board.SD_CLK, MOSI=board.SD_MOSI, MISO=board.SD_MISO)
sd = sdcardio.SDCard(spi, board.SD_CS)
vfs = storage.VfsFat(sd)
storage.mount(vfs, '/sd')
os.listdir('/sd')

time.sleep(10)
