
"""
    
Basic orientation testing and explorations to the Raspberry Pi Gpio interface

 this script works but the unusual item is the measurement across the ground from pin 6 ( 3rd pin on right column)
 to pin 11 (ID GPIO 17)   is opposite to my expectation.  Zero voltage is measured during what is labeled as the on phase
 an 3.3 (approx) during the off phase (aka when thme message in the console prints "Hi rafe ...")
"""

#from gpiozero import LED
import gpiozero as gp
from time import sleep
output_5v = gp.DigitalOutputDevice(2)
control_motor = gp.LED(17)
input_frm_white_blue_wire = gp.DigtalInputDevice(15)

while True:
    control_motor().on()
    print(input_frm_white_blue_wire.value())