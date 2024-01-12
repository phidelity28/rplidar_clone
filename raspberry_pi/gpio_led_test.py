
"""
    
Basic orientation testing and explorations to the Raspberry Pi Gpio interface

    
"""

from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(3)
    print("ON\n")
    led.off()
    sleep(3)
    print("hi Rafe - doesnt seem like 3 seconds does it")