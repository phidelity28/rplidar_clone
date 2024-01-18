import os
from math import floor
from adafruit_rplidar import RPLidar
import board
import digitalio
import machine


# motor pin: GPIO13
# TX: GPIO14
# RX: GPIO15       
# port: /dev/ttyS0     
class UART(machine.UART):
    def flushInput(self):
        self.flush()

uart = UART(rx=board.GPIO15,
        tx=board.GPIO14,
        # we can probably pass CTS as well, that's the motor drive pin, bu ti don't  know if we need to
        # cts=board.GPIO13
        bits=7,
        baudrate=115200,
        )        
motor_pin = digitalio.DigitalInOut(board.GPIO13)
lidar = RPLidar(motor_pin,uart, timeout=3)


# Setup the RPLidar
# PORT_NAME = '/dev/ttyUSB0'
# lidar = RPLidar(None, PORT_NAME, timeout=3)

# used to scale data to fit on the screen
max_distance = 0

def process_data(data):
    print(data)

scan_data = [0]*360

try:
#    print(lidar.get_info())
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance
        process_data(scan_data)

except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()