from ada_rplidar_serial import RPLidar
import os
from math import floor
import gpiozero as gp

from digitalio import DigitalInOut
import serial

# for use with serial port usb
PORT_NAME  = '/dev/ttyUSB0'

from time import sleep
# gpio standard for pin declaration
dc_pin = 2
motor_pin = 13
tx_pin = 14
rx_pin = 15

output_5v = gp.DigitalOutputDevice(dc_pin) #the arg is the pinnumber not the io
motor_control_pwm = gp.DigitalOutputDevice(motor_pin)


# attempt with our uart  this through an error as I was attempting to configure the tx rx ports 
gp_transmit = gp.DigitalOutputDevice(tx_pin) #  gpio / BCM numbering defualt tx pin
gp_receive = gp.DigitalInputDevice(rx_pin) # default /Bcm rx pin

#esp_control_v = DigitalInOut
output_5v.on()
motor_control_pwm.on()

baud_rate = 115200
port_serial = '/dev/ttyUSB0'
ser = serial.Serial(port=port_serial, baudrate=9600, timeout=4)
sleep(5)
esp_1 = RPLidar(motor_pin=motor_pin, port=port_serial, timeout=3)
# the line bellow is a teminal use case only
#  infor = serial.tools.list_ports.ListPortInfo(ser)

try: 
    while True:
        #read gpio input
        ser.write(b"hello usb")
        bytes = 7
        # read_input_esp = ser.read(bytes)
        # print(f"the type of data in the serial read is : {type(read_input_esp)}\n")
        # print(f"this is the input form the serial port : {read_input_esp}")
        # print(f"serial input buffer w in _waiting func :{ser.in_waiting}\n")
        
        # print(f"serial ouput buffer w in _waiting func :{ser.out_waiting}\n")
        gp_in_data = gp_receive.value
        print(f"this is the type of gp input data object {type(gp_in_data)}\n")
        print(f"this is the data {gp_in_data}\n")
        # ser.write(str(gp_in_data).encode())
        # print(f"attempting data ser.readline {ser.readline()}")
        

        # test the tx data
        gp_tx_data = gp_transmit.value
        print(f"tx data {type(gp_tx_data)}\n")
        print(f"tx data {gp_tx_data}\n")
        ser.write(str(gp_in_data).encode())


except KeyboardInterrupt:
    pass


lidar = RPLidar(motor_pin=motor_pin, port=port_serial, timeout=3)

# bleow are some basic method calls as tests 

# clears input buffer by reading all available data
#clear_buffer = lidar.clear_input()
#print(f"\n data in the input buffer:\n{clear_buffer}\n")

ser.close()

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