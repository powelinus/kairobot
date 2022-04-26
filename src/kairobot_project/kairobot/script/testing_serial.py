#!/usr/bin/python

import serial
import time

ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
ser.flush()

while True:
    ser.write("Raspi initialized\n".encode('utf-8'))
    print("kirim")
    time.sleep(1)
