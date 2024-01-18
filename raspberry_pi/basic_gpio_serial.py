from ada_rplidar_serial import RPLidar
import os
from math import floor
import gpiozero as gp

import serial

# for use with serial port usb
PORT_NAME  = '/dev/ttyUSB0'

from time import sleep
output_5v = gp.DigitalOutputDevice(2) #the arg is the pinnumber not the io
motor_control_pwm = gp.DigitalOutputDevice(13)

# attempt with our uart  this through an error as I was attempting to configure the tx rx ports 
gp_transmit = gp.DigitalOutputDevice(14) #  gpio / BCM numbering defualt tx pin
gp_receive = gp.DigitalInputDevice(15) # default /Bcm rx pin

output_5v.on()
motor_control_pwm.on()

motor_pin = 13 #gpio labelling
baud_rate = 115200
port_serial = '/dev/ttyS0'
ser = serial.Serial(port=port_serial, baudrate=baud_rate, timeout=3)


lidar = RPLidar('13', port=ser, timeout=3)


# bleow are some basic method calls as tests 

# clears input buffer by reading all available data
clear_buffer = lidar.clear_input()
print(f"data in the input buffer:\n{clear_buffer}\n")

info = lidar.info
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