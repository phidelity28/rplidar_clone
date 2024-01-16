from adafruit_rplidar import RPLidar
import os
from math import floor
from busio import UART

# for use with serial port usb
# PORT_NAME  = '/dev/ttyUSB0'

# attempt with our uart
uart = busio.UART(2,)

lidar = RPLidar('/dev/ttyUSB0')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

for i, scan in enumerate(lidar.iter_scans()):
    print('%d: Got %d measurments' % (i, len(scan)))
    if i > 10:
        break

lidar.stop()
lidar.stop_motor()
lidar.disconnect()