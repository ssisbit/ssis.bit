import struct
import time
import board
import displayio
import rtc
import socketpool
import terminalio
import wifi
from adafruit_display_text import label

try:
  from secrets import secrets
except ImportError:
  print("WiFi secrets are kept in secrets.py, please add them there!")
  raise

TZ_OFFSET = 3600
NTP_SERVER = "pool.ntp.org"
NTP_PORT = 123

def get_ntp_time(pool):
  packet = bytearray(48)
  packet[0] = 0b00100011

  for i in range(1, len(packet)):
    packet[i] = 0

  with pool.socket(pool.AF_INET, pool.SOCK_DGRAM) as sock:
    sock.sendto(packet, (NTP_SERVER, NTP_PORT))
    sock.recvfrom_into(packet)
    destination = time.monotonic_ns()

  seconds = struct.unpack_from("!I", packet, offset=len(packet) - 8)[0]
  monotonic_start = seconds - 2_208_988_800 - (destination // 1_000_000_000)
  return time.localtime(time.monotonic_ns() // 1_000_000_000 + monotonic_start + TZ_OFFSET)

BORDER = 10
FONTSCALE = 3
BACKGROUND_COLOR = 0x0e1115
FOREGROUND_COLOR = 0x0f1929
TEXT_COLOR = 0xd257ff

def init_ui(display):
  splash = displayio.Group()
  display.show(splash)

  color_bitmap = displayio.Bitmap(display.width, display.height, 1)
  color_palette = displayio.Palette(1)
  color_palette[0] = BACKGROUND_COLOR

  bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
  splash.append(bg_sprite)

  # Draw a smaller inner rectangle
  inner_bitmap = displayio.Bitmap(display.width - BORDER * 2, display.height - BORDER * 2, 1)
  inner_palette = displayio.Palette(1)
  inner_palette[0] = FOREGROUND_COLOR
  inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
  splash.append(inner_sprite)

  text_label = label.Label(terminalio.FONT, color=TEXT_COLOR, text="Starting", anchor_point=(0.5, 0.5))
  text_width = text_label.bounding_box[2] * FONTSCALE
  text_group = displayio.Group(
      scale=FONTSCALE,
      x=display.width // 2 - text_width // 2,
      y=display.height // 2,
  )
  text_group.append(text_label)
  splash.append(text_group)

  return text_label

def update_time(text_label):
  now = time.localtime()
  text_label.text = "%02.d:%02.d:%02.d" % (now.tm_hour, now.tm_min, now.tm_sec)

display = board.DISPLAY
text_label = init_ui(display)
update_time(text_label)

print("Connecting to ", secrets["ssid"])
wifi.radio.connect(ssid=secrets["ssid"], password=secrets["password"])
print("Connected with IP ", wifi.radio.ipv4_address)
text_label.text = "Connected"

pool = socketpool.SocketPool(wifi.radio)
now = get_ntp_time(pool)
rtc.RTC().datetime = now
print("Synced with NTP")
text_label.text = "Synced"
time.sleep(1.0)

while True:
  update_time(text_label)
  time.sleep(1.0)