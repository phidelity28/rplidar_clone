from adafruit_rplidar import RPLidar
import os
from math import floor
import gpiozero as gp
import busio as bu

# for use with serial port usb
PORT_NAME  = '/dev/ttyUSB0'

# attempt with our uart  this through an error as I was attempting to configure the tx rx ports 
gp_transmit = gp.DigitalOutputDevice(14) #  gpio / BCM numbering defualt tx pin
gp_receive = gp.DigitalInputDevice(15) # default /Bcm rx pin
baud_rate = 115200
uart = bu.UART(rx = gp_transmit, tx = gp_receive, baudrate = baud_rate)
lidar = RPLidar(uart)

#PORT_NAME = '/dev/ttyUSB0'

#lidar = RPLidar('/dev/ttyUSB0')
#lidar = RPLidar(None, PORT_NAME, timeout=3 )

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