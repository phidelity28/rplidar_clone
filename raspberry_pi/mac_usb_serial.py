import serial

# Replace 'COMx' with the appropriate serial port on your system (e.g., '/dev/ttyUSB0' on Linux)
serial_port = '/dev/tty.usbserial@14144000'  # Replace with your actual serial port
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate, timeout=1)

try:
    while True:
        # Read data from the serial port
        data = ser.readline().decode('utf-8').strip()
        
        if data:
            print(f"Received: {data}")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    ser.close()
