#!/usr/bin/python3

import serial
import sys
import json
import click
import itertools

def try_parse_line(ser):
    line = None
    try:
        l = ser.readline().decode('utf-8').rstrip()
        json.loads(l)
        line = l
    except KeyboardInterrupt:
        raise
    except:# json.decoder.JSONDecodeError:
        pass

    return line

def WaitingLine():
    dots = itertools.cycle(['.    ', '..   ', '...  ', '.... ', '.....'])
    slashes = itertools.cycle(['\\', '|', '/', '-'])
    while True:
        yield ('\r' + next(slashes) + next(dots))


def debug_read(ser):
    try:
        waiting = False
        waitingLine = WaitingLine()
        while True:
            line = ser.readline().decode('utf-8').rstrip()

            if line and len(line) > 0:
                if waiting: 
                    sys.stdout.write("\r")
                    waiting = False
                    waitingLine = WaitingLine()

                sys.stdout.write(line + "\n")
            else:
                waiting = True
                sys.stdout.write(next(waitingLine))

    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)

def default_read(ser):
        print("Starting to read data from serial port...")
        print("Press Ctrl+C to stop reading...")
        doc = "["
        running = True
        try:
            i = 0
            while True:
                if line := try_parse_line(ser):
                    i += 1
                    sys.stdout.write("Number read: \t\r%d" % i)
                    line += ",\n"
                    doc += line
                    if not running:
                        line += "]"
                        break

        except KeyboardInterrupt:
            if not running:
                raise
            else:
                running = False

        except Exception as e:
            print(e)
            sys.exit(1)

        with open("data.json", "w") as f:
            print("Writing to file...")
            f.write(doc)
            print("Done!!!")
            sys.exit(0)

@click.command()
@click.option('--debug', is_flag=True, default=False, help='debug')
def main(debug):
    with serial.Serial('/dev/ttyUSB0', 115200, timeout=1) as ser:
        if (debug):
                debug_read(ser)

        else:
            default_read(ser)

if __name__ == "__main__":
    main()
