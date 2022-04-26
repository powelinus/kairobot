#!/usr/bin/env python
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyTHS1', 115200, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().rstrip()
            print(line)
        #ser.write("Hello from Raspberry Pi!\n".encode('utf-8'))
        time.sleep(2)
